import math
from geopy.exc import GeopyError
from datetime import datetime, timedelta
from geographiclib.geodesic import Geodesic
from geopy.geocoders import Nominatim

geod = Geodesic.WGS84  # define the WGS84 ellipsoid

class Point4d:
    '''A class to hold position and time. 
    Also produces printable, human readable strings'''
    def __init__(self, time, lat, lon):
        if isinstance(time, str):
            self.time = datetime.fromisoformat(time)
        else:
            self.time = time
        self.lat = round(lat, 5)
        self.lon = round(lon, 5)

    def __repr__(self):
        return self.time.isoformat() + " " + repr(self.lat) + " " + repr(self.lon)
    
    def __str__(self):
        return self.time.strftime('%d.%m.%y %H:%M') + " " + self.getDMpos()[0] + " " + self.getDMpos()[1]

    def __eq__(self, other): 
        """Test for equality. Points are considred equal if within 10s and ca. 1m"""
        if isinstance(other, Point4d):
            return abs(self.time - other.time) <= timedelta(seconds = 30)  and abs(self.lon - other.lon) <= 0.0001 and abs(self.lat - other.lat) <= 0.0001
        else:
            return False

    def __sub__(self, other): 
        """Substraction of two points retuns a tuple with dist. in meter and timedelta."""
        self.g = geod.Inverse(self.lat, self.lon, other.lat, other.lon) 
        dist = self.g["s12"]
        return (dist, abs(self.time - other.time))

    def update(self, time, lat, lon):        
        self.time = time
        self.lat = lat
        self.lon = lon


    def getSOG(self, prepoint): 
        """Calculates SOG in kn
        
        Args:
            prepoint (Point4D): previous position

        Returns:
            sog (float): Speed over ground in kn
        """
        self.g = geod.Inverse(prepoint.lat, prepoint.lon, self.lat, self.lon) 
        dist = self.g["s12"]
        sog = dist / (self.time - prepoint.time).total_seconds() * 1.943844
        return round(sog, 1)
    
    def getCOG(self, prepoint): 
        """Calculates COG
        
        Args:
            prepoint (Point4D): Previous position

        Returns:
            cog (float): True course over ground in degrees
        """
        self.g = geod.Inverse(prepoint.lat, prepoint.lon, self.lat, self.lon)
        cog = self.g['azi1']
        if cog < 0:
            cog = 360 + cog
        return round(cog, 1)
    
    def getDMSpos(self): 
        """Returns a tupel of strings in human readable format. (Degrees, minutes, seconds for GPS positions)"""
        def DgMiSe(decdeg): # convert decimal deg. to deg. min. sec.
            deg = math.trunc(decdeg)
            decmin = abs((decdeg - deg)*60)
            min = abs(math.trunc((decdeg - deg)*60))
            sec = round((decmin - min) * 60 , 1)
            return str(deg) + "° " + str(min) + "′ " + str(sec) + '''″'''

        if self.lon < 0 :
            we = "W"
        else:
            we = "E"
        if self.lat < 0 :
            ns = "S"
        else:
            ns = "N"
        dgspos = (DgMiSe(self.lat) + " " + ns, DgMiSe(self.lon) + " " + we)
        return dgspos
    
    def getDMpos(self):
        '''Returns:
            A tupel of strings in human readable format. (Degrees, deciaml minutes for celstial derived positions)
        '''
        def DgMi(decdeg): #convert decimal deg. to deg. decimal min. as found in the nautical almanac
            deg = math.trunc(decdeg)
            decmin = round(abs((decdeg - deg)*60), 1)
            if decmin == 60.0:
                deg += 1
                decmin = 0.0
            return str(deg) + "°" + str(decmin) + "′"

        if self.lon < 0 :
            we = "W"
        else:
            we = "E"
        if self.lat < 0 :
            ns = "S"
        else:
            ns = "N"
        dgspos = (DgMi(self.lat) +  ns, DgMi(self.lon) + we)
        return dgspos
    
    def getplace(self):
        """Returns a placename for use in a logbook entry (not always entirely akkurate, requires internet)"""
        txt = f"{self.lat}, {self.lon}"
        try:
            geolocator = Nominatim(user_agent="qpylogbooktest")
            location = geolocator.reverse(txt)
        except GeopyError:       
            return "Geopy Error (Network?)"
        else:
            if "city" in location.raw["address"]:
                place = location.raw["address"]["city"]
            elif "village" in location.raw["address"]:
                place = location.raw["address"]["village"]
            elif "hamlet" in location.raw["address"]:
                place = location.raw["address"]["hamlet"]
            elif "farm" in location.raw["address"]:
                place = location.raw["address"]["farm"]
            else:
                place ="No placename found"
        
        return(place)

# testing:

if __name__=='__main__':
    time1 = datetime.fromisoformat('2024-10-27T12:48:47.000Z')
    time2 = datetime.fromisoformat('2024-10-27T12:59:47.000Z')
    time3 = datetime.fromisoformat('2024-10-27T12:59:50.000Z')
    pp =  Point4d(time3, 67.28411, 14.35660)
    ppp = Point4d(time2, 67.28411, 14.35651)
    p = Point4d(time1, 67.29335, 14.39792)

    print("equal:")
    print(pp == ppp)
    print(pp - ppp)
    print(repr(pp))
    print(str(pp))

    # pdict = {'lat': 67.29335, 'lon': 14.39792, 'time': '2024-10-27T12:59:47Z'}
    # p = jsons.load(pdict, Point4d)

    # dumped = jsons.dump(p, strict=True)
    # print(dumped)

    print(p.getSOG(pp))
    print(p.getCOG(pp))
    print(p.getDMSpos()[0])
    print(p.getDMSpos()[1])
    print(p.getDMpos())
    print(p.getplace())
    print(geod.a)