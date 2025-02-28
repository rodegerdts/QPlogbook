import skyfield.api as sf
from skyfield.data import hipparcos, mpc, stellarium
from skyfield.magnitudelib import planetary_magnitude
from datetime import datetime
from point4D import Point4d
import os
import pandas as pd
import math
import orjson

from PySide6.QtCore import Qt, QAbstractListModel, QDateTime
from PySide6.QtWidgets import QWidget, QDialog, QApplication, QMessageBox, QFileDialog
from ui.cellnav_ui import Ui_CelNavigation
from ui.dialog_sight_ui import Ui_DialogSight
import iofunctions

# Variables and objects
pl = {"Venus": "venus", "Mars": "MARS BARYCENTER", "Jupiter": "JUPITER BARYCENTER", "Saturn": "SATURN BARYCENTER",
       "SunUL": "sun", "SunLL": "sun", "MoonUL": "moon", "MoonLL": "moon",
         "Uranus": "URANUS BARYCENTER", "Neptune": "NEPTUNE BARYCENTER", "Pluto": "PLUTO BARYCENTER", "Mercury": "mercury"}

nav_obj = ["SunUL", "SunLL", "MoonUL", "MoonLL", "Venus", "Mars", "Jupiter", "Saturn", "Acamar", "Achernar",
            "Acrux", "Adhara", "Aldebaran", "Alioth", "Alkaid", "Alnair", "Alnilam", "Alphard", "Alphecca",
              "Alpheratz", "Altair", "Ankaa", "Antares", "Arcturus", "Atria", "Avior", "Bellatrix", "Betelgeuse",
                "Canopus", "Capella", "Deneb", "Denebola", "Diphda", "Dubhe", "Elnath", "Eltanin", "Enif", "Fomalhaut",
                  "Gacrux", "Gienah", "Hadar", "Hamal", "Kaus_Australis", "Kochab", "Markab", "Menkar", "Menkent",
                    "Merak", "Miaplacidus", "Mirfak", "Nunki", "Peacock", "Polaris", "Pollux", "Procyon", "Rasalhague",
                      "Regulus", "Rigel", "Rigil_Kentaurus", "Sabik", "Schedar", "Shaula", "Sirius", "Spica",
                        "Suhail", "Vega", "Zubenelgenubi"]


# Create a timescale and ask the current time.
sf_dir = os.path.dirname(os.path.realpath(__file__)) + "/" + "data/skyfield-data"
load = sf.Loader(sf_dir)

ts = sf.load.timescale()
t = ts.utc(2025, 1, 26, 15, 00)



# Load the JPL ephemeris.
#planets = load('de421.bsp') # use this if you want to download the ephemeris
planets = sf.load_file(sf_dir + "/" + 'de440exc.bsp') # a shortened version of de440s.bsp without data from the past.

# load star catalog
with load.open(sf_dir + "/hip_main.dat") as f:
    stars = hipparcos.load_dataframe(f)

# url2 = ('https://raw.githubusercontent.com/Stellarium/stellarium/master'
#        '/skycultures/modern_iau/star_names.fab')

starnamesfile = sf_dir + "/star_names.fab"
with load.open(starnamesfile) as f2:
    star_names = stellarium.parse_star_names(f2)

#star_names = stellarium.parse_star_names(starnamesfile)

starnames = {}
for star in star_names:
    starnames[star.name] = star.hip

# conf file
conf_file = os.path.dirname(os.path.realpath(__file__)) + "/" + "data/conf.json"

with open(conf_file, "r") as conffile:
        conf = orjson.loads(conffile.read())

astro_folder = conf["qplogfolder"] + "/astro/"



# functions ####################################################################

def dr_pos(sog, cog, t1, t2, lat, lon):
    """Calculates the dead reconing position from the course and speed over ground"""
    d = sog * (t2 - t1).total_seconds() / 3600
    #print(f"d:{d}")
    lat = math.radians(lat)
    lon = math.radians(lon)
    cog = math.radians(cog)
    d_lat = math.radians(d/60) * math.cos(cog)
    #print(f"d_lat:{math.degrees(d_lat)}")
    d_lon = math.radians(d/60) * math.sin(cog) / math.cos(lat)
    #print(f"d_lon:{math.degrees(d_lon)}")
    lat_out = d_lat + lat
    lon_out = d_lon + lon
    return (math.degrees(lat_out), math.degrees(lon_out))


