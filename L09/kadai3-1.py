#!/usr/bin/python
# coding: UTF-8

import urllib
import json

city = 130010

class WeatherHacks:

    def __init__(self, city_code):
        src = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%d'
        f = urllib.urlopen( src % (city_code) ) # % 表記使って src の %d を指定する
        self.q = json.loads(f.read())
        f.close()
        
        
    def forecast(self):
        print self.q['title']
        print self.q['location']['city']
        for i in range(3):
            print self.q['forecasts'][i]['date'], ': ',self.q['forecasts'][i]['telop']
        print '-----'
        print self.q['description']['text']
            
        
w = WeatherHacks(city)
w.forecast()


# 実行結果
# 東京都 東京 の天気
# 東京
# 2016-06-13 :  雨のち曇
# 2016-06-14 :  曇時々晴
# 2016-06-15 :  曇時々晴
# -----
#  低気圧が東海道沖を東北東へ進んでいます。

# 【関東甲信地方】
#  関東甲信地方は、雨となっています。

#  13日は、低気圧や前線の影響により、雨で昼前は激しく降る所もありま
# すが、午後は次第に曇りとなるでしょう。

#  14日は、気圧の谷や湿った空気の影響で、曇りですが、日中は晴れる所
# が多いでしょう。

#  関東近海では、14日にかけて、うねりを伴いしけるでしょう。また、所
# 々で霧が発生しています。船舶は高波や視程障害に注意してください。

# 【東京地方】
#  13日は、雨で夕方から曇りでしょう。
#  14日は、曇りで昼前から夕方は晴れますが、夜は雨の降る所がある見込
# みです。
