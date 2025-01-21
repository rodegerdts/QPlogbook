# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_edit.ui'
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
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_EditDialog(object):
    def setupUi(self, EditDialog):
        if not EditDialog.objectName():
            EditDialog.setObjectName(u"EditDialog")
        EditDialog.resize(738, 604)
        self.verticalLayout = QVBoxLayout(EditDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(EditDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.dateTimeEdit = QDateTimeEdit(EditDialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateTimeEdit)

        self.label_4 = QLabel(EditDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.latEdit = QDoubleSpinBox(EditDialog)
        self.latEdit.setObjectName(u"latEdit")
        self.latEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.latEdit.setDecimals(7)
        self.latEdit.setMinimum(-90.000000000000000)
        self.latEdit.setMaximum(90.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.latEdit)

        self.label_3 = QLabel(EditDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lonEdit = QDoubleSpinBox(EditDialog)
        self.lonEdit.setObjectName(u"lonEdit")
        self.lonEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lonEdit.setDecimals(6)
        self.lonEdit.setMinimum(-180.000000000000000)
        self.lonEdit.setMaximum(180.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lonEdit)

        self.label_19 = QLabel(EditDialog)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.sourceEdit = QLineEdit(EditDialog)
        self.sourceEdit.setObjectName(u"sourceEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sourceEdit)

        self.label_5 = QLabel(EditDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.logEdit = QSpinBox(EditDialog)
        self.logEdit.setObjectName(u"logEdit")
        self.logEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.logEdit.setMinimum(-1)
        self.logEdit.setMaximum(10000000)
        self.logEdit.setValue(-1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.logEdit)

        self.label_7 = QLabel(EditDialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.cogEdit = QSpinBox(EditDialog)
        self.cogEdit.setObjectName(u"cogEdit")
        self.cogEdit.setWrapping(True)
        self.cogEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.cogEdit.setMinimum(-1)
        self.cogEdit.setMaximum(359)
        self.cogEdit.setValue(-1)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cogEdit)

        self.label_15 = QLabel(EditDialog)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_15)

        self.headingEdit = QSpinBox(EditDialog)
        self.headingEdit.setObjectName(u"headingEdit")
        self.headingEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.headingEdit.setMinimum(-1)
        self.headingEdit.setMaximum(359)
        self.headingEdit.setValue(-1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.headingEdit)

        self.label_2 = QLabel(EditDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_2)

        self.sogEdit = QDoubleSpinBox(EditDialog)
        self.sogEdit.setObjectName(u"sogEdit")
        self.sogEdit.setDecimals(1)
        self.sogEdit.setMinimum(-1.000000000000000)
        self.sogEdit.setSingleStep(0.100000000000000)
        self.sogEdit.setValue(-1.000000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.sogEdit)

        self.label_8 = QLabel(EditDialog)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.stwEdit = QDoubleSpinBox(EditDialog)
        self.stwEdit.setObjectName(u"stwEdit")
        self.stwEdit.setDecimals(1)
        self.stwEdit.setMinimum(-1.000000000000000)
        self.stwEdit.setSingleStep(0.100000000000000)
        self.stwEdit.setValue(-1.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.stwEdit)

        self.label_6 = QLabel(EditDialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.engineEdit = QDoubleSpinBox(EditDialog)
        self.engineEdit.setObjectName(u"engineEdit")
        self.engineEdit.setDecimals(1)
        self.engineEdit.setMinimum(-1.000000000000000)
        self.engineEdit.setMaximum(1000000.000000000000000)
        self.engineEdit.setValue(-1.000000000000000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.engineEdit)

        self.updateButton = QPushButton(EditDialog)
        self.updateButton.setObjectName(u"updateButton")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.updateButton)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_10 = QLabel(EditDialog)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.twsEdit = QDoubleSpinBox(EditDialog)
        self.twsEdit.setObjectName(u"twsEdit")
        self.twsEdit.setToolTipDuration(3000)
        self.twsEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.twsEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.twsEdit.setDecimals(1)
        self.twsEdit.setMinimum(-1.000000000000000)
        self.twsEdit.setSingleStep(0.100000000000000)
        self.twsEdit.setValue(-1.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.twsEdit)

        self.label_11 = QLabel(EditDialog)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.twdEdit = QSpinBox(EditDialog)
        self.twdEdit.setObjectName(u"twdEdit")
        self.twdEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.twdEdit.setMinimum(-1)
        self.twdEdit.setMaximum(359)
        self.twdEdit.setValue(-1)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.twdEdit)

        self.label_13 = QLabel(EditDialog)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.pressureEdit = QDoubleSpinBox(EditDialog)
        self.pressureEdit.setObjectName(u"pressureEdit")
        self.pressureEdit.setDecimals(1)
        self.pressureEdit.setMinimum(0.000000000000000)
        self.pressureEdit.setMaximum(1084.000000000000000)
        self.pressureEdit.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.pressureEdit.setValue(0.000000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pressureEdit)

        self.label_17 = QLabel(EditDialog)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.seastateBox = QComboBox(EditDialog)
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.addItem("")
        self.seastateBox.setObjectName(u"seastateBox")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.seastateBox)

        self.label_16 = QLabel(EditDialog)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_16)

        self.cloudcoverSpinBox = QSpinBox(EditDialog)
        self.cloudcoverSpinBox.setObjectName(u"cloudcoverSpinBox")
        self.cloudcoverSpinBox.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.cloudcoverSpinBox.setMinimum(-1)
        self.cloudcoverSpinBox.setMaximum(8)
        self.cloudcoverSpinBox.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.cloudcoverSpinBox.setValue(-1)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.cloudcoverSpinBox)

        self.label_9 = QLabel(EditDialog)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.visibilityBox = QComboBox(EditDialog)
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.addItem("")
        self.visibilityBox.setObjectName(u"visibilityBox")
        self.visibilityBox.setMinimumSize(QSize(220, 0))

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.visibilityBox)

        self.label_12 = QLabel(EditDialog)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_12)

        self.crewBox = QListWidget(EditDialog)
        self.crewBox.setObjectName(u"crewBox")
        self.crewBox.setMaximumSize(QSize(220, 103))

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.crewBox)

        self.label_20 = QLabel(EditDialog)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_20)

        self.crewEdit = QLineEdit(EditDialog)
        self.crewEdit.setObjectName(u"crewEdit")
        self.crewEdit.setMinimumSize(QSize(220, 0))

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.crewEdit)

        self.addCrewButton = QPushButton(EditDialog)
        self.addCrewButton.setObjectName(u"addCrewButton")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.addCrewButton)

        self.delCrewButton = QPushButton(EditDialog)
        self.delCrewButton.setObjectName(u"delCrewButton")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.delCrewButton)

        self.airtempSpinBox = QDoubleSpinBox(EditDialog)
        self.airtempSpinBox.setObjectName(u"airtempSpinBox")
        self.airtempSpinBox.setDecimals(1)
        self.airtempSpinBox.setMinimum(-99.000000000000000)
        self.airtempSpinBox.setMaximum(98.000000000000000)
        self.airtempSpinBox.setSingleStep(0.100000000000000)
        self.airtempSpinBox.setValue(-99.000000000000000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.airtempSpinBox)

        self.label_18 = QLabel(EditDialog)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_18)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_14 = QLabel(EditDialog)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.TextEdit = QPlainTextEdit(EditDialog)
        self.TextEdit.setObjectName(u"TextEdit")

        self.verticalLayout.addWidget(self.TextEdit)

        self.buttonBox = QDialogButtonBox(EditDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EditDialog)
        self.buttonBox.accepted.connect(EditDialog.accept)
        self.buttonBox.rejected.connect(EditDialog.reject)

        QMetaObject.connectSlotsByName(EditDialog)
    # setupUi

    def retranslateUi(self, EditDialog):
        EditDialog.setWindowTitle(QCoreApplication.translate("EditDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("EditDialog", u"Date Time (UTC)", None))
        self.label_4.setText(QCoreApplication.translate("EditDialog", u"Latitude(\u00b0)", None))
        self.label_3.setText(QCoreApplication.translate("EditDialog", u"Longitude (\u00b0)", None))
        self.label_19.setText(QCoreApplication.translate("EditDialog", u"Nav. source", None))
        self.label_5.setText(QCoreApplication.translate("EditDialog", u"Log (nm)", None))
        self.label_7.setText(QCoreApplication.translate("EditDialog", u"Course over Ground (\u00b0)", None))
        self.label_15.setText(QCoreApplication.translate("EditDialog", u"Heading", None))
        self.label_2.setText(QCoreApplication.translate("EditDialog", u"Speed over Ground (kn)", None))
        self.label_8.setText(QCoreApplication.translate("EditDialog", u"Speed through water (kn)", None))
        self.label_6.setText(QCoreApplication.translate("EditDialog", u"Engine hours", None))
        self.updateButton.setText(QCoreApplication.translate("EditDialog", u"update from SK", None))
        self.label_10.setText(QCoreApplication.translate("EditDialog", u"True wind speed (kn)", None))
#if QT_CONFIG(tooltip)
        self.twsEdit.setToolTip(QCoreApplication.translate("EditDialog", u"TWS in Knots", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.twsEdit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.twsEdit.setSpecialValueText("")
        self.label_11.setText(QCoreApplication.translate("EditDialog", u"True wind direction (\u00b0)", None))
        self.label_13.setText(QCoreApplication.translate("EditDialog", u"Barometric pressure (hPa)", None))
        self.label_17.setText(QCoreApplication.translate("EditDialog", u"Sea state", None))
        self.seastateBox.setItemText(0, QCoreApplication.translate("EditDialog", u"--", None))
        self.seastateBox.setItemText(1, QCoreApplication.translate("EditDialog", u"Calm (glassy) 0m", None))
        self.seastateBox.setItemText(2, QCoreApplication.translate("EditDialog", u"Calm (rippled) 0 - 0.1m", None))
        self.seastateBox.setItemText(3, QCoreApplication.translate("EditDialog", u"Smooth (wavelets) 0.1 - 0.5m", None))
        self.seastateBox.setItemText(4, QCoreApplication.translate("EditDialog", u"Slight 0.5 - 1.25m", None))
        self.seastateBox.setItemText(5, QCoreApplication.translate("EditDialog", u"Moderate 1.25 - 2.5m", None))
        self.seastateBox.setItemText(6, QCoreApplication.translate("EditDialog", u"Rough 2.5 - 4m", None))
        self.seastateBox.setItemText(7, QCoreApplication.translate("EditDialog", u"Very Rough 4 -6m", None))
        self.seastateBox.setItemText(8, QCoreApplication.translate("EditDialog", u"High  6 - 9", None))
        self.seastateBox.setItemText(9, QCoreApplication.translate("EditDialog", u"Very high 9-14m", None))
        self.seastateBox.setItemText(10, QCoreApplication.translate("EditDialog", u"Phenomenal >14m", None))

        self.seastateBox.setCurrentText(QCoreApplication.translate("EditDialog", u"--", None))
        self.label_16.setText(QCoreApplication.translate("EditDialog", u"Cloud cover (8th)", None))
        self.label_9.setText(QCoreApplication.translate("EditDialog", u"Visibility", None))
        self.visibilityBox.setItemText(0, QCoreApplication.translate("EditDialog", u"--", None))
        self.visibilityBox.setItemText(1, QCoreApplication.translate("EditDialog", u"Dense Fog <50m", None))
        self.visibilityBox.setItemText(2, QCoreApplication.translate("EditDialog", u"Thick Fog 50-200m", None))
        self.visibilityBox.setItemText(3, QCoreApplication.translate("EditDialog", u"Moderate Fog 200-500m", None))
        self.visibilityBox.setItemText(4, QCoreApplication.translate("EditDialog", u"Light Fog 0,5-1km", None))
        self.visibilityBox.setItemText(5, QCoreApplication.translate("EditDialog", u"Thin Fog 1-2km", None))
        self.visibilityBox.setItemText(6, QCoreApplication.translate("EditDialog", u"Haze 2-4km", None))
        self.visibilityBox.setItemText(7, QCoreApplication.translate("EditDialog", u"Light Haze 4-10km", None))
        self.visibilityBox.setItemText(8, QCoreApplication.translate("EditDialog", u"Clear 10-20km", None))
        self.visibilityBox.setItemText(9, QCoreApplication.translate("EditDialog", u"Very Clear 20-50km", None))
        self.visibilityBox.setItemText(10, QCoreApplication.translate("EditDialog", u"Exceptionally Clear >50km", None))

        self.label_12.setText(QCoreApplication.translate("EditDialog", u"Crew", None))
        self.label_20.setText(QCoreApplication.translate("EditDialog", u"New Crew", None))
        self.addCrewButton.setText(QCoreApplication.translate("EditDialog", u"Add Crew", None))
        self.delCrewButton.setText(QCoreApplication.translate("EditDialog", u"Delete Crew", None))
        self.label_18.setText(QCoreApplication.translate("EditDialog", u"Air temperature (\u02daC)", None))
        self.label_14.setText(QCoreApplication.translate("EditDialog", u"Text:", None))
    # retranslateUi