def corrections(Hs, hoe=0, temp=15, press=1013, ie=0):
    """Corect sekstant alitude Hs for index error, dip and refraction.
    No paralax rorrection needed since this is calculated by the skyfield library"""
    D = 0.0293 * math.sqrt(hoe) # dip
    #print(f"D: {D}")
    H = Hs + ie - D
    R0 = 0.0167 / math.tan(math.radians(H + 7.32 / (H + 4.32))) # standart refraction
    R = R0 * ( 0.28 * press / (273 + temp)) # correction for temperature and pressure
    #print(f"R0: {R0} R: {R}")
    return H - R # corrected altitude Ho



def serialize_sights(sights):
    '''Returns:
        A JSON sstring with the sights data.
    '''
    s = []
    for si in sights:
        d = {}
        d["time"] = si.time
        d["lat"] = si.lat
        d["lon"] = si.lon
        d["body"] = si.body
        d["Hs"] = si.Hs
        d["Ha"] = si.Ha
        d["ie"] = si.ie
        d["hoe"] = si.hoe
        d["temperature"] = si.temperature
        d["pressure"] = si.pressure
        s.append(d)
    ojs = orjson.dumps(s, option=orjson.OPT_INDENT_2)
    return ojs.decode("utf-8")


def deserialize_sights(json):
    '''Returns:
        A list of sight objects.
    '''
    s = orjson.loads(json)
    sights = []
    for si in s:
        sights.append(Sight(datetime.fromisoformat(si["time"]), si["lat"], si["lon"], si["body"], si["Hs"], si["Ha"], si["ie"], si["hoe"], si["temperature"], si["pressure"]))
    return sights


# classes ######################################################################

class Sight:
    def __init__(self, time, lat, lon, body, Hs, Ha, ie, hoe, temp, press):
        """A class to hold a sigle sight.
        Calculates and stores the intercept"""
        self.time = time
        self.lat = lat
        self.lon = lon
        self.body = body
        self.Hs = Hs
        self.Ha = Ha
        self.ie = ie
        self.hoe = hoe
        self.temperature = temp
        self.pressure = press

        self.ts = sf.load.timescale()
        self.t = ts.from_datetime(self.time)

    def __str__(self):
        return f"{self.body} {self.time.strftime('%H:%M:%S')}  Alt: {iofunctions.dg_mi(self.Ha)}"

    def get_ic_az(self):
        if self.body in starnames:
            #print(f"Star: {self.body}")
            self.star = sf.Star.from_dataframe(stars.loc[starnames[self.body]])
            star_data = stars.loc[starnames[self.body]]
            self.magnitude = star_data['magnitude'] 
            self.earth = planets['earth']
            self.ap = self.earth + sf.wgs84.latlon(self.lat, self.lon)
            self.astrometric = self.ap.at(self.t).observe(self.star)
        elif self.body in pl:
            self.earth, self.bo = planets['earth'], planets[pl[self.body]]
            self.ap = self.earth + sf.Topos(latitude_degrees=self.lat, longitude_degrees=self.lon)
            self.astrometric = self.ap.at(self.t).observe(self.bo)
            if self.body != "SunUL" and self.body != "SunLL" and self.body != "MoonUL" and self.body != "MoonLL":
                self.magnitude = planetary_magnitude(self.astrometric)
        self.Hc, self.az, self.d = self.astrometric.apparent().altaz()
        if self.body == "SunLL" or self.body == "SunUL":
            self.magnitude = -26.74
            self.semidiameter = math.degrees(math.asin(1392700 / self.d.km)/2)
            # if self.body == "SunUL":
            #     self.intercept = self.Ha - self.Hc.degrees
            # else:
            #     self.intercept = self.Ha - self.Hc.degrees - self.semidiameter
        elif self.body == "MoonLL" or self.body == "MoonUL":
            self.magnitude = -12.74
            self.semidiameter = math.degrees(math.asin(3474.8 / self.d.km)/2)
            # if self.body == "MoonUL":
            #     self.intercept = self.Ha - self.Hc.degrees
            # else:
            #     self.intercept = self.Ha - self.Hc.degrees
        # else:
        self.intercept = self.Ha - self.Hc.degrees
        # print(f"{self.t.utc_iso()} {self.body}: Hc:{self.Hc.degrees} Azimut: {self.az.degrees} Intercept:{self.intercept} magnitude:{self.magnitude}")
        return (self.intercept, self.az.degrees, self.Hc.degrees, self.magnitude)



