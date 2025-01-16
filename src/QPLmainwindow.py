from multiprocessing import Value
import os
import sys
import yaml
import orjson
import math
import copy
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt, QAbstractTableModel
from datetime import datetime, timezone
from point4D import Point4d

from ui.QPLmainwindow_ui import Ui_MainWindow
from ui.Dialog_edit_ui import Ui_EditDialog
from ui.dialog_choice_ui import Ui_DialogChoice
from ui.Dialog_settings_ui import Ui_DialogSettings
import SKconnect
import iofunctions




# Variables:
conf_file = os.path.dirname(os.path.realpath(__file__)) + "/" + "data/conf.json"

currentfile = "/Users/enno/Documents/dev/QPlogbook/src/data/qptestlog.json"

keys_to_head = {
        "log": "Log\n(nm)",
        "enginehours": "Engine\n(h)",
        "cog": "COG",
        "sog": "SOG\n(kts)",
        "stw": "STW",
        "heading": "Heading",
        "airpressure": "Baro \n(hPa)",
        "airtemperature": "Airtemp \n(°C)",
        "twd": "TWD",
        "tws": "TWS\n(kts)",
        "humidity": "Humidity\n(%)",
        "text": "text",
        "fixtype": "Fix",
        "hdop": "HDOP\n(m)",
        "visibility": "Vis.",
        "cloudcover": "Cloud\n(8th)",
        "seastate": "Sea",
        "crewNames": "Crew",
}   

with open(conf_file, "r") as conffile:
        conf = orjson.loads(conffile.read())

def toheaders(conf):
    headers = ["Time", "Position"]
    for key in conf["showkeys"]:
        headers.append(keys_to_head[key])
    return headers

def h_to_key(head):
    head_to_key = {v: k for k, v in keys_to_head.items()}

# testvariables:

QPlog = []
QPlog = iofunctions.getQPlog("/Users/enno/Documents/dev/QPlogbook/src/data/qptestlog.json")  
# QPlog =importandclean.cleanup(QPlog)     


# Qt Mainwindow and Model:

