#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

import os
import sys
import json
import urllib2
import time
import datetime
import urllib

SOURCE = '3142741993';
APP_KEY = '3142741993';#在新浪开放平台的app_key
ACCESS_TOKEN = '2.00ONNQpDzkcg7D62af522f70HkPVXD'#授权码，请打开下面的连接重新获取
#https://api.weibo.com/2/oauth2/authorize?client_id=3142741993&response_type=token&display=js&redirect_uri=https://api.weibo.com/oauth2/default.html

def get_weather(city_name):
    req = 'http://atool.org/apis/weather.for.api.php?q=' + city_name
    weather = urllib2.urlopen(req,timeout=60).read()
    #print weather.encode('utf-8')
    return '#武汉天气# ' + weather + ' @华中大导航网 所在城市天气 http://www.hust.cc/'

def post_weather_weibo():
    req = 'https://api.weibo.com/2/statuses/update.json'
    #http://atool.org/apis/weather.for.api.php?q=%E6%AD%A6%E6%B1%89
    post_dict = {
        'source':SOURCE,
        'access_token':ACCESS_TOKEN,
        'status':get_weather('%E6%AD%A6%E6%B1%89')
    }
    post_data = urllib.urlencode(post_dict)
    f = urllib2.urlopen(req, post_data)
    content = f.read()
    return content


print 'start auto'
while True:
    try:
        time.sleep(1)
        post_weather_weibo()
        #print get_weather('%E6%AD%A6%E6%B1%89')
        print 'post success'
    except Exception,ex:  
        print ex
    #3h检查一次
    time.sleep(60*60*3)

