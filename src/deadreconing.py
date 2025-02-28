from ui.dialog_dr_ui import Ui_DialogDR
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDateTime, Qt    
from point4D import Point4d
from iofunctions import mk_decpos
from celnav import dr_pos
from datetime import datetime, timezone
import math
from geographiclib.geodesic import Geodesic





class DeadReckoning(QDialog, Ui_DialogDR):
    def __init__(self, parent=None, oldpoint=None):
        super().__init__(parent)
        self.setupUi(self)
        self.geod = Geodesic.WGS84  # define the WGS84 ellipsoid
        self.oldpoint = oldpoint
        self.old_time = self.oldpoint.time
        self.old_lat = self.oldpoint.lat
        self.old_lon = self.oldpoint.lon
        self.dr_time = datetime.now(timezone.utc)
        self.timespan = self.dr_time - self.old_time
        self.sog = 0
        self.cog = 0
        self.distancetravelled = 0
        self.drpoint = None
        self.dateTimeEdit_old.setDateTime(QDateTime.fromString(self.old_time.isoformat(), Qt.ISODate))
        self.dateTimeEdit_dr.setDateTime(QDateTime.fromString(self.dr_time.isoformat(), Qt.ISODate))
        self.spinBox_lat_deg_old.setValue(math.trunc(self.old_lat))
        self.doubleSpinBox_lat_min_old.setValue((self.old_lat - math.trunc(self.old_lat)) * 60)
        self.comboBox_ns_old.addItems(["N", "S"])
        self.comboBox_ns_old.setCurrentIndex(0 if self.old_lat >= 0 else 1)
        self.spinBox_lon_deg_old.setValue(math.trunc(self.old_lon))
        self.doubleSpinBox_lon_min_old.setValue((self.old_lon - math.trunc(self.old_lon)) * 60)
        self.comboBox_we_old.addItems(["E", "W"])
        self.comboBox_we_old.setCurrentIndex(0 if self.old_lon >= 0 else 1)
        self.comboBox_ns_dr.addItems(["N", "S"])
        self.comboBox_we_dr.addItems(["E", "W"])
        self.scog_t_changed()

        self.dateTimeEdit_dr.dateTimeChanged.connect(self.scog_t_changed)
        self.dateTimeEdit_old.dateTimeChanged.connect(self.scog_t_changed)
        self.doubleSpinBox_sog.valueChanged.connect(self.scog_t_changed)
        self.spinBox_cog.valueChanged.connect(self.scog_t_changed)
        self.doubleSpinBox_log.valueChanged.connect(self.distance_changed)

        self.spinBox_lat_deg_dr.valueChanged.connect(self.update_rev)
        self.doubleSpinBox_lat_min_dr.valueChanged.connect(self.update_rev)
        self.comboBox_ns_dr.currentIndexChanged.connect(self.update_rev)
        self.spinBox_lon_deg_dr.valueChanged.connect(self.update_rev)
        self.doubleSpinBox_lon_min_dr.valueChanged.connect(self.update_rev)
        self.comboBox_we_dr.currentIndexChanged.connect(self.update_rev)

        self.spinBox_lat_deg_old.valueChanged.connect(self.update_rev)
        self.doubleSpinBox_lat_min_old.valueChanged.connect(self.update_rev)
        self.comboBox_ns_old.currentIndexChanged.connect(self.update_rev)
        self.spinBox_lon_deg_old.valueChanged.connect(self.update_rev)
        self.doubleSpinBox_lon_min_old.valueChanged.connect(self.update_rev)
        self.comboBox_we_old.currentIndexChanged.connect(self.update_rev)

    def get_entry(self):

        if self.drpoint:
            entry = {}
            entry["point"] = self.drpoint
            entry["sog"] = self.sog
            entry["cog"] = self.cog
            return entry
        else:
            return None

        

    def scog_t_changed(self):
        """calulate the dead reconing position from old position, SOG and COG"""
        self.dr_time = datetime.fromisoformat(self.dateTimeEdit_dr.dateTime().toString(format= Qt.ISODate))
        self.old_time = datetime.fromisoformat(self.dateTimeEdit_old.dateTime().toString(format= Qt.ISODate))
        self.sog = self.doubleSpinBox_sog.value()
        self.cog = self.spinBox_cog.value()
        self.timespan = self.dr_time - self.old_time
        self.distancetravelled = self.sog * self.timespan.total_seconds() / 3600
        #self.drpos = dr_pos(self.sog, self.cog, self.old_time, self.dr_time, self.old_lat, self.old_lon)
        self.drpos = self.geod.Direct(self.old_lat, self.old_lon, self.cog, self.distancetravelled * 1852)
        self.drpoint = Point4d(self.dr_time, self.drpos["lat2"], self.drpos["lon2"])
        
        self.spinBox_delta_h.blockSignals(True)
        self.spinBox_delta_min.blockSignals(True)
        self.doubleSpinBox_log.blockSignals(True)
        self.spinBox_lat_deg_dr.blockSignals(True)
        self.doubleSpinBox_lat_min_dr.blockSignals(True)
        self.comboBox_ns_dr.blockSignals(True)
        self.spinBox_lon_deg_dr.blockSignals(True)
        self.doubleSpinBox_lon_min_dr.blockSignals(True)
        self.comboBox_we_dr.blockSignals(True)

        self.spinBox_delta_h.setValue(math.trunc(self.timespan.total_seconds() / 3600))
        self.spinBox_delta_min.setValue(self.timespan.total_seconds() % 3600 / 60)
        self.doubleSpinBox_log.setValue(self.distancetravelled)
        self.spinBox_lat_deg_dr.setValue(math.trunc(abs(self.drpos["lat2"])))
        self.doubleSpinBox_lat_min_dr.setValue((abs(self.drpos["lat2"]) - math.trunc(abs(self.drpos["lat2"]))) * 60)
        self.comboBox_ns_dr.setCurrentIndex(0 if self.drpos["lat2"] >= 0 else 1)
        self.spinBox_lon_deg_dr.setValue(math.trunc(abs(self.drpos["lon2"])))
        self.doubleSpinBox_lon_min_dr.setValue((abs(self.drpos["lon2"]) - math.trunc(abs(self.drpos["lon2"]))) * 60)
        self.comboBox_we_dr.setCurrentIndex(0 if self.drpos["lon2"] >= 0 else 1)

        self.spinBox_delta_h.blockSignals(False)
        self.spinBox_delta_min.blockSignals(False)
        self.doubleSpinBox_log.blockSignals(False)
        self.spinBox_lat_deg_dr.blockSignals(False)
        self.doubleSpinBox_lat_min_dr.blockSignals(False)
        self.comboBox_ns_dr.blockSignals(False)
        self.spinBox_lon_deg_dr.blockSignals(False)
        self.doubleSpinBox_lon_min_dr.blockSignals(False)
        self.comboBox_we_dr.blockSignals(False)

    def distance_changed(self):
        """calulate the dead reconing position from old position and distance travelled"""
        self.dr_time = datetime.fromisoformat(self.dateTimeEdit_dr.dateTime().toString(format= Qt.ISODate))
        self.old_time = datetime.fromisoformat(self.dateTimeEdit_old.dateTime().toString(format= Qt.ISODate))
        self.cog = self.spinBox_cog.value()
        self.old_lat = self.spinBox_lat_deg_old.value() + self.doubleSpinBox_lat_min_old.value() / 60
        self.old_lat = self.old_lat if self.comboBox_ns_old.currentIndex() == 0 else -self.old_lat
        self.old_lon = self.spinBox_lon_deg_old.value() + self.doubleSpinBox_lon_min_old.value() / 60
        self.old_lon = self.old_lon if self.comboBox_we_old.currentIndex() == 0 else -self.old_lon
        self.distancetravelled = self.doubleSpinBox_log.value()
        
        self.timespan = self.dr_time - self.old_time
        self.sog = self.distancetravelled / self.timespan.total_seconds() * 3600
        # self.drpos = dr_pos(self.sog, self.cog, self.old_time, self.dr_time, self.old_lat, self.old_lon)
        self.drpos = self.geod.Direct(self.old_lat, self.old_lon, self.cog, self.distancetravelled * 1852)
        self.drpoint = Point4d(self.dr_time, self.drpos["lat2"], self.drpos["lon2"])
        #print(str(self.drpoint))

        self.spinBox_delta_h.blockSignals(True)
        self.spinBox_delta_min.blockSignals(True)
        self.doubleSpinBox_sog.blockSignals(True)
        self.spinBox_lat_deg_dr.blockSignals(True)
        self.doubleSpinBox_lat_min_dr.blockSignals(True)
        self.comboBox_ns_dr.blockSignals(True)
        self.spinBox_lon_deg_dr.blockSignals(True)
        self.doubleSpinBox_lon_min_dr.blockSignals(True)
        self.comboBox_we_dr.blockSignals(True)

        self.spinBox_delta_h.setValue(math.trunc(self.timespan.total_seconds() / 3600))
        self.spinBox_delta_min.setValue(self.timespan.total_seconds() % 3600 / 60)
        self.doubleSpinBox_sog.setValue(self.sog)
        self.spinBox_lat_deg_dr.setValue(math.trunc(abs(self.drpos["lat2"])))
        self.doubleSpinBox_lat_min_dr.setValue((abs(self.drpos["lat2"]) - math.trunc(abs(self.drpos["lat2"]))) * 60)
        self.comboBox_ns_dr.setCurrentIndex(0 if self.drpos["lat2"] >= 0 else 1)
        self.spinBox_lon_deg_dr.setValue(math.trunc(abs(self.drpos["lon2"])))
        self.doubleSpinBox_lon_min_dr.setValue((abs(self.drpos["lon2"]) - math.trunc(abs(self.drpos["lon2"]))) * 60)
        self.comboBox_we_dr.setCurrentIndex(0 if self.drpos["lon2"] >= 0 else 1)

        self.spinBox_delta_h.blockSignals(False)
        self.spinBox_delta_min.blockSignals(False)
        self.doubleSpinBox_sog.blockSignals(False)
        self.spinBox_lat_deg_dr.blockSignals(False)
        self.doubleSpinBox_lat_min_dr.blockSignals(False)
        self.comboBox_ns_dr.blockSignals(False)
        self.spinBox_lon_deg_dr.blockSignals(False)

    def update_rev(self):
        """calulate the time span, distance travelled, SOG and COG from two points"""
        self.old_time = datetime.fromisoformat(self.dateTimeEdit_old.dateTime().toString(format= Qt.ISODate))
        self.old_lat = self.spinBox_lat_deg_old.value() + self.doubleSpinBox_lat_min_old.value() / 60
        self.old_lat = self.old_lat if self.comboBox_ns_old.currentIndex() == 0 else -self.old_lat
        self.old_lon = self.spinBox_lon_deg_old.value() + self.doubleSpinBox_lon_min_old.value() / 60
        self.old_lon = self.old_lon if self.comboBox_we_old.currentIndex() == 0 else -self.old_lon
        self.oldpoint = Point4d(self.old_time, self.old_lat, self.old_lon)

        self.dr_time = datetime.fromisoformat(self.dateTimeEdit_dr.dateTime().toString(format= Qt.ISODate))
        dr_lat = self.spinBox_lat_deg_dr.value() + self.doubleSpinBox_lat_min_dr.value() / 60
        dr_lat = dr_lat if self.comboBox_ns_dr.currentIndex() == 0 else -dr_lat
        dr_lon = self.spinBox_lon_deg_dr.value() + self.doubleSpinBox_lon_min_dr.value() / 60
        dr_lon = dr_lon if self.comboBox_we_dr.currentIndex() == 0 else -dr_lon        
        self.drpoint = Point4d(self.dr_time, dr_lat, dr_lon)

        self.timespan = self.dr_time - self.old_time
        self.distancetravelled = (self.oldpoint - self.drpoint)[0]/1852
        self.sog = self.distancetravelled / self.timespan.total_seconds() * 3600
        self.cog = (self.oldpoint - self.drpoint)[2]

        self.spinBox_delta_h.blockSignals(True)
        self.spinBox_delta_min.blockSignals(True)
        self.doubleSpinBox_log.blockSignals(True)
        self.spinBox_cog.blockSignals(True)
        self.doubleSpinBox_sog.blockSignals(True)

        self.spinBox_delta_h.setValue(math.trunc(self.timespan.total_seconds() / 3600))
        self.spinBox_delta_min.setValue(self.timespan.total_seconds() % 3600 / 60)
        self.doubleSpinBox_log.setValue(self.distancetravelled)
        self.spinBox_cog.setValue(self.cog)
        self.doubleSpinBox_sog.setValue(self.sog)

        self.spinBox_delta_h.blockSignals(False)
        self.spinBox_delta_min.blockSignals(False)
        self.doubleSpinBox_log.blockSignals(False)
        self.spinBox_cog.blockSignals(False)
        self.doubleSpinBox_sog.blockSignals(False)