class QPlogModel(QAbstractTableModel):
    """the data model for use with QtableView"""
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers
        self.head_to_key = {v: k for k, v in keys_to_head.items()}

    def data(self, index, role):
        column = index.column()
        

        column_key = dictkey = self._headers[column]
        if dictkey == "Time" or dictkey == "Position":
            dictkey = "point"
        else:
            dictkey = self.head_to_key[dictkey]

        if role == Qt.DisplayRole:
            try:
                value = self._data[index.row()][dictkey]
            except KeyError:
                return ""

            # if isinstance(value, datetime):
            #     return value.strftime("%H:%M")

            if column_key == "Time":
                logtime = value.time
                return logtime.strftime("%H:%M")
            
            elif column_key == "Position":             
                return f"{value.getDMpos()[0]} \n {value.getDMpos()[1]}"
            
            elif isinstance(value, list):
                s = ""
                for i in value:
                    s += (i + ", ")
                return s
            else:
                return value
        
        if role == Qt.FontRole: 
            font = QtGui.QFont()
            font.setPointSize(10)           
            if column_key == "Position":
                return font
            font.setPointSize(12)
            return font
        
        if role == Qt.TextAlignmentRole:
            if column_key == "Position":
                return Qt.AlignVCenter + Qt.AlignRight


    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                value = self._data[section]["point"].time 
                return value.strftime("%d.%m")   # str(section)
            

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.model = QPlogModel(QPlog, toheaders(conf))
        self.logTableView.setModel(self.model)
        self.logTableView.resizeRowsToContents()
        self.logTableView.resizeColumnsToContents()

        self.actionSave.triggered.connect(self.save_QPlog)
        self.actionOpen.triggered.connect(self.openDialog)
        self.actionAdd.triggered.connect(self.addDialog)
        self.actionPreferences.triggered.connect(self.openSettings)
        self.actionEdit.triggered.connect(self.openEdit)
        self.actionNew_Entry.triggered.connect(self.openNew)
        self.actionAddEntry.triggered.connect(self.addSKentry)
        self.actionDelete_Entry.triggered.connect(self.deleteEntry)
        self.actionSort.triggered.connect(self.sortandclean)


    def openDialog(self):
        """Open a File Dialog to open a new log file replacing the current log"""
        fileName = QFileDialog.getOpenFileName(self, "Open File",
                                                "",
                                                "JSON files (*.json)")
        self.active_folder = os.path.dirname(fileName[0])
        log = iofunctions.getQPlog(fileName[0])
        QPlog.clear()
        QPlog.extend(log)
        self.model.layoutChanged.emit()


    def addDialog(self):
        """Open a File Dialog to add a log file to the current logbook"""
        fileName = QFileDialog.getOpenFileName(self, "Open File",
                                                "",
                                                "JSON files (*.json)")
        self.active_folder = os.path.dirname(fileName[0])
        log = iofunctions.getQPlog(fileName[0])
        QPlog.extend(log)
        self.model.layoutChanged.emit() 





    # def saveasDialog(self):
    #     path = self.active_folder
    #     safeName = QFileDialog.getSaveFileName(self, "Save Log", path, "YAML(*.yml);; JSON(*.json)")
    #     saveLog(safeName)

    def save_QPlog(self):
        """ Save the current log to the active Folder splits the log into monthly files and promps
        the user to save or merge the files"""
        to_save = iofunctions.splitmonthly(QPlog)
        for key in to_save:
            try:
                with open(f"{conf["qplogfolder"]}/{key}.json", "r") as file:
                    #oldlog = iofunctions.deserialize_log(file.read())
                    oldjson = file.read()
                    newjson = iofunctions.serialize_log(to_save[key])
                    if oldjson == newjson:
                        pass
                    else:
                        choice = ChoiceDialog(self, file)
                        choice.exec()
                        if choice.do == "overwrite":
                            with open(f"{conf["qplogfolder"]}/{key}.json", "w") as file:
                                file.write(iofunctions.serialize_log(to_save[key]))
                        elif choice.do == "merge":
                            with open(f"{conf["qplogfolder"]}/{key}.json", "r") as file:
                                oldlog = iofunctions.deserialize_log(file.read())
                            oldlog.extend(to_save[key])
                            oldlog = iofunctions.cleanup(oldlog)
                            with open(f"{conf["qplogfolder"]}/{key}.json", "w") as file:
                                file.write(iofunctions.serialize_log(oldlog))
                        elif choice.do == "discard":
                            pass
                        elif choice.do == "saveas":
                            self.savename = QFileDialog.getSaveFileName(self, "Save Log", conf["qplogfolder"], "JSON(*.json)")
                            with open(self.savename[0], "w") as file:
                                file.write(iofunctions.serialize_log(to_save[key]))
                        elif choice.do == "cancel":
                            pass
                        else:
                            pass
            except FileNotFoundError:
                with open(f"{conf["qplogfolder"]}/{key}.json", "w") as file:
                    file.write(iofunctions.serialize_log(to_save[key]))



    def openEdit(self):
        """Open the Edit dialog with the crrently highlited entry"""
        index = self.logTableView.currentIndex().row()
        entrym = QPlog[index]
        dlg = EditDialog(self, entrym)
        dlg.exec()
        if dlg.entry != {}:
            QPlog[index] = dlg.entry
            self.model.layoutChanged.emit()
        else:
            pass
        del dlg


    def openSettings(self):
        """Open the Settings Dialog"""
        pref_dlg = SettingsDialog(self, conf)
        pref_dlg.exec()
        with open(conf_file, "w") as conffile:
            conffile.write(orjson.dumps(conf, option=orjson.OPT_INDENT_2).decode("utf-8"))
        del pref_dlg
        self.model = QPlogModel(QPlog, toheaders(conf))
        self.logTableView.setModel(self.model)
        self.logTableView.resizeRowsToContents()
        self.logTableView.resizeColumnsToContents()


    def openNew(self):
        """Open the Edit dialog without data to create a new entry"""
        dlg = EditDialog(self, {})
        dlg.exec()
        if dlg.entry != {}:
            QPlog.append(copy.deepcopy(dlg.entry))
            self.model.layoutChanged.emit()
        else:
            pass
        del dlg
    
    def addSKentry(self):
        """Add a new entry to the logbook with the current values from the SignalK server"""
        entry = SKconnect.getSKpath(conf)
        if entry:
            QPlog.append(entry)
            self.model.layoutChanged.emit()
        else:
            pass

    def deleteEntry(self):
        """Delete the currently highlited entry"""
        index = self.logTableView.currentIndex().row()
        del QPlog[index]
        self.model.layoutChanged.emit()

    def sortandclean(self):
        """Sort the logbook and remove duplicates"""
        global QPlog
        log = iofunctions.cleanup(QPlog)
        QPlog.clear()
        QPlog.extend(log)
        self.model.layoutChanged.emit()


