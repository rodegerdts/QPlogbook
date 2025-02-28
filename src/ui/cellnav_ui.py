# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cellnav.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateTimeEdit,
    QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_CelNavigation(object):
    def setupUi(self, CelNavigation):
        if not CelNavigation.objectName():
            CelNavigation.setObjectName(u"CelNavigation")
        CelNavigation.resize(528, 520)
        self.verticalLayout = QVBoxLayout(CelNavigation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(CelNavigation)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox_sog = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_sog.setObjectName(u"doubleSpinBox_sog")
        self.doubleSpinBox_sog.setDecimals(1)
        self.doubleSpinBox_sog.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_sog)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.spinBox_cog = QSpinBox(self.groupBox_2)
        self.spinBox_cog.setObjectName(u"spinBox_cog")
        self.spinBox_cog.setMaximum(359)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_cog)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.doubleSpinBox_temperature = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_temperature.setObjectName(u"doubleSpinBox_temperature")
        self.doubleSpinBox_temperature.setDecimals(1)
        self.doubleSpinBox_temperature.setMinimum(-100.000000000000000)
        self.doubleSpinBox_temperature.setSingleStep(0.100000000000000)
        self.doubleSpinBox_temperature.setValue(25.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_temperature)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.doubleSpinBox_pressure = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_pressure.setObjectName(u"doubleSpinBox_pressure")
        self.doubleSpinBox_pressure.setDecimals(1)
        self.doubleSpinBox_pressure.setMaximum(1080.000000000000000)
        self.doubleSpinBox_pressure.setValue(1013.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_pressure)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.doubleSpinBox_log = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_log.setObjectName(u"doubleSpinBox_log")
        self.doubleSpinBox_log.setDecimals(1)
        self.doubleSpinBox_log.setMaximum(1000000.000000000000000)
        self.doubleSpinBox_log.setSingleStep(0.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBox_log)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(7, QFormLayout.FieldRole, self.verticalSpacer)

        self.doubleSpinBox_indexerror = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_indexerror.setObjectName(u"doubleSpinBox_indexerror")
        self.doubleSpinBox_indexerror.setDecimals(1)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBox_indexerror)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.doubleSpinBox_hoe = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_hoe.setObjectName(u"doubleSpinBox_hoe")
        self.doubleSpinBox_hoe.setDecimals(1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.doubleSpinBox_hoe)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(CelNavigation)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.button_calculateDR = QPushButton(self.groupBox)
        self.button_calculateDR.setObjectName(u"button_calculateDR")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.button_calculateDR)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.dateTimeEdit_dr = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_dr.setObjectName(u"dateTimeEdit_dr")
        self.dateTimeEdit_dr.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateTimeEdit_dr.setTimeSpec(Qt.TimeSpec.UTC)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.dateTimeEdit_dr)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox_lat_deg = QSpinBox(self.groupBox)
        self.spinBox_lat_deg.setObjectName(u"spinBox_lat_deg")
        self.spinBox_lat_deg.setMinimumSize(QSize(40, 0))
        self.spinBox_lat_deg.setMaximumSize(QSize(1600, 16777215))
        self.spinBox_lat_deg.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lat_deg.setMinimum(-90)
        self.spinBox_lat_deg.setMaximum(90)

        self.horizontalLayout.addWidget(self.spinBox_lat_deg)

        self.doubleSpinBox_lat_min = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_lat_min.setObjectName(u"doubleSpinBox_lat_min")
        self.doubleSpinBox_lat_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lat_min.setDecimals(1)
        self.doubleSpinBox_lat_min.setMaximum(59.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_lat_min)

        self.comboBox_ns = QComboBox(self.groupBox)
        self.comboBox_ns.setObjectName(u"comboBox_ns")
        self.comboBox_ns.setMaximumSize(QSize(60, 16777215))
        self.comboBox_ns.setMaxVisibleItems(3)

        self.horizontalLayout.addWidget(self.comboBox_ns)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox_lon_deg = QSpinBox(self.groupBox)
        self.spinBox_lon_deg.setObjectName(u"spinBox_lon_deg")
        self.spinBox_lon_deg.setMinimumSize(QSize(40, 0))
        self.spinBox_lon_deg.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spinBox_lon_deg.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lon_deg.setMinimum(-180)
        self.spinBox_lon_deg.setMaximum(180)

        self.horizontalLayout_2.addWidget(self.spinBox_lon_deg)

        self.doubleSpinBox_lon_min = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_lon_min.setObjectName(u"doubleSpinBox_lon_min")
        self.doubleSpinBox_lon_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lon_min.setDecimals(1)
        self.doubleSpinBox_lon_min.setMaximum(59.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_lon_min)

        self.comboBox_we = QComboBox(self.groupBox)
        self.comboBox_we.setObjectName(u"comboBox_we")
        self.comboBox_we.setMaximumSize(QSize(60, 16777215))
        self.comboBox_we.setMaxVisibleItems(2)

        self.horizontalLayout_2.addWidget(self.comboBox_we)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(CelNavigation)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_fix_lat = QLineEdit(self.groupBox_3)
        self.lineEdit_fix_lat.setObjectName(u"lineEdit_fix_lat")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_fix_lat)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_fix_lon = QLineEdit(self.groupBox_3)
        self.lineEdit_fix_lon.setObjectName(u"lineEdit_fix_lon")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_fix_lon)

        self.button_calculateFix = QPushButton(self.groupBox_3)
        self.button_calculateFix.setObjectName(u"button_calculateFix")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.button_calculateFix)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.label_time_of_fix = QLabel(self.groupBox_3)
        self.label_time_of_fix.setObjectName(u"label_time_of_fix")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.label_time_of_fix)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_14)


        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(CelNavigation)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView_sights = QListView(self.groupBox_4)
        self.listView_sights.setObjectName(u"listView_sights")

        self.verticalLayout_2.addWidget(self.listView_sights)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_new = QPushButton(self.groupBox_4)
        self.button_new.setObjectName(u"button_new")

        self.horizontalLayout_3.addWidget(self.button_new)

        self.button_edit = QPushButton(self.groupBox_4)
        self.button_edit.setObjectName(u"button_edit")

        self.horizontalLayout_3.addWidget(self.button_edit)

        self.button_delete = QPushButton(self.groupBox_4)
        self.button_delete.setObjectName(u"button_delete")

        self.horizontalLayout_3.addWidget(self.button_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.button_open = QPushButton(CelNavigation)
        self.button_open.setObjectName(u"button_open")

        self.horizontalLayout_4.addWidget(self.button_open)

        self.button_save = QPushButton(CelNavigation)
        self.button_save.setObjectName(u"button_save")

        self.horizontalLayout_4.addWidget(self.button_save)

        self.button_close = QPushButton(CelNavigation)
        self.button_close.setObjectName(u"button_close")

        self.horizontalLayout_4.addWidget(self.button_close)

        self.button_toLog = QPushButton(CelNavigation)
        self.button_toLog.setObjectName(u"button_toLog")

        self.horizontalLayout_4.addWidget(self.button_toLog)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(CelNavigation)

        self.comboBox_ns.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(CelNavigation)
    # setupUi

    def retranslateUi(self, CelNavigation):
        CelNavigation.setWindowTitle(QCoreApplication.translate("CelNavigation", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CelNavigation", u"Parmeters:", None))
        self.label_8.setText(QCoreApplication.translate("CelNavigation", u"SOG", None))
        self.doubleSpinBox_sog.setSuffix(QCoreApplication.translate("CelNavigation", u" kn", None))
        self.label_7.setText(QCoreApplication.translate("CelNavigation", u"COG", None))
        self.spinBox_cog.setSuffix(QCoreApplication.translate("CelNavigation", u"\u02da", None))
        self.label_10.setText(QCoreApplication.translate("CelNavigation", u"Temperaure", None))
        self.doubleSpinBox_temperature.setSuffix(QCoreApplication.translate("CelNavigation", u"\u02daC", None))
        self.label_9.setText(QCoreApplication.translate("CelNavigation", u"Pressure", None))
        self.doubleSpinBox_pressure.setSuffix(QCoreApplication.translate("CelNavigation", u" hPa", None))
        self.label_3.setText(QCoreApplication.translate("CelNavigation", u"Log", None))
        self.doubleSpinBox_log.setSuffix(QCoreApplication.translate("CelNavigation", u" nm", None))
        self.doubleSpinBox_indexerror.setSuffix(QCoreApplication.translate("CelNavigation", u"\u00b4", None))
        self.label_4.setText(QCoreApplication.translate("CelNavigation", u"Index Error", None))
        self.doubleSpinBox_hoe.setSuffix(QCoreApplication.translate("CelNavigation", u" m", None))
        self.label_5.setText(QCoreApplication.translate("CelNavigation", u"Hight of Eye", None))
        self.groupBox.setTitle(QCoreApplication.translate("CelNavigation", u"DR position", None))
        self.label.setText(QCoreApplication.translate("CelNavigation", u"Latitude:", None))
        self.label_2.setText(QCoreApplication.translate("CelNavigation", u"Longitude:", None))
        self.button_calculateDR.setText(QCoreApplication.translate("CelNavigation", u"calculateDR", None))
        self.label_11.setText(QCoreApplication.translate("CelNavigation", u"Time", None))
        self.dateTimeEdit_dr.setDisplayFormat(QCoreApplication.translate("CelNavigation", u"dd/MM/yyyy HH:mm:ss", None))
        self.spinBox_lat_deg.setSuffix(QCoreApplication.translate("CelNavigation", u"\u02da", None))
        self.doubleSpinBox_lat_min.setSuffix(QCoreApplication.translate("CelNavigation", u"\u00b4", None))
        self.comboBox_ns.setCurrentText("")
        self.spinBox_lon_deg.setSuffix(QCoreApplication.translate("CelNavigation", u"\u02da", None))
        self.doubleSpinBox_lon_min.setSuffix(QCoreApplication.translate("CelNavigation", u"\u00b4", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("CelNavigation", u"Fix", None))
        self.label_12.setText(QCoreApplication.translate("CelNavigation", u"Latiude:", None))
        self.label_13.setText(QCoreApplication.translate("CelNavigation", u"Longitude:", None))
        self.button_calculateFix.setText(QCoreApplication.translate("CelNavigation", u"Calculate Fix", None))
        self.label_time_of_fix.setText(QCoreApplication.translate("CelNavigation", u"???", None))
        self.label_14.setText(QCoreApplication.translate("CelNavigation", u"Time of Fix:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("CelNavigation", u"Sights", None))
        self.button_new.setText(QCoreApplication.translate("CelNavigation", u"New", None))
        self.button_edit.setText(QCoreApplication.translate("CelNavigation", u"edit", None))
        self.button_delete.setText(QCoreApplication.translate("CelNavigation", u"Delete", None))
        self.button_open.setText(QCoreApplication.translate("CelNavigation", u"Open", None))
        self.button_save.setText(QCoreApplication.translate("CelNavigation", u"Save", None))
        self.button_close.setText(QCoreApplication.translate("CelNavigation", u"Close", None))
        self.button_toLog.setText(QCoreApplication.translate("CelNavigation", u"Add to Log", None))
    # retranslateUi

