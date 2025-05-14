
import yaml
import json
import glob
import os
import math
from point4D import Point4d
from copy import deepcopy
from datetime import datetime

keymap = {"point": "point",
          "text": "text",
          "position_source": "fixtype",
          "log": "log",
          "engine_hours": "enginehours",
          "course": "cog",
          "heading": "heading",
          "speed_sog": "sog",
          "speed_stw": "stw",
          "barometer": "airpressure",
          "wind_speed": "tws",
          "wind_direction": "twd"}




# Import and export functions:


def getSKlog(path: str) -> list:
    """Reads and parses a SignalK logbook YAML file
    
    Args:
        path (str): Path to the file to import
        
    Returns:
        SKlog (list): A list of dictionarys in SK logbook format
        """
    
    with open(path, 'r') as file:
        SKlog = yaml.safe_load(file)
    return SKlog





def importdir(path):
    """Reads and concatenates all SKlogbook yaml files in a directory into a log
    
    Args:
        
    """
    filelog = glob.glob("*.yml", root_dir = path)
    pathlog = []
    log = []
    for i in filelog:
        pathlog.append(path + '/' + i)       
    for j in pathlog:
        log.extend(getSKlog(j))
    return log



def flatten(dic, parent_key=''):
        items = []
        for k, v in dic.items():
            try:
                items.extend(flatten(v, '%s%s_' % (parent_key, k)).items())
            except AttributeError:
                items.append(('%s%s' % (parent_key, k), v))
        return dict(items)



def logmap(inlog, map):
    """Maps the SK log to a new log of dictionarys according to 
    a dictionary map. Datetime, logitude and latitude are 
    convertewrt to a point4D object."""
    log =[]

    def flatten(dic, parent_key=''):
        items = []
        for k, v in dic.items():
            try:
                items.extend(flatten(v, '%s%s_' % (parent_key, k)).items())
            except AttributeError:
                items.append(('%s%s' % (parent_key, k), v))
        return dict(items)
    
    for i in inlog:
        i =flatten(i)
        i["point"] = Point4d(i["datetime"], i["position_latitude"], i["position_longitude"])
        newdict ={}
        for (oldkey, newkey) in map.items():         
            try:
                newdict.update({newkey: i[oldkey]})        
            except KeyError:
                pass
        log.append(newdict)
    return log



def serialize_log(log: list) -> str:
    """Serializes the log til JSON"""
    lg = deepcopy(log)
    for i in lg:
        i["point"] = {"time": i["point"].time.isoformat(), "lat": i["point"].lat, "lon": i["point"].lon}
        #i.update({"point": spoint})
    ojs = json.dumps(lg, indent=4)
    return ojs

def serialize_entry(entry: dict) -> str:
    """Serializes a single log entry to JSON"""
    entry["point"] = {"time": entry["point"].time.isoformat(), "lat": entry["point"].lat, "lon": entry["point"].lon}
    ojs = json.dumps(entry, indent=4)
    return ojs



def deserialize_log(jn: str) -> dict:
    """Reads a JSON string and returns a list of dictionarys"""
    log = json.loads(jn)
    for i in log:
        i["point"]["time"] = datetime.fromisoformat(i["point"]["time"])
        i["point"] = Point4d(i["point"]["time"], i["point"]["lat"], i["point"]["lon"])
    return log



def getQPlog(path):
    with open(path, 'rt') as file:
        f = file.read()
        QPlog = deserialize_log(f)
    return QPlog


def splitmonthly(log: list) -> dict:
    """Splits a logbook into a dictionary of monthly logs"""
    logs = {}
    for i in log:
        month = i["point"].time.strftime("%Y-%m")
        if month in logs:
            logs[month].append(i)
        else:
            logs[month] = [i]
    return logs
        

def split_dayly(log):
    """Splits a logbook into a dictionary of dayly logs"""
    logs = {}
    for i in log:
        day = i["point"].time.strftime("%Y-%m-%d")
        if day in logs:
            logs[day].append(i)
        else:
            logs[day] = [i]
    return logs



# -----------------------------------------------------------------------------------------
# Cleanup functions:


def remove_empty(logdict):
    """Removes all empty values from a logentry including nested dicts.
    
    Args:
        logdict (dict): logentry to be cleaned up
    
    Returns:
        Nothing:   manipulates logdict directly

    """
    iter = deepcopy(logdict)
    for key in iter.keys():
        if logdict[key] == {} or logdict[key] == [] or logdict[key] == "":
            logdict.pop(key)
        elif isinstance(logdict[key], dict):
            remove_empty(logdict[key])
            if logdict[key] == {} :
                logdict.pop(key)
    return logdict

                 