class Fix:
    """A class to hold and calculate a running fix based on a list of sights 
     as described in the nautical almanac"""
    def __init__(self, sights, sog=0, cog=0):
        self.sights = sights
        self.sights.sort(key=lambda x: x.time, reverse=True)
        self.fix = None
        self.lon = math.radians(self.sights[0].lon)
        self.lat = math.radians(self.sights[0].lat)
        #print(self.sights)
    
        def update_sights(self):
            for s in self.sights:
                if s == self.sights[0]:
                    s.lon = math.degrees(self.lon)
                    s.lat = math.degrees(self.lat)
                else:
                    runningpos = dr_pos(sog, cog, self.sights[0].time, s.time, math.degrees(self.lat), math.degrees(self.lon))
                    s.lon = runningpos[1]
                    s.lat = runningpos[0]
                #print(f"{s.body} {s.time} {dg_mi(s.lat)} {dg_mi(s.lon)}")

        for i in range(10):
            update_sights(self)
            A = B = C = D = E = 0.0
            for s in self.sights:
                icac = s.get_ic_az()
                ic = math.radians(icac[0])
                az = math.radians(icac[1])
                A += math.cos(az)**2
                B += math.cos(az) * math.sin(az)
                C += math.sin(az)**2
                D += ic * math.cos(az)
                E += ic * math.sin(az)
            G = A * C - B**2
            Li = self.lon + (A*E - B*D) / (G * math.cos(self.lat))
            Bi = self.lat + (C * D - B * E) / G
            distance = math.sqrt((Li - self.lon)**2 * math.cos(self.lat)**2 + (Bi - self.lat)**2)
            #print(f"d: {distance} lat:{self.lat} lon:{self.lon} Li:{Li} Bi:{Bi}")
            self.lon = Li
            self.lat = Bi
            if distance < 0.00001:
                update_sights(self)
                break
                
        self.fix = (self.sights[0].time, math.degrees(self.lat), math.degrees(self.lon))



# Qt and PySide6 classes:


class SightsModel(QAbstractListModel):
    def __init__(self, sights):
        super().__init__()
        self.sights = sights

    def rowCount(self, parent):
        return len(self.sights)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.sights[index.row()].__str__()


