import json
import requests
import math
from point4D import Point4d
from datetime import datetime
from requests.exceptions import ConnectionError
import pointbuffer as pb
import os


# Global variables and objects:
buffer = pb.PointBuffer(60)




def getSKpoint4D(config):
    server = config["skserver"]
    dt = config["path"]["datetime"].replace(".", "/")
    position = config["path"]["position"].replace(".", "/")
    try:
        timeresp = requests.get(f"http://{server}/signalk/v1/api/vessels/self/{dt}/value", timeout=0.1, verify=False)
        posresp = requests.get(f"http://{server}/signalk/v1/api/vessels/self/{position}/value", timeout=0.1, verify=False)
    except (ConnectionError, requests.exceptions.ReadTimeout):
        print("Network timeout. SKserver not responding or too slow")
        return None
    timedata = json.loads(timeresp.content)
    time = datetime.fromisoformat(timedata)
    posdata = json.loads(posresp.content)
    if posdata["latitude"] == 0 and posdata["longitude"] == 0:
        print("no gps position yet")
        return None
    else:
        p = Point4d(time, posdata["latitude"], posdata["longitude"])
        return p


def getSKposition(server):
    try:
        posresp = requests.get(
            f"http://{server}/signalk/v1/api/vessels/self/navigation/position/value",
            verify=False,
        )
    except ConnectionError:
        print("Network timeout. SKserver not responding or too slow")
        return None
    posdata = json.loads(posresp.content)
    return posdata


def getSKdecposition(server):
    try:
        resp = requests.get(
            f"http://{server}/signalk/v1/api/vessels/self/navigation/position/value",
            verify=False,
        )
    except ConnectionError:
        print("Network timeout. SKserver not responding or too slow")
        return None
    posdata = json.loads(resp.content)
    return posdata


def getSKpath(config):
    """Returns a dictionary for all signalK paths configured in the configuratin file"""
    server = config["skserver"]
    sto = config["servertimeout"]
    out = {}
    for key in config["path"]:
        try:
            mpath = config["path"][key].replace(".", "/")
            resp = requests.get(
                f"http://{server}/signalk/v1/api/vessels/self/{mpath}/value",
                timeout=sto,
                verify=False,
            )
            out[key] = json.loads(resp.content)
        except ValueError:
            print(f"Value {key} not fount on SignalK server")
            pass
        except ConnectionError: 
            print(f"Network timeout. SKserver not responding or too slow \nServer IP: {server} \nTimeout setting: {sto}s")
            break

    if out == {} or out["datetime"] == None or out["position"]["longitude"] == None or out["position"]["latitude"] == None:
        nout = {"point": None}
    else:
        out["airpressure"] = out["airpressure"]/100
        out["airtemperature"] = out["airtemperature"] - 273.15
        out["datetime"] = datetime.fromisoformat(out["datetime"])
        point = Point4d(out["datetime"], out["position"]["latitude"], out["position"]["longitude"])
        for key in ["datetime", "position"]:
            out.pop(key)
        if "sog" in out:
            out["sog"] = round(out["sog"] * 1.94384, 1)
        if "cog" in out:
            out["cog"] = round(out["cog"] * 57.2957, 0)
        if "stw" in out:
            out["stw"] = round(out["stw"] * 1.94384, 1)
        if "heading" in out:
            out["heading"] = round(out["heading"] * 57.2957, 0)
        if "tws" in out:
            out["tws"] = round(out["tws"] * 1.94384, 1)
        if "twd" in out:
            out["twd"] = round(out["twd"] * 57.2957, 0)
        if "airtemperature" in out:
            out["airtemperature"] = round(out["airtemperature"], 1)
        if "airpressure" in out:
            out["airpressure"] = round(out["airpressure"], 1)
        if "humidity" in out:
            out["humidity"] = round(out["humidity"] *100, 0)
        nout = {"point": point}
        nout.update(out)
        return nout


def getStatic(conf):
    server = conf["server"]
    sto = conf["servertimeout"]
    out = {}
    for key in conf["staticpath"]:
        try:
            mpath = conf["staticpath"][key].replace(".", "/")
            resp = requests.get(
                f"http://{server}/signalk/v1/api/vessels/self/{mpath}",
                timeout=sto,
                verify=False,
            )
            out[key] = json.loads(resp.content)
            if isinstance(out[key], dict):
                out[key] = list(out[key].values())[0]
        except ValueError:
            print(f"Value {key} not fount on SignalK server")
            pass
        except ConnectionError: 
            print(f"Network timeout. SKserver not responding or too slow \nServer IP: {server} \nTimeout setting: {sto}s")
            break
    return out


def convertpos(lat, long):
    def DgMiSe(decdeg):
        deg = math.trunc(decdeg)
        decmin = abs((decdeg - deg) * 60)
        min = abs(math.trunc((decdeg - deg) * 60))
        sec = round((decmin - min) * 60)
        return str(deg) + "° " + str(min) + "′ " + str(sec) + """″"""

    if long < 0:
        we = "W"
    else:
        we = "E"
    if lat < 0:
        ns = "S"
    else:
        ns = "N"
    dgspos = DgMiSe(lat) + " " + ns + "\n" + DgMiSe(long) + " " + we
    return dgspos




if __name__=='__main__':
    conf_file = os.path.dirname(os.path.realpath(__file__)) + "/" + "data/conf.json"
    with open(conf_file, "r") as f:
        conf = json.loads(f.read())

    # mytime = getSKtime("192.168.0.70:3000")
    # mypos = getSKposition("192.168.0.70:3000")
    # mydecpos = getSKdecposition("192.168.0.70:3000")
    # mylong = DgMiSe(mydecpos["longitude"])
    # mysog = getSKpath("192.168.0.70:3000", conf)
    # unic = mypos.format_unicode()
    # dslon = round(float(unic[8:13]),0)
    # print (mytime)
    # print (mypos.format_unicode())
    # print (convertpos(mydecpos['latitude'], mydecpos['longitude']))
    # print (mylong)
    # print (mysog)
    # mypoint = getSKpoint4D(conf)
    # print(mypoint.getDMSpos()[0])

    print(getSKpath(conf))
    # print(getStatic(conf))
    # data = getSKpath(conf)
    # print(json.dumps(data, indent=4))