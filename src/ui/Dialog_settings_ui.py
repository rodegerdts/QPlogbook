# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_settings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QSpinBox, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)
import QPLresources_rc

class Ui_DialogSettings(object):
    def setupUi(self, DialogSettings):
        if not DialogSettings.objectName():
            DialogSettings.setObjectName(u"DialogSettings")
        DialogSettings.resize(930, 602)
        self.verticalLayout = QVBoxLayout(DialogSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(DialogSettings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setToolTipDuration(-1)
        self.tab_generel = QWidget()
        self.tab_generel.setObjectName(u"tab_generel")
        self.verticalLayout_3 = QVBoxLayout(self.tab_generel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.label_31 = QLabel(self.tab_generel)
        self.label_31.setObjectName(u"label_31")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMaximumSize(QSize(16777215, 40))
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_31, 5, 0, 1, 1)

        self.spinBox_mmsi = QSpinBox(self.tab_generel)
        self.spinBox_mmsi.setObjectName(u"spinBox_mmsi")
        self.spinBox_mmsi.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_mmsi.setMinimum(100000000)
        self.spinBox_mmsi.setMaximum(999999999)
        self.spinBox_mmsi.setSingleStep(1)

        self.gridLayout_2.addWidget(self.spinBox_mmsi, 1, 5, 1, 1)

        self.checkBox_autoentry = QCheckBox(self.tab_generel)
        self.checkBox_autoentry.setObjectName(u"checkBox_autoentry")
        self.checkBox_autoentry.setToolTipDuration(1500)

        self.gridLayout_2.addWidget(self.checkBox_autoentry, 4, 2, 1, 1)

        self.label_25 = QLabel(self.tab_generel)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_25, 2, 4, 1, 1)

        self.doubleSpinBox_timeout = QDoubleSpinBox(self.tab_generel)
        self.doubleSpinBox_timeout.setObjectName(u"doubleSpinBox_timeout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_timeout.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_timeout.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_timeout.setSingleStep(0.010000000000000)
        self.doubleSpinBox_timeout.setValue(0.100000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_timeout, 6, 1, 1, 1)

        self.label_27 = QLabel(self.tab_generel)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_27, 2, 0, 1, 1)

        self.doubleSpinBox_loa = QDoubleSpinBox(self.tab_generel)
        self.doubleSpinBox_loa.setObjectName(u"doubleSpinBox_loa")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_loa.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_loa.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.doubleSpinBox_loa, 2, 5, 1, 1)

        self.label_19 = QLabel(self.tab_generel)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)

        self.doubleSpinBox_draft = QDoubleSpinBox(self.tab_generel)
        self.doubleSpinBox_draft.setObjectName(u"doubleSpinBox_draft")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_draft.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_draft.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.doubleSpinBox_draft, 2, 7, 1, 1)

        self.label_21 = QLabel(self.tab_generel)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMaximumSize(QSize(16777215, 40))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)

        self.label_30 = QLabel(self.tab_generel)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_30, 0, 1, 1, 1)

        self.doubleSpinBox_hight = QDoubleSpinBox(self.tab_generel)
        self.doubleSpinBox_hight.setObjectName(u"doubleSpinBox_hight")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_hight.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_hight.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.doubleSpinBox_hight, 2, 1, 1, 1)

        self.checkBox_evententrys = QCheckBox(self.tab_generel)
        self.checkBox_evententrys.setObjectName(u"checkBox_evententrys")
        self.checkBox_evententrys.setToolTipDuration(1500)

        self.gridLayout_2.addWidget(self.checkBox_evententrys, 5, 2, 1, 1)

        self.doubleSpinBox_beam = QDoubleSpinBox(self.tab_generel)
        self.doubleSpinBox_beam.setObjectName(u"doubleSpinBox_beam")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_beam.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_beam.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.doubleSpinBox_beam, 2, 3, 1, 1)

        self.label_29 = QLabel(self.tab_generel)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMaximumSize(QSize(16777215, 40))
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_29, 4, 0, 1, 1)

        self.label_20 = QLabel(self.tab_generel)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_20, 1, 2, 1, 1)

        self.label_24 = QLabel(self.tab_generel)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_24, 1, 4, 1, 1)

        self.label_26 = QLabel(self.tab_generel)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_26, 2, 6, 1, 1)

        self.label_32 = QLabel(self.tab_generel)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMaximumSize(QSize(16777215, 40))
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_32, 6, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.tab_generel)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout_2.addWidget(self.lineEdit_name, 1, 1, 1, 1)

        self.lineEdit_call_sign = QLineEdit(self.tab_generel)
        self.lineEdit_call_sign.setObjectName(u"lineEdit_call_sign")

        self.gridLayout_2.addWidget(self.lineEdit_call_sign, 1, 3, 1, 1)

        self.label_28 = QLabel(self.tab_generel)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_28, 2, 2, 1, 1)

        self.spinBox_update_interv = QSpinBox(self.tab_generel)
        self.spinBox_update_interv.setObjectName(u"spinBox_update_interv")
        sizePolicy1.setHeightForWidth(self.spinBox_update_interv.sizePolicy().hasHeightForWidth())
        self.spinBox_update_interv.setSizePolicy(sizePolicy1)
        self.spinBox_update_interv.setMinimum(1)
        self.spinBox_update_interv.setMaximum(24)
        self.spinBox_update_interv.setSingleStep(0)

        self.gridLayout_2.addWidget(self.spinBox_update_interv, 4, 1, 1, 1)

        self.spinBox_track_interv = QSpinBox(self.tab_generel)
        self.spinBox_track_interv.setObjectName(u"spinBox_track_interv")
        sizePolicy1.setHeightForWidth(self.spinBox_track_interv.sizePolicy().hasHeightForWidth())
        self.spinBox_track_interv.setSizePolicy(sizePolicy1)
        self.spinBox_track_interv.setMinimum(1)
        self.spinBox_track_interv.setMaximum(59)

        self.gridLayout_2.addWidget(self.spinBox_track_interv, 5, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 3)
        self.gridLayout_2.setColumnStretch(3, 3)
        self.gridLayout_2.setColumnStretch(4, 3)
        self.gridLayout_2.setColumnStretch(5, 4)
        self.gridLayout_2.setColumnStretch(6, 3)
        self.gridLayout_2.setColumnStretch(7, 3)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, 17, 12)
        self.label_22 = QLabel(self.tab_generel)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)

        self.lineEdit_qplog_dir = QLineEdit(self.tab_generel)
        self.lineEdit_qplog_dir.setObjectName(u"lineEdit_qplog_dir")
        self.lineEdit_qplog_dir.setMinimumSize(QSize(250, 0))

        self.gridLayout_3.addWidget(self.lineEdit_qplog_dir, 1, 1, 1, 1)

        self.lineEdit_sklog_dir = QLineEdit(self.tab_generel)
        self.lineEdit_sklog_dir.setObjectName(u"lineEdit_sklog_dir")
        self.lineEdit_sklog_dir.setMinimumSize(QSize(250, 0))

        self.gridLayout_3.addWidget(self.lineEdit_sklog_dir, 4, 1, 1, 1)

        self.qplPathButton = QToolButton(self.tab_generel)
        self.qplPathButton.setObjectName(u"qplPathButton")
        icon = QIcon()
        icon.addFile(u":/icons/SVG/document-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.qplPathButton.setIcon(icon)

        self.gridLayout_3.addWidget(self.qplPathButton, 1, 2, 1, 1)

        self.sklPathButton = QToolButton(self.tab_generel)
        self.sklPathButton.setObjectName(u"sklPathButton")
        self.sklPathButton.setIcon(icon)

        self.gridLayout_3.addWidget(self.sklPathButton, 4, 2, 1, 1)

        self.label_23 = QLabel(self.tab_generel)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 4, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.label_33 = QLabel(self.tab_generel)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMaximumSize(QSize(16777215, 40))
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_33)

        self.lineEdit_server = QLineEdit(self.tab_generel)
        self.lineEdit_server.setObjectName(u"lineEdit_server")
        self.lineEdit_server.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_server.sizePolicy().hasHeightForWidth())
        self.lineEdit_server.setSizePolicy(sizePolicy2)
        self.lineEdit_server.setMinimumSize(QSize(250, 0))
        self.lineEdit_server.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_server.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_server)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_generel, "")
        self.tab_SKkeys = QWidget()
        self.tab_SKkeys.setObjectName(u"tab_SKkeys")
        self.gridLayoutWidget = QWidget(self.tab_SKkeys)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 861, 486))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_stw = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_stw.setObjectName(u"lineEdit_stw")

        self.gridLayout.addWidget(self.lineEdit_stw, 8, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 14, 0, 1, 1)

        self.checkBox_sog = QCheckBox(self.gridLayoutWidget)
        self.checkBox_sog.setObjectName(u"checkBox_sog")
        self.checkBox_sog.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_sog, 5, 2, 1, 1)

        self.checkBox_airpressure = QCheckBox(self.gridLayoutWidget)
        self.checkBox_airpressure.setObjectName(u"checkBox_airpressure")

        self.gridLayout.addWidget(self.checkBox_airpressure, 12, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.checkBox_s_airpressure = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_airpressure.setObjectName(u"checkBox_s_airpressure")

        self.gridLayout.addWidget(self.checkBox_s_airpressure, 12, 3, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)

        self.lineEdit_log = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_log.setObjectName(u"lineEdit_log")

        self.gridLayout.addWidget(self.lineEdit_log, 3, 1, 1, 1)

        self.checkBox_s_log = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_log.setObjectName(u"checkBox_s_log")
        self.checkBox_s_log.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_s_log, 3, 3, 1, 1)

        self.checkBox_s_sog = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_sog.setObjectName(u"checkBox_s_sog")

        self.gridLayout.addWidget(self.checkBox_s_sog, 5, 3, 1, 1)

        self.lineEdit_position = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_position.setObjectName(u"lineEdit_position")

        self.gridLayout.addWidget(self.lineEdit_position, 2, 1, 1, 1)

        self.checkBox_s_stw = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_stw.setObjectName(u"checkBox_s_stw")

        self.gridLayout.addWidget(self.checkBox_s_stw, 8, 3, 1, 1)

        self.checkBox_s_hdop = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_hdop.setObjectName(u"checkBox_s_hdop")

        self.gridLayout.addWidget(self.checkBox_s_hdop, 14, 3, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 15, 0, 1, 1)

        self.checkBox_fix = QCheckBox(self.gridLayoutWidget)
        self.checkBox_fix.setObjectName(u"checkBox_fix")

        self.gridLayout.addWidget(self.checkBox_fix, 15, 2, 1, 1)

        self.lineEdit_sog = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_sog.setObjectName(u"lineEdit_sog")

        self.gridLayout.addWidget(self.lineEdit_sog, 5, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)

        self.checkBox_s_fix = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_fix.setObjectName(u"checkBox_s_fix")

        self.gridLayout.addWidget(self.checkBox_s_fix, 15, 3, 1, 1)

        self.lineEdit_temp = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_temp.setObjectName(u"lineEdit_temp")

        self.gridLayout.addWidget(self.lineEdit_temp, 11, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)

        self.lineEdit_airpressure = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_airpressure.setObjectName(u"lineEdit_airpressure")

        self.gridLayout.addWidget(self.lineEdit_airpressure, 12, 1, 1, 1)

        self.lineEdit_engine = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_engine.setObjectName(u"lineEdit_engine")

        self.gridLayout.addWidget(self.lineEdit_engine, 4, 1, 1, 1)

        self.checkBox_engine = QCheckBox(self.gridLayoutWidget)
        self.checkBox_engine.setObjectName(u"checkBox_engine")
        self.checkBox_engine.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_engine, 4, 2, 1, 1)

        self.checkBox_s_engine = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_engine.setObjectName(u"checkBox_s_engine")

        self.gridLayout.addWidget(self.checkBox_s_engine, 4, 3, 1, 1)

        self.checkBox_cog = QCheckBox(self.gridLayoutWidget)
        self.checkBox_cog.setObjectName(u"checkBox_cog")
        self.checkBox_cog.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_cog, 6, 2, 1, 1)

        self.checkBox_temp = QCheckBox(self.gridLayoutWidget)
        self.checkBox_temp.setObjectName(u"checkBox_temp")

        self.gridLayout.addWidget(self.checkBox_temp, 11, 2, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setToolTipDuration(2000)

        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)

        self.checkBox_s_heading = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_heading.setObjectName(u"checkBox_s_heading")

        self.gridLayout.addWidget(self.checkBox_s_heading, 7, 3, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 10, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)

        self.checkBox_s_humidity = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_humidity.setObjectName(u"checkBox_s_humidity")

        self.gridLayout.addWidget(self.checkBox_s_humidity, 13, 3, 1, 1)

        self.checkBox_s_tws = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_tws.setObjectName(u"checkBox_s_tws")

        self.gridLayout.addWidget(self.checkBox_s_tws, 9, 3, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 5, 0, 1, 1)

        self.lineEdit_cog = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_cog.setObjectName(u"lineEdit_cog")

        self.gridLayout.addWidget(self.lineEdit_cog, 6, 1, 1, 1)

        self.lineEdit_hdop = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_hdop.setObjectName(u"lineEdit_hdop")

        self.gridLayout.addWidget(self.lineEdit_hdop, 14, 1, 1, 1)

        self.checkBox_s_temp = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_temp.setObjectName(u"checkBox_s_temp")

        self.gridLayout.addWidget(self.checkBox_s_temp, 11, 3, 1, 1)

        self.checkBox_hdop = QCheckBox(self.gridLayoutWidget)
        self.checkBox_hdop.setObjectName(u"checkBox_hdop")

        self.gridLayout.addWidget(self.checkBox_hdop, 14, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 13, 0, 1, 1)

        self.checkBox_humidity = QCheckBox(self.gridLayoutWidget)
        self.checkBox_humidity.setObjectName(u"checkBox_humidity")

        self.gridLayout.addWidget(self.checkBox_humidity, 13, 2, 1, 1)

        self.checkBox_tws = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tws.setObjectName(u"checkBox_tws")

        self.gridLayout.addWidget(self.checkBox_tws, 9, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setToolTipDuration(2000)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.lineEdit_datetime = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_datetime.setObjectName(u"lineEdit_datetime")

        self.gridLayout.addWidget(self.lineEdit_datetime, 1, 1, 1, 1)

        self.checkBox_log = QCheckBox(self.gridLayoutWidget)
        self.checkBox_log.setObjectName(u"checkBox_log")
        self.checkBox_log.setIconSize(QSize(16, 16))
        self.checkBox_log.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_log, 3, 2, 1, 1)

        self.checkBox_heading = QCheckBox(self.gridLayoutWidget)
        self.checkBox_heading.setObjectName(u"checkBox_heading")

        self.gridLayout.addWidget(self.checkBox_heading, 7, 2, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)

        self.lineEdit_heading = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_heading.setObjectName(u"lineEdit_heading")

        self.gridLayout.addWidget(self.lineEdit_heading, 7, 1, 1, 1)

        self.lineEdit_tws = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_tws.setObjectName(u"lineEdit_tws")

        self.gridLayout.addWidget(self.lineEdit_tws, 9, 1, 1, 1)

        self.lineEdit_twd = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_twd.setObjectName(u"lineEdit_twd")

        self.gridLayout.addWidget(self.lineEdit_twd, 10, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 12, 0, 1, 1)

        self.lineEdit_humidity = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_humidity.setObjectName(u"lineEdit_humidity")

        self.gridLayout.addWidget(self.lineEdit_humidity, 13, 1, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setToolTipDuration(2000)

        self.gridLayout.addWidget(self.label_34, 0, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 11, 0, 1, 1)

        self.checkBox_stw = QCheckBox(self.gridLayoutWidget)
        self.checkBox_stw.setObjectName(u"checkBox_stw")

        self.gridLayout.addWidget(self.checkBox_stw, 8, 2, 1, 1)

        self.checkBox_twd = QCheckBox(self.gridLayoutWidget)
        self.checkBox_twd.setObjectName(u"checkBox_twd")

        self.gridLayout.addWidget(self.checkBox_twd, 10, 2, 1, 1)

        self.checkBox_s_twd = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_twd.setObjectName(u"checkBox_s_twd")

        self.gridLayout.addWidget(self.checkBox_s_twd, 10, 3, 1, 1)

        self.checkBox_s_cog = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_cog.setObjectName(u"checkBox_s_cog")

        self.gridLayout.addWidget(self.checkBox_s_cog, 6, 3, 1, 1)

        self.lineEdit_fix = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_fix.setObjectName(u"lineEdit_fix")

        self.gridLayout.addWidget(self.lineEdit_fix, 15, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout.addWidget(self.label_35, 0, 4, 1, 1)

        self.checkBox_s_seastate = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_seastate.setObjectName(u"checkBox_s_seastate")

        self.gridLayout.addWidget(self.checkBox_s_seastate, 1, 4, 1, 1)

        self.checkBox_s_cloud = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_cloud.setObjectName(u"checkBox_s_cloud")

        self.gridLayout.addWidget(self.checkBox_s_cloud, 2, 4, 1, 1)

        self.checkBox_s_crew = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_crew.setObjectName(u"checkBox_s_crew")
        sizePolicy1.setHeightForWidth(self.checkBox_s_crew.sizePolicy().hasHeightForWidth())
        self.checkBox_s_crew.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.checkBox_s_crew, 4, 4, 1, 1)

        self.checkBox_s_visibility = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_visibility.setObjectName(u"checkBox_s_visibility")

        self.gridLayout.addWidget(self.checkBox_s_visibility, 3, 4, 1, 1)

        self.checkBox_s_text = QCheckBox(self.gridLayoutWidget)
        self.checkBox_s_text.setObjectName(u"checkBox_s_text")

        self.gridLayout.addWidget(self.checkBox_s_text, 5, 4, 1, 1)

        self.tabWidget.addTab(self.tab_SKkeys, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(DialogSettings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogSettings)
        self.buttonBox.accepted.connect(DialogSettings.accept)
        self.buttonBox.rejected.connect(DialogSettings.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogSettings)
    # setupUi

    def retranslateUi(self, DialogSettings):
        DialogSettings.setWindowTitle(QCoreApplication.translate("DialogSettings", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("DialogSettings", u"Track frequency (min):", None))
#if QT_CONFIG(tooltip)
        self.checkBox_autoentry.setToolTip(QCoreApplication.translate("DialogSettings", u"Enable autoentrys at startup", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_autoentry.setText(QCoreApplication.translate("DialogSettings", u"Enable autoentrys ", None))
        self.label_25.setText(QCoreApplication.translate("DialogSettings", u"LOA:", None))
        self.label_27.setText(QCoreApplication.translate("DialogSettings", u"Air Hight", None))
        self.label_19.setText(QCoreApplication.translate("DialogSettings", u"Name:", None))
        self.label_21.setText(QCoreApplication.translate("DialogSettings", u"Settings:", None))
        self.label_30.setText(QCoreApplication.translate("DialogSettings", u"Static Boatdata:", None))
#if QT_CONFIG(tooltip)
        self.checkBox_evententrys.setToolTip(QCoreApplication.translate("DialogSettings", u"Enable tracking at startup", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_evententrys.setText(QCoreApplication.translate("DialogSettings", u"Enable event entrys", None))
        self.label_29.setText(QCoreApplication.translate("DialogSettings", u"Entry frequency (hours):", None))
        self.label_20.setText(QCoreApplication.translate("DialogSettings", u"Call Sign:", None))
        self.label_24.setText(QCoreApplication.translate("DialogSettings", u"MMSI:", None))
        self.label_26.setText(QCoreApplication.translate("DialogSettings", u"Draft:", None))
        self.label_32.setText(QCoreApplication.translate("DialogSettings", u"Server timeout (s):", None))
        self.label_28.setText(QCoreApplication.translate("DialogSettings", u"Beam:", None))
#if QT_CONFIG(tooltip)
        self.spinBox_update_interv.setToolTip(QCoreApplication.translate("DialogSettings", u"<html><head/><body><p>This is multibles of hours of the day, not a real interval.</p><p>recomended values are 1, 2, 3, 4, 6, 8, 12 and 24</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("DialogSettings", u"QPlog directory path:", None))
        self.qplPathButton.setText(QCoreApplication.translate("DialogSettings", u"...", None))
        self.sklPathButton.setText(QCoreApplication.translate("DialogSettings", u"...", None))
        self.label_23.setText(QCoreApplication.translate("DialogSettings", u"SK log directory path", None))
        self.label_33.setText(QCoreApplication.translate("DialogSettings", u"SK server adress:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_generel), QCoreApplication.translate("DialogSettings", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("DialogSettings", u"HDOP:", None))
        self.checkBox_sog.setText("")
        self.checkBox_airpressure.setText("")
        self.label_16.setText(QCoreApplication.translate("DialogSettings", u"Engine hours:", None))
        self.label_7.setText(QCoreApplication.translate("DialogSettings", u"Function", None))
        self.checkBox_s_airpressure.setText("")
        self.label_11.setText(QCoreApplication.translate("DialogSettings", u"Speed through water:", None))
        self.checkBox_s_log.setText("")
        self.checkBox_s_sog.setText("")
        self.checkBox_s_stw.setText("")
        self.checkBox_s_hdop.setText("")
        self.label_6.setText(QCoreApplication.translate("DialogSettings", u"Fix Type:", None))
        self.checkBox_fix.setText("")
        self.label_15.setText(QCoreApplication.translate("DialogSettings", u"Log:", None))
        self.checkBox_s_fix.setText("")
        self.label_13.setText(QCoreApplication.translate("DialogSettings", u"Date Time:", None))
        self.checkBox_engine.setText("")
        self.checkBox_s_engine.setText("")
        self.checkBox_cog.setText("")
        self.checkBox_temp.setText("")
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("DialogSettings", u"Values to be recorded from SK server", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("DialogSettings", u"active", None))
        self.checkBox_s_heading.setText("")
        self.label.setText(QCoreApplication.translate("DialogSettings", u"True Wind Direcion:", None))
        self.label_12.setText(QCoreApplication.translate("DialogSettings", u"True Wind Speed:", None))
        self.checkBox_s_humidity.setText("")
        self.checkBox_s_tws.setText("")
        self.label_10.setText(QCoreApplication.translate("DialogSettings", u"Heading:", None))
        self.label_17.setText(QCoreApplication.translate("DialogSettings", u"Speed over Ground:", None))
        self.checkBox_s_temp.setText("")
        self.checkBox_hdop.setText("")
        self.label_4.setText(QCoreApplication.translate("DialogSettings", u"Air humidity:", None))
        self.checkBox_humidity.setText("")
        self.checkBox_tws.setText("")
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("DialogSettings", u"The SK server path for the current Value", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("DialogSettings", u"Signal K Path", None))
        self.checkBox_log.setText("")
        self.checkBox_heading.setText("")
        self.label_14.setText(QCoreApplication.translate("DialogSettings", u"Position:", None))
        self.label_18.setText(QCoreApplication.translate("DialogSettings", u"Course over Ground:", None))
        self.label_3.setText(QCoreApplication.translate("DialogSettings", u"Air pressure:", None))
#if QT_CONFIG(tooltip)
        self.label_34.setToolTip(QCoreApplication.translate("DialogSettings", u"Values to show in logbook", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("DialogSettings", u"show", None))
        self.label_2.setText(QCoreApplication.translate("DialogSettings", u"Air temperature:", None))
        self.checkBox_stw.setText("")
        self.checkBox_twd.setText("")
        self.checkBox_s_twd.setText("")
        self.checkBox_s_cog.setText("")
        self.label_35.setText(QCoreApplication.translate("DialogSettings", u"Others", None))
        self.checkBox_s_seastate.setText(QCoreApplication.translate("DialogSettings", u"Sea State", None))
        self.checkBox_s_cloud.setText(QCoreApplication.translate("DialogSettings", u"Cloud cover", None))
        self.checkBox_s_crew.setText(QCoreApplication.translate("DialogSettings", u"Crew", None))
        self.checkBox_s_visibility.setText(QCoreApplication.translate("DialogSettings", u"Visibility", None))
        self.checkBox_s_text.setText(QCoreApplication.translate("DialogSettings", u"Text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SKkeys), QCoreApplication.translate("DialogSettings", u"Signal K Paths", None))
    # retranslateUi