class CelNavUi(QWidget, Ui_CelNavigation):
    def __init__(self, log=None, logmodel=None, lastpoint=None, indexerror=0, hoe=0):
        super().__init__()
        self.setupUi(self)
        self.l_changed()
        self.sights = []
        self.fix = None
        self.sog = 0
        self.cog = 0
        self.sights_model = SightsModel(self.sights)
        self.listView_sights.setModel(self.sights_model)
        self.log = log
        self.indexerror = indexerror
        self.pressure = 1013.25
        self.temperature = 15
        self.hoe = hoe
        self.logmodel = logmodel
        self.lastpoint = lastpoint

        self.doubleSpinBox_indexerror.setValue(self.indexerror)
        self.doubleSpinBox_hoe.setValue(self.hoe)

        self.button_new.clicked.connect(self.new_sight)
        self.button_calculateFix.clicked.connect(self.calculate_fix)
        self.button_calculateDR.clicked.connect(self.calculate_dr)
        self.button_close.clicked.connect(self.close_celnav)
        self.button_save.clicked.connect(self.save_astro)
        self.button_open.clicked.connect(self.open_astro)
        self.button_edit.clicked.connect(self.edit_sight)
        self.button_delete.clicked.connect(self.delete_sight)
        self.button_toLog.clicked.connect(self.to_log)

        self.comboBox_ns.addItems(["N", "S"])
        self.comboBox_we.addItems(["E", "W"])
        self.comboBox_ns.setCurrentIndex(0)
        self.comboBox_we.setCurrentIndex(0)
        self.spinBox_lat_deg.valueChanged.connect(self.l_changed)
        self.doubleSpinBox_lat_min.valueChanged.connect(self.l_changed)
        self.spinBox_lon_deg.valueChanged.connect(self.l_changed)
        self.doubleSpinBox_lon_min.valueChanged.connect(self.l_changed)
        self.comboBox_ns.currentIndexChanged.connect(self.l_changed)
        self.comboBox_we.currentIndexChanged.connect(self.l_changed)
        self.dateTimeEdit_dr.setDateTime(datetime.now())
        self.dateTimeEdit_dr.dateTimeChanged.connect(self.dr_time_changed)
        self.dr_time = datetime.fromisoformat(self.dateTimeEdit_dr.dateTime().toString(format= Qt.ISODate))

        #parameters
        self.doubleSpinBox_sog.valueChanged.connect(self.sog_changed)
        self.spinBox_cog.valueChanged.connect(self.cog_changed)
        self.doubleSpinBox_indexerror.valueChanged.connect(self.indexerror_changed)
        self.doubleSpinBox_pressure.valueChanged.connect(self.pressure_changed)
        self.doubleSpinBox_temperature.valueChanged.connect(self.temperature_changed)
        self.doubleSpinBox_hoe.valueChanged.connect(self.hoe_changed)


    def indexerror_changed(self):
        self.indexerror = self.doubleSpinBox_indexerror.value() / 60   

    def sog_changed(self):
        self.sog = self.doubleSpinBox_sog.value()

    def cog_changed(self):
        self.cog = self.spinBox_cog.value()

    def pressure_changed(self):
        self.pressure = self.doubleSpinBox_pressure.value()

    def temperature_changed(self):
        self.temperature = self.doubleSpinBox_temperature.value()

    def hoe_changed(self):
        self.hoe = self.doubleSpinBox_hoe.value()

    def l_changed(self):
        self.lat, self.lon = iofunctions.mk_decpos(self.spinBox_lat_deg.value(), self.doubleSpinBox_lat_min.value(),
                                        self.spinBox_lon_deg.value(), self.doubleSpinBox_lon_min.value(),
                                        self.comboBox_ns.currentText(), self.comboBox_we.currentText())
        #print(self.lat, self.lon)

    def dr_time_changed(self, qtime):
        self.dr_time = datetime.fromisoformat(qtime.toString(format= Qt.ISODate))
        #print(self.dr_time.isoformat())


    def calculate_dr(self):
        self.dr_time = datetime.fromisoformat(self.dateTimeEdit_dr.dateTime().toString(format= Qt.ISODate))
        newpos = dr_pos(self.sog, self.cog, self.lastpoint.time, self.dr_time, self.lastpoint.lat, self.lastpoint.lon)
        self.spinBox_lat_deg.setValue(math.trunc(abs(newpos[0])))
        self.doubleSpinBox_lat_min.setValue((abs(newpos[0]) - math.trunc(abs(newpos[0]))) * 60)
        self.spinBox_lon_deg.setValue(math.trunc(abs(newpos[1])))
        self.doubleSpinBox_lon_min.setValue((abs(newpos[1]) - math.trunc(abs(newpos[1]))) * 60)

    def new_sight(self):
        self.dialog = DialogSight(time=self.dr_time, lat=self.lat, lon=self.lon, hoe=self.hoe,
                                   pressure=self.pressure, temperature=self.temperature,
                                     ie=self.indexerror)
        if self.dialog.exec() == QDialog.Accepted:
            self.sights.append(self.dialog.sight)
            self.sights_model.layoutChanged.emit()
        else:
            pass

    def edit_sight(self):
        index = self.listView_sights.currentIndex().row()
        self.dialog = DialogSight(time=self.sights[index].time, lat=self.sights[index].lat, lon=self.sights[index].lon, body=self.sights[index].body, hoe=self.sights[index].hoe,
                                   pressure=self.sights[index].pressure, temperature=self.sights[index].temperature,
                                     alt=self.sights[index].Ha, ie=self.sights[index].ie, hs=self.sights[index].Hs)
        if self.dialog.exec() == QDialog.Accepted:
            self.sights[index] = self.dialog.sight
            self.sights_model.layoutChanged.emit()
        else:
            pass


    def calculate_fix(self):
        #print(self.sights)
        self.fix = Fix(self.sights, self.sog, self.cog)
        fix_pos = iofunctions.dg_min_pos(self.fix.fix[1], self.fix.fix[2])
        self.lineEdit_fix_lat.setText(fix_pos[0])
        self.lineEdit_fix_lon.setText(fix_pos[1])
        self.label_time_of_fix.setText(self.fix.fix[0].strftime("%H:%M:%S"))

    def to_log(self):
        if self.fix:
            self.entry = {}
            self.entry["point"] = Point4d(self.fix.fix[0], self.fix.fix[1], self.fix.fix[2])
            self.entry["fixtype"] = "celestial"
            sightstr = ""
            for si in self.sights:
                sightstr += (si.__str__() + "\n")
            self.entry["text"] = sightstr
            self.log.append(self.entry)
            self.logmodel.layoutChanged.emit()


    def delete_sight(self):
        """Delete the currently highlited sight"""
        index = self.listView_sights.currentIndex().row()
        del self.sights[index]
        self.sights_model.layoutChanged.emit()


    def save_astro(self):
        """Save the sights ad Fix to a file"""
        sights = serialize_sights(self.sights)
        safe_dict = {}
        safe_dict["sights"] = sights
        safe_dict["sog"] = self.sog
        safe_dict["cog"] = self.cog
        safe_dict["indexerror"] = self.indexerror
        safe_dict["pressure"] = self.pressure
        safe_dict["temperature"] = self.temperature
        safe_dict["hoe"] = self.hoe
        safe_dict["latitude"] = self.lat
        safe_dict["longitude"] = self.lon
        out = orjson.dumps(safe_dict, option=orjson.OPT_INDENT_2)

        filename = self.sights[0].time.strftime("%Y-%m-%d_%H-%M") + "_sights.json"
        os.makedirs(astro_folder, exist_ok=True) 
        with open(astro_folder + filename, "w") as sightsfile:
            sightsfile.write(out.decode("utf-8"))

    def open_astro(self):
        """Open a file with sights and Fix"""
        filename = QFileDialog.getOpenFileName(self, "Open file",
                                                astro_folder, "JSON files (*.json)")
        self.activefolder = os.path.dirname(filename[0])
        with open(filename[0], "r") as infile:
            read_in = infile.read()
        in_dict = orjson.loads(read_in)
        self.sog = in_dict["sog"]
        self.doubleSpinBox_sog.setValue(self.sog)
        self.cog = in_dict["cog"]
        self.spinBox_cog.setValue(self.cog)
        self.indexerror = in_dict["indexerror"]
        self.doubleSpinBox_indexerror.setValue(self.indexerror)
        self.pressure = in_dict["pressure"]
        self.doubleSpinBox_pressure.setValue(self.pressure)
        self.temperature = in_dict["temperature"]
        self.doubleSpinBox_temperature.setValue(self.temperature)
        self.hoe = in_dict["hoe"]
        self.doubleSpinBox_hoe.setValue(self.hoe)
        self.lat = in_dict["latitude"]
        self.spinBox_lat_deg.setValue(math.trunc(abs(self.lat)))
        self.doubleSpinBox_lat_min.setValue((abs(self.lat) - math.trunc(abs(self.lat))) * 60)
        self.lon = in_dict["longitude"]
        self.spinBox_lon_deg.setValue(math.trunc(abs(self.lon)))
        self.doubleSpinBox_lon_min.setValue((abs(self.lon) - math.trunc(abs(self.lon))) * 60)
        self.sights.clear()
        self.sights.extend(deserialize_sights(in_dict["sights"]))
        self.sights_model.layoutChanged.emit()
        


    def close_celnav(self):
        self.close()
        


