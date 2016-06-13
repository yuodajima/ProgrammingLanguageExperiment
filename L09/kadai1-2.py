#!/usr/bin/python
# coding: UTF-8

import urllib
import json

city = 130010
day_to_num = {'today' : 0, 'tomorrow' : 1}


def Forecast(city_code, day='today'):
    src = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%d'
    f = urllib.urlopen( src % (city_code) ) # % 表記使って src の %d を指定する
    q = json.loads( f.read() )
    f.close()

    print q['title']
    print q['location']['city']
    print q['forecasts'][day_to_num[day]]['date'], ': ', q['forecasts'][day_to_num[day]]['telop']
    print '-----'

Forecast(city)

Forecast(city, "tomorrow")

# 実行結果                        
# 東京都 東京 の天気
# 東京
# 2016-06-13 :  雨のち曇
# -----
# 東京都 東京 の天気
# 東京
# 2016-06-14 :  曇時々晴
# -----
