# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_dr.ui'
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
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_DialogDR(object):
    def setupUi(self, DialogDR):
        if not DialogDR.objectName():
            DialogDR.setObjectName(u"DialogDR")
        DialogDR.resize(568, 350)
        self.gridLayout = QGridLayout(DialogDR)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(DialogDR)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.dateTimeEdit_old = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_old.setObjectName(u"dateTimeEdit_old")
        self.dateTimeEdit_old.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateTimeEdit_old.setTimeSpec(Qt.TimeSpec.UTC)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.dateTimeEdit_old)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox_lat_deg_old = QSpinBox(self.groupBox)
        self.spinBox_lat_deg_old.setObjectName(u"spinBox_lat_deg_old")
        self.spinBox_lat_deg_old.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lat_deg_old.setMinimum(-90)
        self.spinBox_lat_deg_old.setMaximum(90)

        self.horizontalLayout_2.addWidget(self.spinBox_lat_deg_old)

        self.doubleSpinBox_lat_min_old = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_lat_min_old.setObjectName(u"doubleSpinBox_lat_min_old")
        self.doubleSpinBox_lat_min_old.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lat_min_old.setDecimals(1)
        self.doubleSpinBox_lat_min_old.setMaximum(59.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_lat_min_old)

        self.comboBox_ns_old = QComboBox(self.groupBox)
        self.comboBox_ns_old.setObjectName(u"comboBox_ns_old")
        self.comboBox_ns_old.setMaxVisibleItems(3)

        self.horizontalLayout_2.addWidget(self.comboBox_ns_old)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spinBox_lon_deg_old = QSpinBox(self.groupBox)
        self.spinBox_lon_deg_old.setObjectName(u"spinBox_lon_deg_old")
        self.spinBox_lon_deg_old.setWrapping(True)
        self.spinBox_lon_deg_old.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spinBox_lon_deg_old.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lon_deg_old.setMinimum(-180)
        self.spinBox_lon_deg_old.setMaximum(180)

        self.horizontalLayout_4.addWidget(self.spinBox_lon_deg_old)

        self.doubleSpinBox_lon_min_old = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_lon_min_old.setObjectName(u"doubleSpinBox_lon_min_old")
        self.doubleSpinBox_lon_min_old.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lon_min_old.setDecimals(1)
        self.doubleSpinBox_lon_min_old.setMaximum(59.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_lon_min_old)

        self.comboBox_we_old = QComboBox(self.groupBox)
        self.comboBox_we_old.setObjectName(u"comboBox_we_old")
        self.comboBox_we_old.setMaxVisibleItems(2)

        self.horizontalLayout_4.addWidget(self.comboBox_we_old)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_3 = QGroupBox(DialogDR)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox_sog = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_sog.setObjectName(u"doubleSpinBox_sog")
        self.doubleSpinBox_sog.setDecimals(1)
        self.doubleSpinBox_sog.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_sog)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.spinBox_cog = QSpinBox(self.groupBox_3)
        self.spinBox_cog.setObjectName(u"spinBox_cog")
        self.spinBox_cog.setWrapping(True)
        self.spinBox_cog.setMaximum(359)
        self.spinBox_cog.setSingleStep(1)
        self.spinBox_cog.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_cog)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.doubleSpinBox_log = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_log.setObjectName(u"doubleSpinBox_log")
        self.doubleSpinBox_log.setDecimals(1)
        self.doubleSpinBox_log.setMaximum(1000000.000000000000000)
        self.doubleSpinBox_log.setSingleStep(1.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_log)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.spinBox_delta_h = QSpinBox(self.groupBox_3)
        self.spinBox_delta_h.setObjectName(u"spinBox_delta_h")
        self.spinBox_delta_h.setReadOnly(True)
        self.spinBox_delta_h.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_delta_h.setMinimum(0)
        self.spinBox_delta_h.setMaximum(1000)

        self.horizontalLayout_5.addWidget(self.spinBox_delta_h)

        self.spinBox_delta_min = QSpinBox(self.groupBox_3)
        self.spinBox_delta_min.setObjectName(u"spinBox_delta_min")
        self.spinBox_delta_min.setReadOnly(True)
        self.spinBox_delta_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_delta_min.setMaximum(59)

        self.horizontalLayout_5.addWidget(self.spinBox_delta_min)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox_2 = QGroupBox(DialogDR)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.dateTimeEdit_dr = QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit_dr.setObjectName(u"dateTimeEdit_dr")
        self.dateTimeEdit_dr.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateTimeEdit_dr.setTimeSpec(Qt.TimeSpec.UTC)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.dateTimeEdit_dr)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBox_lon_deg_dr = QSpinBox(self.groupBox_2)
        self.spinBox_lon_deg_dr.setObjectName(u"spinBox_lon_deg_dr")
        self.spinBox_lon_deg_dr.setWrapping(True)
        self.spinBox_lon_deg_dr.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spinBox_lon_deg_dr.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lon_deg_dr.setMinimum(-180)
        self.spinBox_lon_deg_dr.setMaximum(180)

        self.horizontalLayout_3.addWidget(self.spinBox_lon_deg_dr)

        self.doubleSpinBox_lon_min_dr = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_lon_min_dr.setObjectName(u"doubleSpinBox_lon_min_dr")
        self.doubleSpinBox_lon_min_dr.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lon_min_dr.setDecimals(1)
        self.doubleSpinBox_lon_min_dr.setMaximum(59.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_lon_min_dr)

        self.comboBox_we_dr = QComboBox(self.groupBox_2)
        self.comboBox_we_dr.setObjectName(u"comboBox_we_dr")
        self.comboBox_we_dr.setMaxVisibleItems(2)

        self.horizontalLayout_3.addWidget(self.comboBox_we_dr)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox_lat_deg_dr = QSpinBox(self.groupBox_2)
        self.spinBox_lat_deg_dr.setObjectName(u"spinBox_lat_deg_dr")
        self.spinBox_lat_deg_dr.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_lat_deg_dr.setMinimum(-90)
        self.spinBox_lat_deg_dr.setMaximum(90)

        self.horizontalLayout.addWidget(self.spinBox_lat_deg_dr)

        self.doubleSpinBox_lat_min_dr = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_lat_min_dr.setObjectName(u"doubleSpinBox_lat_min_dr")
        self.doubleSpinBox_lat_min_dr.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_lat_min_dr.setDecimals(1)
        self.doubleSpinBox_lat_min_dr.setMaximum(59.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_lat_min_dr)

        self.comboBox_ns_dr = QComboBox(self.groupBox_2)
        self.comboBox_ns_dr.setObjectName(u"comboBox_ns_dr")
        self.comboBox_ns_dr.setMaxVisibleItems(3)

        self.horizontalLayout.addWidget(self.comboBox_ns_dr)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 2, 2)

        self.buttonBox = QDialogButtonBox(DialogDR)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)


        self.retranslateUi(DialogDR)
        self.buttonBox.accepted.connect(DialogDR.accept)
        self.buttonBox.rejected.connect(DialogDR.reject)

        self.comboBox_ns_old.setCurrentIndex(-1)
        self.comboBox_ns_dr.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(DialogDR)
    # setupUi

    def retranslateUi(self, DialogDR):
        DialogDR.setWindowTitle(QCoreApplication.translate("DialogDR", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogDR", u"Previous position", None))
        self.label_12.setText(QCoreApplication.translate("DialogDR", u"Time", None))
        self.dateTimeEdit_old.setDisplayFormat(QCoreApplication.translate("DialogDR", u"dd/MM/yyyy HH:mm:ss", None))
        self.label_3.setText(QCoreApplication.translate("DialogDR", u"Latitude:", None))
        self.spinBox_lat_deg_old.setSuffix(QCoreApplication.translate("DialogDR", u"\u02da", None))
        self.doubleSpinBox_lat_min_old.setSuffix(QCoreApplication.translate("DialogDR", u"\u00b4", None))
        self.comboBox_ns_old.setCurrentText("")
        self.label_4.setText(QCoreApplication.translate("DialogDR", u"Longitude:", None))
        self.spinBox_lon_deg_old.setSuffix(QCoreApplication.translate("DialogDR", u"\u02da", None))
        self.doubleSpinBox_lon_min_old.setSuffix(QCoreApplication.translate("DialogDR", u"\u00b4", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DialogDR", u"Parmeters:", None))
        self.label_8.setText(QCoreApplication.translate("DialogDR", u"SOG", None))
        self.doubleSpinBox_sog.setSuffix(QCoreApplication.translate("DialogDR", u" kn", None))
        self.label_7.setText(QCoreApplication.translate("DialogDR", u"COG", None))
        self.spinBox_cog.setSuffix(QCoreApplication.translate("DialogDR", u"\u02da", None))
        self.label_5.setText(QCoreApplication.translate("DialogDR", u"Distance:", None))
        self.doubleSpinBox_log.setSuffix(QCoreApplication.translate("DialogDR", u" nm", None))
        self.label_6.setText(QCoreApplication.translate("DialogDR", u"Time \u0394", None))
        self.spinBox_delta_h.setSuffix(QCoreApplication.translate("DialogDR", u"h", None))
        self.spinBox_delta_min.setSuffix(QCoreApplication.translate("DialogDR", u"min", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogDR", u"DR position", None))
        self.label.setText(QCoreApplication.translate("DialogDR", u"Latitude:", None))
        self.label_2.setText(QCoreApplication.translate("DialogDR", u"Longitude:", None))
        self.label_11.setText(QCoreApplication.translate("DialogDR", u"Time", None))
        self.dateTimeEdit_dr.setDisplayFormat(QCoreApplication.translate("DialogDR", u"dd/MM/yyyy HH:mm:ss", None))
        self.spinBox_lon_deg_dr.setSuffix(QCoreApplication.translate("DialogDR", u"\u02da", None))
        self.doubleSpinBox_lon_min_dr.setSuffix(QCoreApplication.translate("DialogDR", u"\u00b4", None))
        self.spinBox_lat_deg_dr.setSuffix(QCoreApplication.translate("DialogDR", u"\u02da", None))
        self.doubleSpinBox_lat_min_dr.setSuffix(QCoreApplication.translate("DialogDR", u"\u00b4", None))
        self.comboBox_ns_dr.setCurrentText("")
    # retranslateUi

