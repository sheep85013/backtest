
#+++++++++++Setting of using PySide2 instead of PyQt5+++++++++++++++#
import sys, os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

from PySide2.QtCore import  Qt, QThread, Signal
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog

from UI import myui, mylogic
import datetime

#def trap_exc_during_debug(*args):
#    # when app raises uncaught exception, print info
#    print(args)
#
#
## install exception hook: without this, uncaught exception would cause application to exit
#sys.excepthook = trap_exc_during_debug

class QThread1(QThread):

    sig_log = Signal(object)    

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        
    def run(self):
        mylogic.beginPushed(self, input_info)
        

class MyWidget(QMainWindow, myui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self) # Initiative the UI file myui.py

        # Connect signal to slot
        self.checkBoxAllNews.stateChanged.connect(self.greyOutKeys)
        self.checkBoxAllCountry.stateChanged.connect(self.greyOutCountries)
        self.checkBoxSiteCountry.stateChanged.connect(self.greyOutCountries)
        self.checkBoxNoDateRange.stateChanged.connect(self.greyOutCalenders)
        
        self.pushButtonBegin.clicked.connect(self.pushBegin)
        self.pushButtonCancel.clicked.connect(self.pushCancel)
        self.pushButtonInFileCho.clicked.connect(self.pushInFileCho)
        self.pushButtonOutFileCho.clicked.connect(self.pushOutFileCho)
        
        self.calendarWidgetStartDate.selectionChanged.connect(self.showStartDate)
        self.calendarWidgetEndDate.selectionChanged.connect(self.showEndDate)
       
    def greyOutKeys(self):
        if self.checkBoxAllNews.isChecked():
            self.plainTextEditKeyEng.setEnabled(True)
            self.plainTextEditKeyCht.setEnabled(True)
        else:
            self.plainTextEditKeyEng.setEnabled(False)
            self.plainTextEditKeyCht.setEnabled(False)
            
    def greyOutCountries(self):            
        if self.checkBoxAllCountry.isChecked() or self.checkBoxSiteCountry.isChecked():
            self.plainTextEditCountryEng.setEnabled(True)
            self.plainTextEditCountryCht.setEnabled(True)
        else:
            self.plainTextEditCountryEng.setEnabled(False)
            self.plainTextEditCountryCht.setEnabled(False)
    
    def greyOutCalenders(self):            
        if self.checkBoxNoDateRange.isChecked():
            self.calendarWidgetStartDate.setEnabled(False)
            self.calendarWidgetEndDate.setEnabled(False)
            self.lineEditStartDate.setEnabled(False)
            self.lineEditEndDate.setEnabled(False) 
        else:
            self.calendarWidgetStartDate.setEnabled(True)
            self.calendarWidgetEndDate.setEnabled(True)
            self.lineEditStartDate.setEnabled(True)
            self.lineEditEndDate.setEnabled(True)           
    
    def pushInFileCho(self, event): # Single File
        file_, filetype = QFileDialog.getOpenFileName(None,  # 不能用Self, https://ask.csdn.net/questions/381839
                                "選取文件",  
                                "C:/",  
                                "CSV Files (*.csv);;All Files (*)")   #设置文件扩展名过滤,注意用双分号间隔
        self.lineEditInFilePth.setText(file_)
        
    def pushOutFileCho(self, event): # Folder
        dir = QFileDialog.getExistingDirectory(None,  # 不能用Self, https://ask.csdn.net/questions/381839
                                    "選取資料夾",  
                                    "C:/")                  # 起始路径
        self.lineEditOutPath.setText(dir)    
    
    def showStartDate(self):
        start_date = self.calendarWidgetStartDate.selectedDate()
        self.lineEditStartDate.setText(start_date.toString(Qt.ISODate))
        
    def showEndDate(self):
        end_date = self.calendarWidgetEndDate.selectedDate()
        self.lineEditEndDate.setText(end_date.toString(Qt.ISODate))
        
     
    def pushBegin(self):
        '''Actions when push the "Begin" buttom'''
        emp_ID = self.lineEditEmpID.text()
        proxy_id = self.lineEditProxyID.text()
        proxy_pw = self.lineEditProxyPW.text()
        csv_path = self.lineEditInFilePth.text()
        out_state = [self.checkBoxAllNews.isChecked(), 
                     self.checkBoxAllCountry.isChecked(),
                     self.checkBoxSiteCountry.isChecked()]
        need_code = self.radioButtonSourceCodeChoY.isChecked()
        cht_keywords = self.plainTextEditKeyCht.toPlainText().split('\n')
        eng_keywords = self.plainTextEditKeyEng.toPlainText().split('\n')
        cht_countries = self.plainTextEditCountryCht.toPlainText().split('\n')
        eng_countries = self.plainTextEditCountryEng.toPlainText().split('\n')
        start_date = self.lineEditStartDate.text()
        end_date = self.lineEditEndDate.text()
        no_date_range = self.checkBoxNoDateRange.isChecked()
        out_path = self.lineEditOutPath.text()
        
        global input_info
        input_info = {'emp_ID':emp_ID, # A string
                      'proxy_id':proxy_id, # A string
                      'proxy_pw':proxy_pw, # A string
                      'csv_path':csv_path, # A string
                      'out_state':out_state, # A list of True or False. ex: [True, True, False]
                      'need_code':need_code, # True or False
                      'eng_keywords':eng_keywords, # A list of keywords
                      'cht_keywords':cht_keywords, # A list of keywords
                      'eng_countries':eng_countries, # A list of countries
                      'cht_countries':cht_countries, # A list of countries
                      'start_date':start_date, # A sting of ISO date ex: '2018-10-10'
                      'end_date':end_date, # A sting of ISO date ex: '2018-10-10'
                      'no_date_range':no_date_range, # True or false
                      'out_path':out_path} # A string
        self.thread1 = QThread1()
        self.thread1.start()
        self.thread1.sig_log.connect(self.on_log)
        self.lock_UI()


    def pushCancel(self):
        '''Actions when push the "Cancel" buttom'''        
        try:
            self.thread1.terminate()
            self.on_log('你按了停止')   
            self.unlock_UI()
        except:
            pass
        
    def on_log(self, my_log):
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.plainTextEditMsg.appendPlainText(time_now+" - "+str(my_log))
            
    def lock_UI(self):
        self.pushButtonBegin.setEnabled(False)
        self.pushButtonCancel.setEnabled(True)
        self.lineEditEmpID.setEnabled(False)
        self.lineEditProxyID.setEnabled(False)
        self.lineEditProxyPW.setEnabled(False)
        self.lineEditInFilePth.setEnabled(False)
        self.lineEditOutPath.setEnabled(False)
        #self.plainTextEditKeyEng.setEnabled(False)
        #self.plainTextEditCountryCht.setEnabled(False)
        #self.plainTextEditCountryEng.setEnabled(False)
        #self.plainTextEditKeyCht.setEnabled(False)
        self.pushButtonInFileCho.setEnabled(False)
        self.pushButtonOutFileCho.setEnabled(False)
        self.radioButtonSourceCodeChoN.setEnabled(False)        
        self.checkBoxSiteCountry.setEnabled(False)
        self.radioButtonSourceCodeChoY.setEnabled(False)
        self.pushButtonOutFileCho.setEnabled(False)
        self.checkBoxAllNews.setEnabled(False)        
        self.checkBoxAllCountry.setEnabled(False)
        self.checkBoxSiteCountry.setEnabled(False)
        self.calendarWidgetStartDate.setEnabled(False)
        self.calendarWidgetEndDate.setEnabled(False)
        self.lineEditStartDate.setEnabled(False)
        self.lineEditEndDate.setEnabled(False)
        self.checkBoxNoDateRange.setEnabled(False)

    def unlock_UI(self):
        self.pushButtonBegin.setEnabled(True)
        self.pushButtonCancel.setEnabled(False) 
        self.lineEditEmpID.setEnabled(True)
        self.lineEditProxyID.setEnabled(True)
        self.lineEditProxyPW.setEnabled(True)
        self.lineEditInFilePth.setEnabled(True)
        self.lineEditOutPath.setEnabled(True)
        #self.plainTextEditKeyEng.setEnabled(True)
        #self.plainTextEditCountryCht.setEnabled(True)
        #self.plainTextEditCountryEng.setEnabled(True)
        #self.plainTextEditKeyCht.setEnabled(True)
        self.pushButtonInFileCho.setEnabled(True)
        self.pushButtonOutFileCho.setEnabled(True)
        self.radioButtonSourceCodeChoN.setEnabled(True)        
        self.checkBoxSiteCountry.setEnabled(True)
        self.radioButtonSourceCodeChoY.setEnabled(True)
        self.pushButtonOutFileCho.setEnabled(True)
        self.checkBoxAllNews.setEnabled(True)        
        self.checkBoxAllCountry.setEnabled(True)
        self.checkBoxSiteCountry.setEnabled(True)
        self.calendarWidgetStartDate.setEnabled(True)
        self.calendarWidgetEndDate.setEnabled(True)
        self.lineEditStartDate.setEnabled(True)
        self.lineEditEndDate.setEnabled(True)
        self.checkBoxNoDateRange.setEnabled(True)
        
if __name__ == "__main__":
    app = QApplication([])
    form = MyWidget()
    form.show()
    sys.exit(app.exec_())