class DialogSight(QDialog, Ui_DialogSight):
    def __init__(self, parent=None, time=datetime.now(), lat=0, lon=0, body="SunUL", hoe = 2, pressure=1013, temperature=25, alt=0, ie=0, hs=0):
        super().__init__(parent)
        self.setupUi(self)
        self.time = time
        self.qtime = QDateTime.fromString(self.time.isoformat(), Qt.ISODate)
        self.lat = lat
        self.lon = lon
        self.body = body
        self.hs = hs
        self.alt = alt
        self.ie = ie
        self.hc = None
        self.pressure = pressure
        self.temperature = temperature
        self.hoe = hoe

        self.dateTimeEdit_sight.setDateTime(self.qtime)
        self.comboBox_body.addItems(nav_obj)
        self.comboBox_body.setCurrentIndex(nav_obj.index(self.body))
        self.spinBox_alt_deg.setValue(math.trunc(self.alt))
        self.doubleSpinBox_alt_min.setValue((self.alt - math.trunc(self.alt)) * 60)
        self.spinBox_Hs_deg.setValue(math.trunc(self.hs))
        self.doubleSpinBox_Hs_min.setValue((self.hs - math.trunc(self.hs)) * 60) 


        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)
        self.dateTimeEdit_sight.dateTimeChanged.connect(self.body_changed)
        self.comboBox_body.currentTextChanged.connect(self.body_changed)
        self.spinBox_alt_deg.valueChanged.connect(self.alt_changed)
        self.doubleSpinBox_alt_min.valueChanged.connect(self.alt_changed)
        self.spinBox_Hs_deg.valueChanged.connect(self.hs_changed)
        self.doubleSpinBox_Hs_min.valueChanged.connect(self.hs_changed)
        self.button_Hs_to_Hc.clicked.connect(self.correct_hs_to_ho)
        self.button_actoalt.clicked.connect(self.actoalt)

        # position
        self.comboBox_ns.addItems(["N", "S"])
        self.comboBox_we.addItems(["E", "W"])
        self.comboBox_ns.setCurrentIndex(0) if self.lat > 0 else self.comboBox_ns.setCurrentIndex(1)
        self.comboBox_we.setCurrentIndex(0) if self.lon > 0 else self.comboBox_we.setCurrentIndex(1)
        self.spinBox_lat_deg.setValue(math.trunc(abs(self.lat)))
        self.doubleSpinBox_lat_min.setValue((abs(self.lat) - math.trunc(abs(self.lat))) * 60)
        self.spinBox_lon_deg.setValue(math.trunc(abs(self.lon)))
        self.doubleSpinBox_lon_min.setValue((abs(self.lon) - math.trunc(abs(self.lon))) * 60)
        self.spinBox_lat_deg.valueChanged.connect(self.l_changed)
        self.doubleSpinBox_lat_min.valueChanged.connect(self.l_changed)
        self.spinBox_lon_deg.valueChanged.connect(self.l_changed)
        self.doubleSpinBox_lon_min.valueChanged.connect(self.l_changed)
        self.comboBox_ns.currentIndexChanged.connect(self.l_changed)
        self.comboBox_we.currentIndexChanged.connect(self.l_changed)

        # parameters
        self.doubleSpinBox_indexerror.setValue(self.ie)
        self.doubleSpinBox_indexerror.valueChanged.connect(self.indexerror_changed)
        self.doubleSpinBox_pressure.setValue(self.pressure)
        self.doubleSpinBox_pressure.valueChanged.connect(self.pressure_changed)
        self.doubleSpinBox_temperature.setValue(self.temperature)
        self.doubleSpinBox_temperature.valueChanged.connect(self.temperature_changed)
        self.doubleSpinBox_hoe.setValue(self.hoe)
        self.doubleSpinBox_hoe.valueChanged.connect(self.hoe_changed)


    def indexerror_changed(self):
        self.ie = self.doubleSpinBox_indexerror.value()/60    

    def pressure_changed(self):
        self.pressure = self.doubleSpinBox_pressure.value()

    def temperature_changed(self):
        self.temperature = self.doubleSpinBox_temperature.value()

    def hoe_changed(self):
        self.hoe = self.doubleSpinBox_hoe.value()



    def correct_hs_to_ho(self):
        self.time = datetime.fromisoformat(self.dateTimeEdit_sight.dateTime().toString(format= Qt.ISODate))
        self.body = self.comboBox_body.currentText()
        self.sight = Sight(self.time, self.lat, self.lon, self.body, self.alt, self.hs, self.ie, self.hoe, self.temperature, self.pressure)
        if self.body == "SunLL" or self.body == "MoonLL":
            sd = self.sight.semidiameter
        elif self.body == "SunUL" or self.body == "MoonUL":
            sd = 0 - self.sight.semidiameter
        self.alt = corrections(self.hs+sd, self.hoe, self.temperature, self.pressure, self.ie)
        #print(f"Corrected altitude: {self.alt}")
        deg = math.trunc(self.alt)
        min = (self.alt - deg) * 60
        self.spinBox_alt_deg.setValue(deg)
        self.doubleSpinBox_alt_min.setValue(min)
        


    def alt_changed(self):
        self.alt = self.spinBox_alt_deg.value() + self.doubleSpinBox_alt_min.value()/60

    def hs_changed(self):
        self.hs = self.spinBox_Hs_deg.value() + self.doubleSpinBox_Hs_min.value()/60

    def body_changed(self, s):
        self.time = datetime.fromisoformat(self.dateTimeEdit_sight.dateTime().toString(format= Qt.ISODate))
        self.body = self.comboBox_body.currentText()
        self.sight = Sight(self.time, self.lat, self.lon, self.body, self.alt, self.hs, self.ie, self.hoe, self.temperature, self.pressure)
        ic, az, self.hc, mag = self.sight.get_ic_az()
        # if self.body == "SunLL" or self.body == "MoonLL":
        #     self.hc = self.hc + self.sight.semidiameter
        #     print(f"LL: {self.hc} {self.sight.semidiameter}")
        # elif self.body == "SunUL" or self.body == "MoonUL":
        #     self.hc = self.hc - self.sight.semidiameter
        #     print(f"UL: {self.hc} {self.sight.semidiameter}")
        self.label_az.setText(f" Az: {math.trunc(az)}˚")
        self.label_hc.setText(f" Hc: {iofunctions.dg_mi(self.hc)} mag:{mag}")

    def actoalt(self):
        #self.Hc = self.sight.get_ic_az()[2]
        if self.hc:
            #print(f"actoalt clicked {math.trunc(self.hc)}")
            self.spinBox_alt_deg.setValue(math.trunc(self.hc))
            self.spinBox_Hs_deg.setValue(math.trunc(self.hc))
            self.doubleSpinBox_alt_min.setValue((self.hc - math.trunc(self.hc)) * 60)
            self.doubleSpinBox_Hs_min.setValue((self.hc - math.trunc(self.hc)) * 60)
        else:

            msg = QMessageBox.information(self, "Warning", "No altitude calculated")



    def l_changed(self):
        self.lat, self.lon = iofunctions.mk_decpos(self.spinBox_lat_deg.value(), self.doubleSpinBox_lat_min.value(),
                                        self.spinBox_lon_deg.value(), self.doubleSpinBox_lon_min.value(),
                                        self.comboBox_ns.currentText(), self.comboBox_we.currentText())


    def accept(self):
        hs = self.spinBox_Hs_deg.value() + self.doubleSpinBox_Hs_min.value()/60
        alt = self.spinBox_alt_deg.value() + self.doubleSpinBox_alt_min.value()/60
        if (self.comboBox_body.currentText() in pl or self.comboBox_body.currentText() in starnames) and alt > 0 and alt < 90:
            qtime = self.dateTimeEdit_sight.dateTime()
            self.time = datetime.fromisoformat(qtime.toString(format= Qt.ISODate))
            self.sight = Sight(self.time, self.lat, self.lon, self.comboBox_body.currentText(), hs, alt, self.ie, self.hoe, self.temperature, self.pressure)
            QDialog.accept(self)
        else:
            print("Invalid input")
            QDialog.reject(self)



