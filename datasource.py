'''
這是專門取得台灣股市資料
'''
import pandas_datareader.data as pdr
import yfinance as yf
from datetime import datetime
import os
import pandas as pd

def get_stock_data(stock_id):
    '''
    @parma stock_id: 股祥代碱
    '''
    
    
    
    yf.pdr_override()
    stockid_str=f'{stock_id}.TW'
    
    current=os.path.abspath("./")
    current_date=datetime.now()
    stock_id="2303"
    filename=f"{stockid_str}_{current_date.year}_{current_date.month}_{current_date.day}.csv"
    csv_File_path=os.path.join(current,"data",filename)
    if not os.path.exists(csv_File_path):
        tw_2303 = pdr.get_data_yahoo(stockid_str)
        tw_2303.to_csv(csv_File_path)   
    else:
        print("讀取檔案")
    tw_2303=pd.read_csv(csv_File_path)
    print(tw_2303)
    # stock_list1=tw_2303.reset_index()
    # stock_list1['Date']=stock_list1['Date'].map(lambda x: x.strftime('%Y-%m-%d'))
    stock_list=tw_2303.to_numpy().tolist()
    return stock_list