# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:11:04 2017
1.自Google finance抓取台股日資料(任意期間)
2.存入EXCEL檔案
@author: 林萍珍
"""
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import datetime
import os.path
import pymysql.cursors
import xlrd
from pandas_datareader import data as pdr
import yfinance as yf

class GetYahooFinance():
    def __init__(self,stkno,startdate,enddate,refresh=True):
        #string to datetime
        if(isinstance(startdate, str) == True or isinstance(enddate, str) == True):
            startdate=datetime.datetime.strptime(startdate,'%Y-%m-%d')
            enddate=datetime.datetime.strptime(enddate,'%Y-%m-%d')
        self.sdate=startdate
        self.edate=enddate
        #datetime to string
        S_date=datetime.datetime.strftime(startdate,'%Y%m%d')
        E_date=datetime.datetime.strftime(enddate,'%Y%m%d')
        self.fn=str(stkno)+'_'+S_date+'_'+E_date+'.xlsx'
        self.stkno=stkno
        self.refresh=refresh     
    def savetoexcel(self,data,sheetname):
        '''
        若資料不存在，則不寫入檔案
        '''
        if   len(data) != 0:
            writer=pd.ExcelWriter(self.fn)
            data.to_excel(writer,sheetname,index=False)
            writer.save()

    def getstock(self,asc=False):
        if not self.refresh and os.path.exists(self.fn):    #不重置 &檔案已存在
            Data=pd.read_excel(self.fn)
            Data[['open','high','low','close','volume']]=\
            Data[['open','high','low','close','volume']].astype(float)
            Data[['dates']]=Data[['dates']].astype(object)
        else:
            try:
                yf.pdr_override() # <== that's all it takes :-)
                Data = pdr.get_data_yahoo(self.stkno+'.tw',self.sdate,self.edate)
                del Data['Adj Close']
                Data = Data.reset_index()
                print(Data)
            except Exception as err:
                print(err)
            if  len(Data)   != 0:        #有取得資料才進行轉換
                Data.columns=['dates','open','high','low','close','volume']
                Data[['open','high','low','close','volume']]=\
                Data[['open','high','low','close','volume']].astype(float)

                if asc==True:
                    Data=Data.sort_values(by=['dates'],ascending=True)
        return Data
    def excel_to_db(self,data,sheetname):
        #若資料不存在，則不匯進資料庫
        if   len(data) != 0:
            #連線MySQL
            connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = 'tfis20160929',
                                 db = 'mydatabase',
                                 charset = 'utf8mb4')
            try:
                with connection.cursor() as cursor:

                    #去除副檔名 .xlsx
                    #check_table_name = self.fn[:-5]
                    delete_msg = ''                    
                    #取股票名
                    table_name = 'stock_'+self.fn[:4]
                    #判斷資料表是否已存在
                    table_exist_sql = "SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA='mydatabase' AND TABLE_NAME='%s'" % (table_name)

                    # 使用execute()方法查询資料庫中表是否存在
                    exist_table=cursor.execute(table_exist_sql)
                    #如果已存在資料表
                    if exist_table == 1:
                        delete_sql = "DROP TABLE `%s`" % (table_name)
                        cursor.execute(delete_sql)
                        delete_msg = "將資料庫中已有的%s表進行刪除!<br>" % table_name
                    create_table_sql = "CREATE TABLE `mydatabase`.`"+table_name+"` (`id` INT NOT NULL AUTO_INCREMENT,`dates` DATETIME NULL,`open` VARCHAR(10) NULL,`high` VARCHAR(10) NULL,`low` VARCHAR(10) NULL,`close` VARCHAR(10) NULL,`volume` VARCHAR(20) NULL,PRIMARY KEY (`id`))"   
                    cursor.execute(create_table_sql)

                    stock_fn = xlrd.open_workbook(self.fn)
                    sheet = stock_fn.sheet_by_name(sheetname)
                    for r in range(1, sheet.nrows):
                        #第一個參數是取日期。第二個參數有兩種取值，0或者1，0是以1900-01-01為基準的日期，而1是1904-01-01為基準的日期。
                        date_value  = xlrd.xldate_as_tuple(sheet.cell(r,0).value,0)
                        #date = datetime.date(*date_value[:3]).strftime('%Y/%m/%d %H:%M:%S')  datetime
                        date = datetime.date(*date_value[:3]).strftime('%Y/%m/%d')
                        open = sheet.cell(r,1).value
                        high = sheet.cell(r,2).value
                        low = sheet.cell(r,3).value
                        close = sheet.cell(r,4).value
                        volume = sheet.cell(r,5).value
                        #print(date, open, high, low, close, volume)
                        sql_insert = "INSERT INTO `mydatabase`.`"+table_name+"` (`dates`, `open`, `high`, `low`, `close`, `volume`) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql_insert, (date, open, high, low, close, volume))
                        #沒有設置默認自動提交，需要主動提交，以保存所執行的語句
                        connection.commit()
                    return (delete_msg+"股價資料已儲存到excel中，並成功寫入進資料庫!")

            except Exception as e:
                print("Exeception occured:{}".format(e))
                return ("Error")
            finally:
                connection.close()
        else:
            return ("輸入錯誤的股票代號或是錯誤的日期")