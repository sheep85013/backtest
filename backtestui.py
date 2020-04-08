from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 879)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditEndDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEndDate.setObjectName("lineEditEndDate")
        self.gridLayout.addWidget(self.lineEditEndDate, 10, 4, 1, 1)
        self.calendarWidgetEndDate = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidgetEndDate.setObjectName("calendarWidgetEndDate")
        self.gridLayout.addWidget(self.calendarWidgetEndDate, 7, 3, 3, 2)
        self.labelEndDate = QtWidgets.QLabel(self.centralwidget)
        self.labelEndDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelEndDate.setObjectName("labelEndDate")
        self.gridLayout.addWidget(self.labelEndDate, 10, 3, 1, 1)
        self.checkBoxAllNews = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAllNews.setChecked(True)
        self.checkBoxAllNews.setObjectName("checkBoxAllNews")
        self.gridLayout.addWidget(self.checkBoxAllNews, 3, 1, 1, 1)
        self.labelEmpID = QtWidgets.QLabel(self.centralwidget)
        self.labelEmpID.setObjectName("labelEmpID")
        self.gridLayout.addWidget(self.labelEmpID, 0, 0, 1, 1)
        self.labelInFilePth = QtWidgets.QLabel(self.centralwidget)
        self.labelInFilePth.setObjectName("labelInFilePth")
        self.gridLayout.addWidget(self.labelInFilePth, 2, 0, 1, 1)
        #self.labelProxyIDPW = QtWidgets.QLabel(self.centralwidget)
        #self.labelProxyIDPW.setObjectName("labelProxyIDPW")
        #self.gridLayout.addWidget(self.labelProxyIDPW, 1, 0, 1, 1)
        #self.labelProxyPW = QtWidgets.QLabel(self.centralwidget)
        #self.labelProxyPW.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        #self.labelProxyPW.setObjectName("labelProxyPW")
        #self.gridLayout.addWidget(self.labelProxyPW, 1, 3, 1, 1)
        self.pushButtonInFileCho = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInFileCho.setObjectName("pushButtonInFileCho")
        self.gridLayout.addWidget(self.pushButtonInFileCho, 2, 5, 1, 1)
        #self.lineEditProxyPW = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEditProxyPW.setObjectName("lineEditProxyPW")
        #self.gridLayout.addWidget(self.lineEditProxyPW, 1, 4, 1, 1)
        
        self.lineEditInFilePth = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInFilePth.setText("")
        self.lineEditInFilePth.setObjectName("lineEditInFilePth")
        self.gridLayout.addWidget(self.lineEditInFilePth, 2, 1, 1, 4)
        #self.lineEditProxyID = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEditProxyID.setObjectName("lineEditProxyID")
        #self.gridLayout.addWidget(self.lineEditProxyID, 1, 2, 1, 1)

        self.lineEditEmpID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmpID.setObjectName("lineEditEmpID")
        self.gridLayout.addWidget(self.lineEditEmpID, 0, 1, 1, 5)
       #self.labelProxyID = QtWidgets.QLabel(self.centralwidget)
        #self.labelProxyID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        #self.labelProxyID.setObjectName("labelProxyID")
        #self.gridLayout.addWidget(self.labelProxyID, 1, 1, 1, 1)
        self.labelMsg = QtWidgets.QLabel(self.centralwidget)
        self.labelMsg.setObjectName("labelMsg")
        self.gridLayout.addWidget(self.labelMsg, 12, 0, 1, 1)
        self.radioButtonSourceCodeChoY = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonSourceCodeChoY.setChecked(True)
        self.radioButtonSourceCodeChoY.setObjectName("radioButtonSourceCodeChoY")
        self.gridLayout.addWidget(self.radioButtonSourceCodeChoY, 4, 1, 1, 1)
        self.labelKeyCht = QtWidgets.QLabel(self.centralwidget)
        self.labelKeyCht.setObjectName("labelKeyCht")
        self.gridLayout.addWidget(self.labelKeyCht, 5, 1, 1, 1)
        self.checkBoxSiteCountry = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxSiteCountry.setChecked(True)
        self.checkBoxSiteCountry.setObjectName("checkBoxSiteCountry")
        self.gridLayout.addWidget(self.checkBoxSiteCountry, 3, 5, 1, 1)
        self.checkBoxAllCountry = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAllCountry.setChecked(True)
        self.checkBoxAllCountry.setObjectName("checkBoxAllCountry")
        self.gridLayout.addWidget(self.checkBoxAllCountry, 3, 3, 1, 1)
        self.labelSourceCodeCho = QtWidgets.QLabel(self.centralwidget)
        self.labelSourceCodeCho.setObjectName("labelSourceCodeCho")
        self.gridLayout.addWidget(self.labelSourceCodeCho, 4, 0, 1, 1)
        self.radioButtonSourceCodeChoN = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonSourceCodeChoN.setChecked(False)
        self.radioButtonSourceCodeChoN.setObjectName("radioButtonSourceCodeChoN")
        self.gridLayout.addWidget(self.radioButtonSourceCodeChoN, 4, 3, 1, 1)
        self.labelCountryEng = QtWidgets.QLabel(self.centralwidget)
        self.labelCountryEng.setObjectName("labelCountryEng")
        self.gridLayout.addWidget(self.labelCountryEng, 5, 3, 1, 1)
        self.labelKeyEng = QtWidgets.QLabel(self.centralwidget)
        self.labelKeyEng.setObjectName("labelKeyEng")
        self.gridLayout.addWidget(self.labelKeyEng, 5, 0, 1, 1)
        self.plainTextEditKeyCht = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditKeyCht.setEnabled(True)
        self.plainTextEditKeyCht.setReadOnly(True)
        self.plainTextEditKeyCht.setObjectName("plainTextEditKeyCht")
        self.gridLayout.addWidget(self.plainTextEditKeyCht, 6, 1, 1, 2)
        self.plainTextEditKeyEng = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditKeyEng.setEnabled(True)
        self.plainTextEditKeyEng.setReadOnly(True)
        self.plainTextEditKeyEng.setObjectName("plainTextEditKeyEng")
        self.gridLayout.addWidget(self.plainTextEditKeyEng, 6, 0, 1, 1)
        self.plainTextEditCountryCht = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditCountryCht.setEnabled(True)
        self.plainTextEditCountryCht.setReadOnly(True)
        self.plainTextEditCountryCht.setObjectName("plainTextEditCountryCht")
        self.gridLayout.addWidget(self.plainTextEditCountryCht, 6, 5, 1, 1)
        self.labelDateRange = QtWidgets.QLabel(self.centralwidget)
        self.labelDateRange.setObjectName("labelDateRange")
        self.gridLayout.addWidget(self.labelDateRange, 7, 0, 1, 1)
        self.calendarWidgetStartDate = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidgetStartDate.setObjectName("calendarWidgetStartDate")
        self.gridLayout.addWidget(self.calendarWidgetStartDate, 7, 1, 3, 2)
        self.labelStartDate = QtWidgets.QLabel(self.centralwidget)
        self.labelStartDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStartDate.setObjectName("labelStartDate")
        self.gridLayout.addWidget(self.labelStartDate, 10, 1, 1, 1)
        self.lineEditStartDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStartDate.setObjectName("lineEditStartDate")
        self.gridLayout.addWidget(self.lineEditStartDate, 10, 2, 1, 1)
        self.labelOutPath = QtWidgets.QLabel(self.centralwidget)
        self.labelOutPath.setObjectName("labelOutPath")
        self.gridLayout.addWidget(self.labelOutPath, 11, 0, 1, 1)
        self.lineEditOutPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOutPath.setText("")
        self.lineEditOutPath.setObjectName("lineEditOutPath")
        self.gridLayout.addWidget(self.lineEditOutPath, 11, 1, 1, 3)
        self.pushButtonBegin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBegin.setObjectName("pushButtonBegin")
        self.gridLayout.addWidget(self.pushButtonBegin, 12, 1, 1, 4)
        self.plainTextEditMsg = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditMsg.setReadOnly(True)
        self.plainTextEditMsg.setObjectName("plainTextEditMsg")
        self.gridLayout.addWidget(self.plainTextEditMsg, 13, 0, 1, 6)
        self.pushButtonOutFileCho = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOutFileCho.setObjectName("pushButtonOutFileCho")
        self.gridLayout.addWidget(self.pushButtonOutFileCho, 11, 4, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 12, 5, 1, 1)
        self.labelOutCho = QtWidgets.QLabel(self.centralwidget)
        self.labelOutCho.setObjectName("labelOutCho")
        self.gridLayout.addWidget(self.labelOutCho, 3, 0, 1, 1)
        self.labelCountryCht = QtWidgets.QLabel(self.centralwidget)
        self.labelCountryCht.setObjectName("labelCountryCht")
        self.gridLayout.addWidget(self.labelCountryCht, 5, 5, 1, 1)
        self.plainTextEditCountryEng = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditCountryEng.setEnabled(True)
        self.plainTextEditCountryEng.setReadOnly(True)
        self.plainTextEditCountryEng.setObjectName("plainTextEditCountryEng")
        self.gridLayout.addWidget(self.plainTextEditCountryEng, 6, 3, 1, 2)
        self.checkBoxNoDateRange = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxNoDateRange.setObjectName("checkBoxNoDateRange")
        self.gridLayout.addWidget(self.checkBoxNoDateRange, 8, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "新聞爬蟲"))
        self.labelEndDate.setText(_translate("MainWindow", "結束日"))
        self.checkBoxAllNews.setText(_translate("MainWindow", "負面新聞全網路搜尋"))
        self.labelEmpID.setText(_translate("MainWindow", "輸入員工編號:"))
        self.labelInFilePth.setText(_translate("MainWindow", "輸入檔案路徑:"))
        #self.labelProxyIDPW.setText(_translate("MainWindow", "代理伺服器帳號密碼:"))
        #self.labelProxyPW.setText(_translate("MainWindow", "密碼"))
        self.pushButtonInFileCho.setText(_translate("MainWindow", "選擇檔案"))
        #self.labelProxyID.setText(_translate("MainWindow", "帳號"))
        self.labelMsg.setText(_translate("MainWindow", "訊息:"))
        self.radioButtonSourceCodeChoY.setText(_translate("MainWindow", "是"))
        self.labelKeyCht.setText(_translate("MainWindow", "中文關鍵字表:"))
        self.checkBoxSiteCountry.setText(_translate("MainWindow", "制裁國家官網搜尋"))
        self.checkBoxAllCountry.setText(_translate("MainWindow", "制裁國家全網路搜尋"))
        self.labelSourceCodeCho.setText(_translate("MainWindow", "是否需要完整source code:"))
        self.radioButtonSourceCodeChoN.setText(_translate("MainWindow", "否"))
        self.labelCountryEng.setText(_translate("MainWindow", "英文國家列表:"))
        self.labelKeyEng.setText(_translate("MainWindow", "英文關鍵字表:"))
        self.plainTextEditKeyCht.setPlainText(_translate("MainWindow", "洗錢\n"
"內線交易\n"
"操縱市場\n"
"違反\n"
"逃稅\n"
"逃漏稅\n"
"收賄\n"
"行賄\n"
"貪污\n"
"罪犯\n"
"犯罪\n"
"詐欺\n"
"詐騙\n"
"違法\n"
"非法\n"
"裁罰\n"
"恐怖分子\n"
"走私\n"
"偷運\n"
"勒索\n"
"敲詐\n"
"組織犯罪\n"
"侵占\n"
"盜用"))
        self.plainTextEditKeyEng.setPlainText(_translate("MainWindow", "money laundering\n"
"market abuse\n"
"market manipulation\n"
"insider trading\n"
"regulatory breach\n"
"tax evasion\n"
"bribery\n"
"corruption\n"
"criminal\n"
"fraud\n"
"illegal\n"
"penalty\n"
"terrorist\n"
"trafficking\n"
"smuggling\n"
"extortion\n"
"racketeering\n"
"organised crime\n"
"embezzle"))
        self.plainTextEditCountryCht.setPlainText(_translate("MainWindow", "伊朗\n"
"古巴\n"
"北韓\n"
"朝鮮民主主義人民共和國\n"
"敘利亞\n"
"克里米亞\n"
"塞瓦斯托波爾\n"
"蘇丹\n"
"南蘇丹\n"
"俄羅斯"))
        self.labelDateRange.setText(_translate("MainWindow", "日期範圍:"))
        self.labelStartDate.setText(_translate("MainWindow", "起始日"))
        self.labelOutPath.setText(_translate("MainWindow", "輸出路徑:"))
        self.pushButtonBegin.setText(_translate("MainWindow", "開始"))
        self.pushButtonOutFileCho.setText(_translate("MainWindow", "選擇資料夾"))
        self.pushButtonCancel.setText(_translate("MainWindow", "停止"))
        self.labelOutCho.setText(_translate("MainWindow", "選擇輸出結果:"))
        self.labelCountryCht.setText(_translate("MainWindow", "中文國家列表"))
        self.plainTextEditCountryEng.setPlainText(_translate("MainWindow", "Cuba\n"
"Iran\n"
"North Korea\n"
"DPRK\n"
"Democratic People\'s Republic of Korea\n"
"Syria\n"
"Crimea\n"
"Sevastopol\n"
"Russia\n"
"Ukraine\n"
"Sudan"))
        self.checkBoxNoDateRange.setText(_translate("MainWindow", "不限日期範圍"))

