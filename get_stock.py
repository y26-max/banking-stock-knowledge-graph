#coding=utf-8
import tushare as ts
import pandas as pd

# 和 Tushare 建立连接
pro = ts.pro_api('08fbab8087eb66409ec66452b756beb05ef93388bbba7905fab1f7b5')

stock_basic = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname')
stock_basic.to_csv('./data/knowledge/股票信息2.csv', encoding='gbk')