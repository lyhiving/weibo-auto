#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

import os
import sys
import json
import urllib2
import time
import datetime
import urllib
import random
import pycurl

SOURCE = '3142741993';
APP_KEY = '3142741993';#在新浪开放平台的app_key
ACCESS_TOKEN = '2.00ONNQpDzkcg7D62af522f70HkPVXD'#授权码，请打开下面的连接重新获取
#https://api.weibo.com/2/oauth2/authorize?client_id=3142741993&response_type=token&display=js&redirect_uri=https://api.weibo.com/oauth2/default.html

def get_weather(city_name):
    req = 'http://atool.org/apis/weather.for.api.php?q=' + city_name
    weather = urllib2.urlopen(req,timeout=60).read()
    #print weather.encode('utf-8')
    return '#武汉天气# ' + weather + ' @华中大导航网 所在城市天气 http://www.hust.cc/'

def post_weibo(content):
    if content:
        filename = r'/alidata/batch/images/' + str(random.randint(1, 26)) + '.png'
        print filename
        pc = pycurl.Curl()  
        pc.setopt(pycurl.POST, 1)  
        pc.setopt(pycurl.URL, 'https://api.weibo.com/2/statuses/upload.json')  
        pc.setopt(pycurl.HTTPPOST, [('pic', (pc.FORM_FILE, filename)),   
                                    ('source', (pc.FORM_CONTENTS, SOURCE)),
                                    ('access_token', (pc.FORM_CONTENTS, ACCESS_TOKEN)),
                                    ('status', (pc.FORM_CONTENTS, urllib2.quote(content)))])
        pc.perform()  
        response_code = pc.getinfo(pycurl.RESPONSE_CODE)  
        pc.close()
        return response_code
    return 'no content'


print 'start auto'
while True:
    try:
        time.sleep(1)
        post_weibo(get_weather('%E6%AD%A6%E6%B1%89'))
        #print get_weather('%E6%AD%A6%E6%B1%89')
        print 'post success'
    except Exception,ex:  
        print ex
    #3h检查一次
    time.sleep(60*60*3)

