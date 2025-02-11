# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_sight.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QComboBox,
    QDateTimeEdit, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_DialogSight(object):
    def setupUi(self, DialogSight):
        if not DialogSight.objectName():
            DialogSight.setObjectName(u"DialogSight")
        DialogSight.resize(371, 441)
        self.verticalLayout = QVBoxLayout(DialogSight)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DialogSight)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.dateTimeEdit_sight = QDateTimeEdit(DialogSight)
        self.dateTimeEdit_sight.setObjectName(u"dateTimeEdit_sight")
        self.dateTimeEdit_sight.setDateTime(QDateTime(QDate(1999, 12, 31), QTime(19, 0, 0)))
        self.dateTimeEdit_sight.setMaximumDateTime(QDateTime(QDate(9999, 12, 28), QTime(17, 59, 59)))
        self.dateTimeEdit_sight.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateTimeEdit_sight.setTimeSpec(Qt.TimeSpec.UTC)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateTimeEdit_sight)

        self.label_4 = QLabel(DialogSight)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.comboBox_body = QComboBox(DialogSight)
        self.comboBox_body.setObjectName(u"comboBox_body")
        self.comboBox_body.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_body)

        self.label_az = QLabel(DialogSight)
        self.label_az.setObjectName(u"label_az")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_az)

        self.label_hc = QLabel(DialogSight)
        self.label_hc.setObjectName(u"label_hc")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_hc)

        self.label_3 = QLabel(DialogSight)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox_Hs_deg = QSpinBox(DialogSight)
        self.spinBox_Hs_deg.setObjectName(u"spinBox_Hs_deg")

        self.horizontalLayout_2.addWidget(self.spinBox_Hs_deg)

        self.doubleSpinBox_Hs_min = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_Hs_min.setObjectName(u"doubleSpinBox_Hs_min")
        self.doubleSpinBox_Hs_min.setDecimals(1)
        self.doubleSpinBox_Hs_min.setMaximum(59.899999999999999)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_Hs_min)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.button_Hs_to_Hc = QPushButton(DialogSight)
        self.button_Hs_to_Hc.setObjectName(u"button_Hs_to_Hc")

        self.horizontalLayout_2.addWidget(self.button_Hs_to_Hc)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_2 = QLabel(DialogSight)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox_alt_deg = QSpinBox(DialogSight)
        self.spinBox_alt_deg.setObjectName(u"spinBox_alt_deg")
        self.spinBox_alt_deg.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_alt_deg.setMinimum(0)
        self.spinBox_alt_deg.setMaximum(89)

        self.horizontalLayout.addWidget(self.spinBox_alt_deg)

        self.doubleSpinBox_alt_min = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_alt_min.setObjectName(u"doubleSpinBox_alt_min")
        self.doubleSpinBox_alt_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.doubleSpinBox_alt_min.setDecimals(1)
        self.doubleSpinBox_alt_min.setMaximum(59.899999999999999)

        self.horizontalLayout.addWidget(self.doubleSpinBox_alt_min)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_actoalt = QPushButton(DialogSight)
        self.button_actoalt.setObjectName(u"button_actoalt")

        self.horizontalLayout.addWidget(self.button_actoalt)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_6 = QLabel(DialogSight)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spinBox_lat_deg = QSpinBox(DialogSight)
        self.spinBox_lat_deg.setObjectName(u"spinBox_lat_deg")
        self.spinBox_lat_deg.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lat_deg.setMinimum(-90)
        self.spinBox_lat_deg.setMaximum(90)

        self.horizontalLayout_4.addWidget(self.spinBox_lat_deg)

        self.doubleSpinBox_lat_min = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_lat_min.setObjectName(u"doubleSpinBox_lat_min")
        self.doubleSpinBox_lat_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lat_min.setDecimals(1)
        self.doubleSpinBox_lat_min.setMaximum(59.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_lat_min)

        self.comboBox_ns = QComboBox(DialogSight)
        self.comboBox_ns.setObjectName(u"comboBox_ns")
        self.comboBox_ns.setMaxVisibleItems(3)

        self.horizontalLayout_4.addWidget(self.comboBox_ns)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_5 = QLabel(DialogSight)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBox_lon_deg = QSpinBox(DialogSight)
        self.spinBox_lon_deg.setObjectName(u"spinBox_lon_deg")
        self.spinBox_lon_deg.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spinBox_lon_deg.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lon_deg.setMinimum(-180)
        self.spinBox_lon_deg.setMaximum(180)

        self.horizontalLayout_3.addWidget(self.spinBox_lon_deg)

        self.doubleSpinBox_lon_min = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_lon_min.setObjectName(u"doubleSpinBox_lon_min")
        self.doubleSpinBox_lon_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lon_min.setDecimals(1)
        self.doubleSpinBox_lon_min.setMaximum(59.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_lon_min)

        self.comboBox_we = QComboBox(DialogSight)
        self.comboBox_we.setObjectName(u"comboBox_we")
        self.comboBox_we.setMaxVisibleItems(2)

        self.horizontalLayout_3.addWidget(self.comboBox_we)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_10 = QLabel(DialogSight)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_10)

        self.doubleSpinBox_temperature = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_temperature.setObjectName(u"doubleSpinBox_temperature")
        self.doubleSpinBox_temperature.setDecimals(1)
        self.doubleSpinBox_temperature.setMinimum(-100.000000000000000)
        self.doubleSpinBox_temperature.setSingleStep(0.100000000000000)
        self.doubleSpinBox_temperature.setValue(25.000000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.doubleSpinBox_temperature)

        self.label_9 = QLabel(DialogSight)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.doubleSpinBox_pressure = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_pressure.setObjectName(u"doubleSpinBox_pressure")
        self.doubleSpinBox_pressure.setDecimals(1)
        self.doubleSpinBox_pressure.setMaximum(1080.000000000000000)
        self.doubleSpinBox_pressure.setValue(1013.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.doubleSpinBox_pressure)

        self.label_7 = QLabel(DialogSight)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_7)

        self.doubleSpinBox_indexerror = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_indexerror.setObjectName(u"doubleSpinBox_indexerror")
        self.doubleSpinBox_indexerror.setDecimals(1)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.doubleSpinBox_indexerror)

        self.label_8 = QLabel(DialogSight)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox_hoe = QDoubleSpinBox(DialogSight)
        self.doubleSpinBox_hoe.setObjectName(u"doubleSpinBox_hoe")
        self.doubleSpinBox_hoe.setDecimals(1)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.doubleSpinBox_hoe)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(DialogSight)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogSight)
        self.buttonBox.accepted.connect(DialogSight.accept)
        self.buttonBox.rejected.connect(DialogSight.reject)

        self.comboBox_ns.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(DialogSight)
    # setupUi

    def retranslateUi(self, DialogSight):
        DialogSight.setWindowTitle(QCoreApplication.translate("DialogSight", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogSight", u"Time:", None))
        self.dateTimeEdit_sight.setDisplayFormat(QCoreApplication.translate("DialogSight", u"dd/MM/yyyy HH:mm:ss", None))
        self.label_4.setText(QCoreApplication.translate("DialogSight", u"Body:", None))
        self.label_az.setText(QCoreApplication.translate("DialogSight", u"Az:?", None))
        self.label_hc.setText(QCoreApplication.translate("DialogSight", u"Hc:?", None))
        self.label_3.setText(QCoreApplication.translate("DialogSight", u"Sextant altiude (Hs)", None))
        self.spinBox_Hs_deg.setSuffix(QCoreApplication.translate("DialogSight", u"\u02da", None))
        self.doubleSpinBox_Hs_min.setSuffix(QCoreApplication.translate("DialogSight", u"\u00b4", None))
        self.button_Hs_to_Hc.setText(QCoreApplication.translate("DialogSight", u"Hs -> Ho", None))
        self.label_2.setText(QCoreApplication.translate("DialogSight", u"Altitude (Ho):", None))
        self.spinBox_alt_deg.setSuffix(QCoreApplication.translate("DialogSight", u"\u02da", None))
        self.doubleSpinBox_alt_min.setSuffix(QCoreApplication.translate("DialogSight", u"\u00b4", None))
        self.button_actoalt.setText(QCoreApplication.translate("DialogSight", u"Hc -> Ho", None))
        self.label_6.setText(QCoreApplication.translate("DialogSight", u"Latitude:", None))
        self.spinBox_lat_deg.setSuffix(QCoreApplication.translate("DialogSight", u"\u02da", None))
        self.doubleSpinBox_lat_min.setSuffix(QCoreApplication.translate("DialogSight", u"\u00b4", None))
        self.comboBox_ns.setCurrentText("")
        self.label_5.setText(QCoreApplication.translate("DialogSight", u"Longitude:", None))
        self.spinBox_lon_deg.setSuffix(QCoreApplication.translate("DialogSight", u"\u02da", None))
        self.doubleSpinBox_lon_min.setSuffix(QCoreApplication.translate("DialogSight", u"\u00b4", None))
        self.label_10.setText(QCoreApplication.translate("DialogSight", u"Temperaure", None))
        self.doubleSpinBox_temperature.setSuffix(QCoreApplication.translate("DialogSight", u"\u02daC", None))
        self.label_9.setText(QCoreApplication.translate("DialogSight", u"Pressure", None))
        self.doubleSpinBox_pressure.setSuffix(QCoreApplication.translate("DialogSight", u" hPa", None))
        self.label_7.setText(QCoreApplication.translate("DialogSight", u"Index Error", None))
        self.doubleSpinBox_indexerror.setSuffix(QCoreApplication.translate("DialogSight", u"\u00b4", None))
        self.label_8.setText(QCoreApplication.translate("DialogSight", u"Hight of Eye", None))
        self.doubleSpinBox_hoe.setSuffix(QCoreApplication.translate("DialogSight", u" m", None))
    # retranslateUi

