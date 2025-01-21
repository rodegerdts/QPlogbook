# import math
# from geopy.exc import GeopyError
from datetime import datetime, timedelta
from time import sleep
# from geographiclib.geodesic import Geodesic
# from geopy.geocoders import Nominatim
from point4D import Point4d
import json
import requests
# import gpxpy
# import gpxpy.gpx



class PointBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self,size_max):
        self.max = size_max
        self.data = []


    class __Full:
        """ class that implements a full buffer """
        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def getdata(self):
            """ return list of elements in correct order """
            return self.data[self.cur:]+self.data[:self.cur]
        

    def append(self,x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def getdata(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data
    

def get_sog(pointlist, age=0, averaging=0):
    lst = pointlist
    if len(lst) >= age + averaging + 1:
        return lst[len(lst)-age-1].getSOG(lst[len(lst)-age-2-averaging])
    else: 
        return None

def get_cog(pointlist, age=0, averaging=0):
    lst = pointlist
    if len(lst) >= age + averaging + 1:
        return lst[len(lst)-age-1].getCOG(lst[len(lst)-age-2-averaging])
    else: 
        return None


def get_gpx(pointlist):
    gpx = gpxpy.gpx.GPX()
    
    gpx_track = gpxpy.gpx.GPXTrack() # Create first track in our GPX:
    gpx.tracks.append(gpx_track)

    gpx_segment = gpxpy.gpx.GPXTrackSegment()  # Create first segment in our GPX track:
    gpx_track.segments.append(gpx_segment)

    for point in pointlist:
        tp = gpxpy.gpx.GPXTrackPoint(point.lat, point.lon, time=point.time)
        gpx_segment.points.append(tp)

    return gpx



def append_gpx(pointlist, gpx):
    gpx_track = gpx.tracks[len(gpx.tracks)-1]

    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    for point in pointlist:
        tp = gpxpy.gpx.GPXTrackPoint(point.lat, point.lon, time=point.time)
        gpx_segment.points.append(tp)



def getSKpoint4D(config):
    server = config["server"]
    dt = config["path"]["datetime"].replace(".", "/")
    position = config["path"]["position"].replace(".", "/")
    timeresp = requests.get(f"http://{server}/signalk/v1/api/vessels/self/{dt}/value", timeout=0.1, verify=False)
    timedata = json.loads(timeresp.content)
    time = datetime.fromisoformat(timedata)
    posresp = requests.get(
        f"http://{server}/signalk/v1/api/vessels/self/{position}/value",
        timeout=0.1,
        verify=False,
    )
    hdopresp = requests.get(
        f"http://{server}/signalk/v1/api/vessels/self/{position}/value",
        timeout=0.1,
        verify=False,
    )

    posdata = json.loads(posresp.content)
    hdopdata = json.loads(hdopresp.content)
    if posdata["latitude"] == 0 and posdata["longitude"] == 0 or hdopdata > 5:
        return None
        print("no gps position yet")
    else:
        p = Point4d(time, posdata["latitude"], posdata["longitude"])
        return p
  
  

def getStatus(pointlist, status):
    """ Returns the status of the vessel based on the last points in the pointlist """
    if len(pointlist) < 3:
        pass
    elif get_sog(pointlist, 0, 0) < 0.5 and get_sog(pointlist, 1, 0) < 0.5 and get_sog(pointlist, 2, 0) < 0.5:
        status = "stopped"
    elif get_sog(pointlist, 0, 0) >= 0.5 and get_sog(pointlist, 1, 0) >= 0.5 and get_sog(pointlist, 2, 0) >= 0.5:
        status = "moving"
    else:
        pass
    return status





# testing:
if __name__=='__main__':
    time1 = datetime.fromisoformat('2024-10-27T12:48:47.000Z')
    p = Point4d(time1, 67.29335, 14.39792)
    x=PointBuffer(6)
    d = 0
    stat = "not defined"
    for i in range(10):
        x.append(p)     
        d = 1/60
        lat = p.lat + d
        lon = p.lon 
        ptime = p.time + timedelta(minutes = 1)
        p = Point4d(ptime, lat, lon)
        stat = getStatus(x.getdata(), stat)
        print(stat)
        sleep(1)
    for i in range(10):
        x.append(p)     
        d = 1/60
        lat = p.lat 
        lon = p.lon 
        ptime = p.time + timedelta(minutes = 1)
        p = Point4d(ptime, lat, lon)
        stat = getStatus(x.getdata(), stat)
        print(stat)
        sleep(1)

    # print(x.getdata())
    # print(get_sog(x.getdata(), 4))
    # print(get_sog(x.getdata()))
    # gpxtrack = get_gpx(x.getdata())
    # append_gpx(x.getdata(), gpxtrack)
    # print(gpxtrack.to_xml())

