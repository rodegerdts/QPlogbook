# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_choice.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DialogChoice(object):
    def setupUi(self, DialogChoice):
        if not DialogChoice.objectName():
            DialogChoice.setObjectName(u"DialogChoice")
        DialogChoice.resize(484, 307)
        self.verticalLayout = QVBoxLayout(DialogChoice)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_filename = QLabel(DialogChoice)
        self.label_filename.setObjectName(u"label_filename")

        self.verticalLayout.addWidget(self.label_filename)

        self.label = QLabel(DialogChoice)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(DialogChoice)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(1)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(DialogChoice)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(1)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(DialogChoice)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)
        self.label_4.setIndent(1)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(DialogChoice)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(DialogChoice)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mergeButton = QPushButton(DialogChoice)
        self.mergeButton.setObjectName(u"mergeButton")

        self.horizontalLayout.addWidget(self.mergeButton)

        self.discardButton = QPushButton(DialogChoice)
        self.discardButton.setObjectName(u"discardButton")

        self.horizontalLayout.addWidget(self.discardButton)

        self.saveasButton = QPushButton(DialogChoice)
        self.saveasButton.setObjectName(u"saveasButton")

        self.horizontalLayout.addWidget(self.saveasButton)

        self.buttonBox = QDialogButtonBox(DialogChoice)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogChoice)
        self.buttonBox.rejected.connect(DialogChoice.reject)
        self.buttonBox.accepted.connect(DialogChoice.accept)

        QMetaObject.connectSlotsByName(DialogChoice)
    # setupUi

    def retranslateUi(self, DialogChoice):
        DialogChoice.setWindowTitle(QCoreApplication.translate("DialogChoice", u"Dialog", None))
        self.label_filename.setText(QCoreApplication.translate("DialogChoice", u"Filename:", None))
        self.label.setText(QCoreApplication.translate("DialogChoice", u"This monthly file already exists with differences in the Logbook. You have the following choices:", None))
        self.label_2.setText(QCoreApplication.translate("DialogChoice", u"<html><head/><body><p>- If you want to merge the file with the currrent logbook press &quot;<span style=\" font-weight:700;\">Merge</span>&quot; Any deleted entrys will reappear.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("DialogChoice", u"<html><head/><body><p>- If you want to overwrite the file with the currrent logbook press &quot;<span style=\" font-weight:700;\">OK</span>&quot;</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("DialogChoice", u"<html><head/><body><p>- If you want to discard the changes in the currrent logbook press &quot;<span style=\" font-weight:700;\">Discard</span>&quot;</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DialogChoice", u"<html><head/><body><p>- You can also save a copy for later review. Press &quot;<span style=\" font-weight:700;\">Save Copy</span>&quot;</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("DialogChoice", u"Do you want to overwrite the existing file?", None))
        self.mergeButton.setText(QCoreApplication.translate("DialogChoice", u"Merge", None))
        self.discardButton.setText(QCoreApplication.translate("DialogChoice", u"Discard", None))
        self.saveasButton.setText(QCoreApplication.translate("DialogChoice", u"Save Copy", None))
    # retranslateUi

