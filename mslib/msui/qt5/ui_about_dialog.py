# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutMSUIDialog(object):
    def setupUi(self, AboutMSUIDialog):
        AboutMSUIDialog.setObjectName("AboutMSUIDialog")
        AboutMSUIDialog.resize(1052, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutMSUIDialog.sizePolicy().hasHeightForWidth())
        AboutMSUIDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutMSUIDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblDummy = QtWidgets.QLabel(AboutMSUIDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDummy.sizePolicy().hasHeightForWidth())
        self.lblDummy.setSizePolicy(sizePolicy)
        self.lblDummy.setMinimumSize(QtCore.QSize(100, 40))
        self.lblDummy.setMaximumSize(QtCore.QSize(100, 40))
        self.lblDummy.setText("")
        self.lblDummy.setObjectName("lblDummy")
        self.horizontalLayout_3.addWidget(self.lblDummy)
        self.lblName = QtWidgets.QLabel(AboutMSUIDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblName.sizePolicy().hasHeightForWidth())
        self.lblName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblName.setFont(font)
        self.lblName.setTextFormat(QtCore.Qt.PlainText)
        self.lblName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.horizontalLayout_3.addWidget(self.lblName)
        self.lblPython = QtWidgets.QLabel(AboutMSUIDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPython.sizePolicy().hasHeightForWidth())
        self.lblPython.setSizePolicy(sizePolicy)
        self.lblPython.setMinimumSize(QtCore.QSize(100, 40))
        self.lblPython.setMaximumSize(QtCore.QSize(100, 40))
        self.lblPython.setObjectName("lblPython")
        self.horizontalLayout_3.addWidget(self.lblPython)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.textBrowser = QtWidgets.QTextBrowser(AboutMSUIDialog)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser.setMaximumSize(QtCore.QSize(1310, 300))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblVersion = QtWidgets.QLabel(AboutMSUIDialog)
        self.lblVersion.setObjectName("lblVersion")
        self.horizontalLayout_2.addWidget(self.lblVersion)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lblChanges = QtWidgets.QLabel(AboutMSUIDialog)
        self.lblChanges.setOpenExternalLinks(True)
        self.lblChanges.setObjectName("lblChanges")
        self.horizontalLayout_2.addWidget(self.lblChanges)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.lblLicense = QtWidgets.QLabel(AboutMSUIDialog)
        self.lblLicense.setObjectName("lblLicense")
        self.verticalLayout_2.addWidget(self.lblLicense)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.lblCopyright = QtWidgets.QLabel(AboutMSUIDialog)
        self.lblCopyright.setObjectName("lblCopyright")
        self.verticalLayout_2.addWidget(self.lblCopyright)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem4)
        self.lblLinks = QtWidgets.QLabel(AboutMSUIDialog)
        self.lblLinks.setOpenExternalLinks(True)
        self.lblLinks.setObjectName("lblLinks")
        self.verticalLayout_2.addWidget(self.lblLinks)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btOK = QtWidgets.QPushButton(AboutMSUIDialog)
        self.btOK.setObjectName("btOK")
        self.horizontalLayout.addWidget(self.btOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(AboutMSUIDialog)
        self.btOK.clicked.connect(AboutMSUIDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutMSUIDialog)

    def retranslateUi(self, AboutMSUIDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutMSUIDialog.setWindowTitle(_translate("AboutMSUIDialog", "About MSUI"))
        self.lblName.setText(_translate("AboutMSUIDialog", "Mission Support System User Interface"))
        self.lblPython.setText(_translate("AboutMSUIDialog", "Python Powered"))
        self.textBrowser.setHtml(_translate("AboutMSUIDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">Please read the reference documentation:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">Bauer, R., Grooß, J.-U., Ungermann, J., Bär, M., Geldenhuys, M., and Hoffmann, L.: The Mission Support</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">System (MSS v7.0.4) and its use in planning for the SouthTRAC aircraft campaign, Geosci.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">Model Dev., 15, 8983–8997, https://doi.org/10.5194/gmd-15-8983-2022, 2022.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">Rautenhaus, M., Bauer, G., and Doernbrack, A.: A web service based tool to plan</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">atmospheric research flights, Geosci. Model Dev., 5,55-71, https://doi.org/10.5194/gmd-5-55-2012, 2012.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">and the paper\'s Supplement (which includes a tutorial) before using the application. The documents are available at:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\"> * http://www.geosci-model-dev.net/5/55/2012/gmd-5-55-2012.pdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\"> * http://www.geosci-model-dev.net/5/55/2012/gmd-5-55-2012-supplement.pdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\"> When using this software, please be so kind and acknowledge its use by citing the above mentioned reference documentation in publications, presentations, reports, etc. that you create. Thank you very much.</span></p></body></html>"))
        self.lblVersion.setText(_translate("AboutMSUIDialog", "Version: --VERSION--"))
        self.lblChanges.setText(_translate("AboutMSUIDialog", "Changes:  --CHANGES--"))
        self.lblLicense.setText(_translate("AboutMSUIDialog", "License: Apache License Version 2.0"))
        self.lblCopyright.setText(_translate("AboutMSUIDialog", "Copyright 2008-2014: Deutsches Zentrum fuer Luft- und Raumfahrt e.V.\n"
"Copyright 2011-2014: Marc Rautenhaus\n"
"Copyright 2016-2023: by the MSS team, see AUTHORS"))
        self.lblLinks.setText(_translate("AboutMSUIDialog", "<html><head/><body><p>See <a href=\"http://mss.rtfd.io\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mss.rtfd.io</span></a> for detailed information and documentation.<br>Report bugs or feature requests at <a href=\"https://github.com/Open-MSS/MSS\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Open-MSS/MSS</span></a>.</p></body></html>"))
        self.btOK.setText(_translate("AboutMSUIDialog", "Ok"))