# Dialogs:

class ChoiceDialog(Ui_DialogChoice, QtWidgets.QDialog):
    """Dialog class for choosing between saving, merging, discarding and overwriting a log file"""
    def __init__(self, parent=None, file=None):
        super().__init__(parent)
        self.setupUi(self)
        self.file = file
        self.do = ""
        self.label_filename.setText(file.name)
        self.buttonBox.accepted.connect(self.overwrite)
        self.buttonBox.rejected.connect(self.cancel)
        self.mergeButton.clicked.connect(self.merge)
        self.discardButton.clicked.connect(self.discard)
        self.saveasButton.clicked.connect(self.save_as)

    def save_as(self):
        self.do = "saveas"
        self.close()

    def cancel(self):
        self.do = "cancel"
        self.close()

    def overwrite(self):
        self.do = "overwrite"
        self.close()

    def merge(self):
        self.do = "merge"
        self.close()

    def discard(self):
        self.do = "discard"
        self.close()


class EditDialog(Ui_EditDialog, QtWidgets.QDialog):
    """Dialog class for editing a log entry"""
    def __init__(self, parent=None, ent={}):
        super().__init__(parent)
        self.setupUi(self)
        self.entry = ent
        if self.entry != {}:
            self.updatevalues()

        self.buttonBox.accepted.connect(self.applyValues)
        self.buttonBox.rejected.connect(self.cancel_edit)
        self.updateButton.clicked.connect(self.update_from_SK)

        self.delCrewButton.clicked.connect(self.removecrew)
        self.addCrewButton.clicked.connect(self.addcrew)


    def removecrew(self):
        i = self.crewBox.currentRow()
        self.crewBox.takeItem(i)

    def addcrew(self):
        c = self.crewEdit.text()
        if c :
            self.crewBox.addItem(c)
            self.crewEdit.clear()

    def update_from_SK(self):
        """Update the dialog with the current values from the SignalK server"""
        self.entry = SKconnect.getSKpath(conf)
        if self.entry:
            print(self.entry)
            self.updatevalues()
        else:
            pass


    def updatevalues(self):
        """Update the dialog with the values from the current entry"""
        if isinstance(self.entry["point"], Point4d):
            self.dateTimeEdit.setDateTime(self.entry["point"].time)
            self.latEdit.setValue(self.entry["point"].lat)
            self.lonEdit.setValue(self.entry["point"].lon)
            st = self.dateTimeEdit.dateTime()
        else:
            pass
        if "fixtype" in self.entry:
            self.sourceEdit.setText(self.entry["fixtype"])
        if "log" in self.entry:
            self.logEdit.setValue(self.entry["log"])
        if "cog" in self.entry:
            self.cogEdit.setValue(self.entry["cog"])
        if "heading" in self.entry:
            self.headingEdit.setValue(self.entry["heading"])
        if "sog" in self.entry:
            self.sogEdit.setValue(self.entry["sog"])
        if "stw" in self.entry:
            self.stwEdit.setValue(self.entry["stw"])
        if "enginehours" in self.entry:
            self.engineEdit.setValue(self.entry["enginehours"])
        if "tws" in self.entry:
            self.twsEdit.setValue(self.entry["tws"])
        if "twd" in self.entry:
            self.twdEdit.setValue(self.entry["twd"])
        if "airpressure" in self.entry:
            self.pressureEdit.setValue(self.entry["airpressure"])
        if "airtemperature" in self.entry:
            self.airtempSpinBox.setValue(self.entry["airtemperature"])
        if  "seastate" in self.entry:
            self.seastateBox.setCurrentIndex(self.entry["seastate"])
        if "cloudcover" in self.entry:
            self.cloudcoverSpinBox.setValue(self.entry["cloudcover"])
        if "visibility" in self.entry:
            self.visibilityBox.setCurrentIndex(self.entry["visibility"])
        if "crewNames" in self.entry:
            self.crewBox.clear()
            for name in self.entry["crewNames"]:
                self.crewBox.addItem(name)
        if "text" in self.entry:
            self.TextEdit.setPlainText(self.entry["text"])


        
    def applyValues(self):
        """Apply the values from the dialog to the current entry"""
        if self.latEdit.value() == 0 and self.lonEdit.value() == 0:
            self.entry = {}
        time = self.dateTimeEdit.dateTime()
        dt = time.toPython()
        dt = dt.replace(tzinfo = timezone.utc)
        self.entry["point"] = Point4d(dt, self.latEdit.value(), self.lonEdit.value())
        self.entry["fixtype"] = self.sourceEdit.text()
        if self.entry["fixtype"] == "":
            del self.entry["fixtype"]
        self.entry["log"] = self.logEdit.value()
        if self.entry["log"] < 0:
            del self.entry["log"]
        self.entry["cog"] = self.cogEdit.value()
        if self.entry["cog"] < 0:
            del self.entry["cog"]
        self.entry["heading"] = self.headingEdit.value()
        if self.entry["heading"] < 0:
            del self.entry["heading"]
        self.entry["sog"] = self.sogEdit.value()
        if self.entry["sog"] < 0:
            del self.entry["sog"]
        self.entry["stw"] = self.stwEdit.value()
        if self.entry["stw"] < 0:
            del self.entry["stw"]
        self.entry["enginehours"] = self.engineEdit.value()
        if self.entry["enginehours"] < 0:
            del self.entry["enginehours"]
        self.entry["tws"] = self.twsEdit.value()
        if self.entry["tws"] < 0:
            del self.entry["tws"]
        self.entry["twd"] = self.twdEdit.value()
        if self.entry["twd"] < 0:
            del self.entry["twd"]
        self.entry["airpressure"] = self.pressureEdit.value()
        if self.entry["airpressure"] < 870:
            del self.entry["airpressure"]
        self.entry["airtemperature"] = self.airtempSpinBox.value()
        if self.entry["airtemperature"] < -70:
            del self.entry["airtemperature"]
        self.entry["seastate"] = self.seastateBox.currentIndex()
        if self.entry["seastate"] == 0:
            del self.entry["seastate"]
        self.entry["cloudcover"] = self.cloudcoverSpinBox.value()
        if self.entry["cloudcover"] < 0:
            del self.entry["cloudcover"]
        self.entry["visibility"] = self.visibilityBox.currentIndex()
        if self.entry["visibility"] == 0:
            del self.entry["visibility"]
        self.entry["crewNames"] = []
        for i in range(self.crewBox.count()):
            self.entry["crewNames"].append(self.crewBox.item(i).text())
        self.entry["text"] = self.TextEdit.toPlainText()
        if self.entry["text"] == "":
            del self.entry["text"]

    def cancel_edit(self):
        self.entry = {}
        self.close()