def merge_entrys(d1: dict, d2: dict) -> dict:
    """Used to merge a dublicate logentry to a single entry with minimal data loss.
    
    Args:
        d1 (dict): A logbook entry.
        d2 (dict): A 2nd logbook entry d1 is merged into.

    Returns:
        merged (dict): A merged logbook entry.
    """

    merged = {**d1, **d2}
    for key in merged.keys():
        if d1.get(key, "") == d2.get(key, ""):
            pass
        elif key == "text" and d1.get(key, "") != d2.get(key, ""):
            merged[key] = d1.get(key, "") + d2.get(key, "")
        elif isinstance(merged[key], dict):
            merged[key] = {**d1.get(key,  {}), **d2.get(key, {})}
        elif isinstance(merged[key], list):
            merged[key] = set(d1.get(key, "") + d2.get(key, ""))
            merged[key]  = list(merged[key])
            merged[key].sort()

    return merged



def cleanup(log):
    """Takes a log of logbook entrys 
        - sorts entrys by time
        - removes emty items 
        - removes dublicate entrys
        
    Args:
        log (list): a list of logbook entrys

    Returns:
        log (list): a modified list of logbook entrys
    """
    lst = deepcopy(log)
    lst.sort(key = lambda d: d["point"].time)
    for indx, val in enumerate(lst): # remove empty items
        remove_empty(lst[indx])
    for indx, val in enumerate(lst): # remove dublicae entrys
        if indx < len(lst)-1:
            if lst[indx]['point'] == lst[indx+1]['point']:
                lst[indx] = merge_entrys(lst[indx], lst[indx+1])
                lst.pop(indx+1)
    return lst


# convert functions:

def dg_mi(decdeg): 
    """convert decimal deg. to deg. decimal min. as found in the nautical almanac"""
    deg = math.trunc(decdeg)
    decmin = round(abs((decdeg - deg)*60), 1)
    if decmin == 60.0:
        deg += 1
        decmin = 0.0
    return str(deg) + "°" + str(decmin) + "'"


def dg_min_pos(lat, lon):
    '''Returns:
        A tupel of strings in human readable format. (Degrees, deciaml minutes for celstial derived positions)
    '''

    if lon < 0 :
        we = "W"
    else:
        we = "E"
    if lat < 0 :
        ns = "S"
    else:
        ns = "N"
    dgspos = (dg_mi(lat) +  ns, dg_mi(lon) + we)
    return dgspos


def mk_deg(deg, min):
    '''Returns:
        A float in decimal degrees from degrees and decimal minutes.
    '''
    return deg + min/60

def mk_decpos(deg_lat, min_lat, deg_lon, min_lon, ns, we):
    '''Returns:
        A tupel of floats in decimal degrees for degrees and decimal minuts positions.
    '''
    if ns == "S":
        lat = -mk_deg(deg_lat, min_lat)
    else:
        lat = mk_deg(deg_lat, min_lat)
    if we == "W":
        lon = -mk_deg(deg_lon, min_lon)
    else:
        lon = mk_deg(deg_lon, min_lon)
    return (lat, lon)




# ----------------------------------------------------------
# testing:

if __name__=='__main__':
    # d1 =  {"a": 1, "b": 2, "c": 3, "g": {"e": 5, "f": 6}, "k": ["Karin", "Enno", "Steffi"]}
    # d2 =  {"a": 1.1, "b": 2.2, "d": 4.4, "i": {"e": 5.5, "h": 7.7, "n": ""}, "j": {}, "k": ["Karin", "Enno", "Klaus"], "l": {"m": ""}}
    # time1 = datetime.fromisoformat('2024-10-27T12:48:47.000Z')
    # time2 = datetime.fromisoformat('2024-10-27T12:59:47.000Z')
    # time3 = datetime.fromisoformat('2024-10-27T12:59:50.000Z')
    # pp =  Point4d(time3, 67.28411, 14.35660)
    # ppp = Point4d(time2, 67.28411, 14.35651)
    # p = Point4d(time1, 67.29335, 14.39792)
    # d1["point"] = pp
    # d2["point"] = ppp
    # list1 = [d1, d2]
    # basedir = os.getcwd()
    # # print(basedir)
    # # dic = importdir(basedir)
    # # dic = getSKlog("/Users/enno/Documents/dev/VScode/VSCpython/testlog.yml")
    dic = getQPlog("/Users/enno/Documents/dev/QPlogbook/log/2024-08.json")
    # # dic = merge_entrys(d1, d2)
    # # di = flatten(dic[2])
    # # di = logmap(dic, keymap)
    # d = cleanup(list1)
    # print(d)
    # print(list1[0]["point"] == list1[1]["point"])
    
    # serial = serialize_log(d)

    # print(json.loads(serial))
    # log = deserialize_log(serial)
    # print(serial)
    # print("di: ", di[1]["point"])
    # print("log: ", log[1]["point"])
    # print(di == log)

    print(dic)