if __name__=='__main__':
    # #Ho = corrections(21.3283, 5.4, -3.0, 982)

    # test running fix
    # s = [0, 0, 0]
    # time1 = datetime.fromisoformat('2025-02-01T11:00:00.000Z')
    # s[0] = Sight(time1, 65.0, 14.5, 'Venus', 16.2927)
    
    # time2 = datetime.fromisoformat('2025-02-01T12:00:00.000Z')
    # s[1] = Sight(time2, 65.0, 10.5, 'SunLL', 5.4125)
    # time3 = datetime.fromisoformat('2025-02-01T13:00:00.000Z')
    # s[2] = Sight(time3, 65.0, 10.5, 'Hamal', 36.7055)
   
    # f = Fix(s, 23.44, 90)
    # print(f"Fix: {f.fix[0]} \n {dg_min_pos(f.fix[1], f.fix[2])}")

    #print(s[0])


    # time1 = datetime.fromisoformat('2025-01-29T17:48:40.000Z')
    # time2 = datetime.fromisoformat('2025-01-29T18:48:40.000Z')
    # print(dr_pos(23.44, 90, time1, time2, 67.0, 14.5))


    # test cellnav GUI
    import sys
    app = QApplication(sys.argv)
    w = CelNavUi()
    w.show()
    app.exec()
   