class SettingsDialog(Ui_DialogSettings, QtWidgets.QDialog):
    def __init__(self, parent=None, conf={}):
        super().__init__(parent)
        self.setupUi(self)
        self.conf = conf
        self.updatevalues()
        self.buttonBox.accepted.connect(self.applyValues)
        self.buttonBox.rejected.connect(self.cancel_edit)
        self.qplPathButton.clicked.connect(self.qplog_dir)
        self.sklPathButton.clicked.connect(self.sklog_dir)


    def qplog_dir(self):
        print("qplog")
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.lineEdit_qplog_dir.setText(path)

    def sklog_dir(self):
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.lineEdit_sklog_dir.setText(path)

    def updatevalues(self):
        # update the values in the Settings Dialog according to the current configuration file
        self.lineEdit_name.setText(self.conf["boat"]["name"])
        self.lineEdit_call_sign.setText(self.conf["boat"]["callsign"])
        self.spinBox_mmsi.setValue(self.conf["boat"]["mmsi"])
        self.doubleSpinBox_hight.setValue(self.conf["boat"]["hight"])
        self.doubleSpinBox_beam.setValue(self.conf["boat"]["beam"])
        self.doubleSpinBox_loa.setValue(self.conf["boat"]["loa"])
        self.doubleSpinBox_draft.setValue(self.conf["boat"]["draft"])
        self.doubleSpinBox_update_interv.setValue(self.conf["loginterv"])
        self.doubleSpinBox_track_interv.setValue(self.conf["trackinterv"])
        self.doubleSpinBox_timeout.setValue(self.conf["servertimeout"])
        self.lineEdit_qplog_dir.setText(self.conf["qplogfolder"])
        self.lineEdit_sklog_dir.setText(self.conf["sklogfolder"])
        self.lineEdit_server.setText(self.conf["skserver"])

        self.checkBox_autoentry.setChecked(self.conf["enableauto"])
        self.checkBox_tracking.setChecked(self.conf["enabletracking"])

        self.lineEdit_datetime.setText(self.conf["path"]["datetime"])
        self.lineEdit_position.setText(self.conf["path"]["position"])
        self.lineEdit_log.setText(self.conf["path"]["log"])
        self.lineEdit_engine.setText(self.conf["path"]["enginehours"])
        self.lineEdit_sog.setText(self.conf["path"]["sog"])
        self.lineEdit_cog.setText(self.conf["path"]["cog"])
        self.lineEdit_heading.setText(self.conf["path"]["heading"])
        self.lineEdit_stw.setText(self.conf["path"]["stw"])
        self.lineEdit_tws.setText(self.conf["path"]["tws"])
        self.lineEdit_twd.setText(self.conf["path"]["twd"])
        self.lineEdit_temp.setText(self.conf["path"]["airtemperature"])
        self.lineEdit_airpressure.setText(self.conf["path"]["airpressure"])
        self.lineEdit_humidity.setText(self.conf["path"]["humidity"])
        self.lineEdit_hdop.setText(self.conf["path"]["hdop"])
        self.lineEdit_fix.setText(self.conf["path"]["fixtype"])

        self.checkBox_log.setChecked(True) if "log" in self.conf["activekeys"] else self.checkBox_log.setChecked(False)
        self.checkBox_engine.setChecked(True) if "enginehours" in self.conf["activekeys"] else self.checkBox_engine.setChecked(False)
        self.checkBox_sog.setChecked(True) if "sog" in self.conf["activekeys"] else self.checkBox_sog.setChecked(False)
        self.checkBox_cog.setChecked(True) if "cog" in self.conf["activekeys"] else self.checkBox_cog.setChecked(False)
        self.checkBox_heading.setChecked(True) if "heading" in self.conf["activekeys"] else self.checkBox_heading.setChecked(False)
        self.checkBox_stw.setChecked(True) if "stw" in self.conf["activekeys"] else self.checkBox_stw.setChecked(False)
        self.checkBox_tws.setChecked(True) if "tws" in self.conf["activekeys"] else self.checkBox_tws.setChecked(False)
        self.checkBox_twd.setChecked(True) if "twd" in self.conf["activekeys"] else self.checkBox_twd.setChecked(False)
        self.checkBox_temp.setChecked(True) if "airtemperature" in self.conf["activekeys"] else self.checkBox_temp.setChecked(False)
        self.checkBox_airpressure.setChecked(True) if "airpressure" in self.conf["activekeys"] else self.checkBox_airpressure.setChecked(False)
        self.checkBox_humidity.setChecked(True) if "humidity" in self.conf["activekeys"] else self.checkBox_humidity.setChecked(False)
        self.checkBox_hdop.setChecked(True) if "hdop" in self.conf["activekeys"] else self.checkBox_hdop.setChecked(False)
        self.checkBox_fix.setChecked(True) if "fixtype" in self.conf["activekeys"] else self.checkBox_fix.setChecked(False)

        self.checkBox_s_log.setChecked(True) if "log" in self.conf["showkeys"] else self.checkBox_s_log.setChecked(False)
        self.checkBox_s_engine.setChecked(True) if "enginehours" in self.conf["showkeys"] else self.checkBox_s_engine.setChecked(False)
        self.checkBox_s_sog.setChecked(True) if "sog" in self.conf["showkeys"] else self.checkBox_s_sog.setChecked(False)
        self.checkBox_s_cog.setChecked(True) if "cog" in self.conf["showkeys"] else self.checkBox_s_cog.setChecked(False)
        self.checkBox_s_heading.setChecked(True) if "heading" in self.conf["showkeys"] else self.checkBox_s_heading.setChecked(False)
        self.checkBox_s_stw.setChecked(True) if "stw" in self.conf["showkeys"] else self.checkBox_s_stw.setChecked(False)
        self.checkBox_s_tws.setChecked(True) if "tws" in self.conf["showkeys"] else self.checkBox_s_tws.setChecked(False)
        self.checkBox_s_twd.setChecked(True) if "twd" in self.conf["showkeys"] else self.checkBox_s_twd.setChecked(False)
        self.checkBox_s_temp.setChecked(True) if "airtemperature" in self.conf["showkeys"] else self.checkBox_s_temp.setChecked(False)
        self.checkBox_s_airpressure.setChecked(True) if "airpressure" in self.conf["showkeys"] else self.checkBox_s_airpressure.setChecked(False)
        self.checkBox_s_humidity.setChecked(True) if "humidity" in self.conf["showkeys"] else self.checkBox_s_humidity.setChecked(False)
        self.checkBox_s_hdop.setChecked(True) if "hdop" in self.conf["showkeys"] else self.checkBox_s_hdop.setChecked(False)
        self.checkBox_s_fix.setChecked(True) if "fixtype" in self.conf["showkeys"] else self.checkBox_s_fix.setChecked(False)
        self.checkBox_s_seastate.setChecked(True) if "seastate" in self.conf["showkeys"] else self.checkBox_s_seastate.setChecked(False)
        self.checkBox_s_cloud.setChecked(True) if "cloudcover" in self.conf["showkeys"] else self.checkBox_s_cloud.setChecked(False)
        self.checkBox_s_visibility.setChecked(True) if "visibility" in self.conf["showkeys"] else self.checkBox_s_visibility.setChecked(False)
        self.checkBox_s_crew.setChecked(True) if "crewNames" in self.conf["showkeys"] else self.checkBox_s_crew.setChecked(False)
        self.checkBox_s_text.setChecked(True) if "text" in self.conf["showkeys"] else self.checkBox_s_text.setChecked(False)



    def applyValues(self):
        self.conf["boat"]["name"] = self.lineEdit_name.text()
        self.conf["boat"]["callsign"] = self.lineEdit_call_sign.text()
        self.conf["boat"]["mmsi"] = self.spinBox_mmsi.value()
        self.conf["boat"]["hight"] = self.doubleSpinBox_hight.value()
        self.conf["boat"]["beam"] = self.doubleSpinBox_beam.value()
        self.conf["boat"]["loa"] = self.doubleSpinBox_loa.value()
        self.conf["boat"]["draft"] = self.doubleSpinBox_draft.value()
        self.conf["loginterv"] = self.doubleSpinBox_update_interv.value()
        self.conf["trackinterv"] = self.doubleSpinBox_track_interv.value()
        self.conf["servertimeout"] = self.doubleSpinBox_timeout.value()
        self.conf["qplogfolder"] = self.lineEdit_qplog_dir.text()
        self.conf["sklogfolder"] = self.lineEdit_sklog_dir.text()
        self.conf["skserver"] = self.lineEdit_server.text()

        self.conf["enableauto"] = self.checkBox_autoentry.isChecked()
        self.conf["enabletracking"] = self.checkBox_tracking.isChecked()

        self.conf["path"]["datetime"] = self.lineEdit_datetime.text()
        self.conf["path"]["position"] = self.lineEdit_position.text()
        self.conf["path"]["log"] = self.lineEdit_log.text()
        self.conf["path"]["enginehours"] = self.lineEdit_engine.text()
        self.conf["path"]["sog"] = self.lineEdit_sog.text()
        self.conf["path"]["cog"] = self.lineEdit_cog.text()
        self.conf["path"]["heading"] = self.lineEdit_heading.text()
        self.conf["path"]["stw"] = self.lineEdit_stw.text()
        self.conf["path"]["tws"] = self.lineEdit_tws.text()
        self.conf["path"]["twd"] = self.lineEdit_twd.text()
        self.conf["path"]["airtemperature"] = self.lineEdit_temp.text()
        self.conf["path"]["airpressure"] = self.lineEdit_airpressure.text()
        self.conf["path"]["humidity"] = self.lineEdit_humidity.text()
        self.conf["path"]["hdop"] = self.lineEdit_hdop.text()
        self.conf["path"]["fixtype"] = self.lineEdit_fix.text()

        self.conf["activekeys"] = ["Time", "Position"]
        if self.checkBox_log.isChecked(): self.conf["activekeys"].append("log")
        if self.checkBox_engine.isChecked(): self.conf["activekeys"].append("enginehours")
        if self.checkBox_sog.isChecked(): self.conf["activekeys"].append("sog")
        if self.checkBox_cog.isChecked(): self.conf["activekeys"].append("cog")
        if self.checkBox_heading.isChecked(): self.conf["activekeys"].append("heading")
        if self.checkBox_stw.isChecked(): self.conf["activekeys"].append("stw")
        if self.checkBox_tws.isChecked(): self.conf["activekeys"].append("tws")
        if self.checkBox_twd.isChecked(): self.conf["activekeys"].append("twd")
        if self.checkBox_temp.isChecked(): self.conf["activekeys"].append("airtemperature")
        if self.checkBox_airpressure.isChecked(): self.conf["activekeys"].append("airpressure")
        if self.checkBox_humidity.isChecked(): self.conf["activekeys"].append("humidity")
        if self.checkBox_hdop.isChecked(): self.conf["activekeys"].append("hdop")
        if self.checkBox_fix.isChecked(): self.conf["activekeys"].append("fixtype")

        self.conf["showkeys"] = []
        if self.checkBox_s_log.isChecked(): self.conf["showkeys"].append("log")
        if self.checkBox_s_engine.isChecked(): self.conf["showkeys"].append("enginehours")
        if self.checkBox_s_sog.isChecked(): self.conf["showkeys"].append("sog")
        if self.checkBox_s_cog.isChecked(): self.conf["showkeys"].append("cog")
        if self.checkBox_s_heading.isChecked(): self.conf["showkeys"].append("heading")
        if self.checkBox_s_stw.isChecked(): self.conf["showkeys"].append("stw")
        if self.checkBox_s_tws.isChecked(): self.conf["showkeys"].append("tws")
        if self.checkBox_s_twd.isChecked(): self.conf["showkeys"].append("twd")
        if self.checkBox_s_temp.isChecked(): self.conf["showkeys"].append("airtemperature")
        if self.checkBox_s_airpressure.isChecked(): self.conf["showkeys"].append("airpressure")
        if self.checkBox_s_humidity.isChecked(): self.conf["showkeys"].append("humidity")
        if self.checkBox_s_hdop.isChecked(): self.conf["showkeys"].append("hdop")
        if self.checkBox_s_fix.isChecked(): self.conf["showkeys"].append("fixtype")
        if self.checkBox_s_seastate.isChecked(): self.conf["showkeys"].append("seastate")
        if self.checkBox_s_cloud.isChecked(): self.conf["showkeys"].append("cloudcover")
        if self.checkBox_s_visibility.isChecked(): self.conf["showkeys"].append("visibility")
        if self.checkBox_s_crew.isChecked(): self.conf["showkeys"].append("crewNames")
        if self.checkBox_s_text.isChecked(): self.conf["showkeys"].append("text")
        self.close()

        
        

    def cancel_edit(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()