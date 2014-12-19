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
#写成远程便于部署，过期的时候不用到服务器上停止脚本在修改重新运行
def get_token():
    req = 'http://www.hust.cc/sina_token.php'
    ACCESS_TOKEN = urllib2.urlopen(req,timeout=60).read()
    #print weather.encode('utf-8')
    return ACCESS_TOKEN
#分享图片
def get_share_img():
    req = 'http://www.hust.cc/share_img.php'
    img_name = urllib2.urlopen(req,timeout=60).read()
    return img_name

#白云黄鹤十大
def get_byhh_top10(n):
    req = 'http://www.hust.cc/byhh_spider.php?n=' + str(n)
    byhh = urllib2.urlopen(req,timeout=60).read()
    #print weather.encode('utf-8')
    return byhh
    
#pm2.5#天气
def get_weather(city_name):
    req = 'http://www.pm25.in/api/querys/pm2_5.json?token=GhVUF6xyb7g6CuJz27ZF&stations=no&city=' + city_name
    pm_str = urllib2.urlopen(req, timeout=60).read()
    pm_str = unicode(pm_str, "utf-8")
    pm_json = json.loads(pm_str)
    if type(pm_json) == dict and pm_json.has_key('error'):
        return None
    weather = '实时' + pm_json[0]['time_point'].encode("utf-8") + '整，武汉市空气质量指数(AQI)：' + str(pm_json[0]['aqi']) + '，当前PM2.5指数：' + str(pm_json[0]['pm2_5']) + '，20小时内平均PM2.5指数：' + str(pm_json[0]['pm2_5_24h']) + '，空气质量' + pm_json[0]['quality'].encode("utf-8") + '，首要污染物：' + pm_json[0]['primary_pollutant'].encode("utf-8")
    return '#武汉PM2.5# ' + weather + ' @华中大导航网 所在城市天气 http://www.hust.cc/'

#获得心灵鸡汤句子
def get_random_setin():
    req = 'http://pomelo.sinaapp.com/batch/random_one.php'
    byhh = urllib2.urlopen(req,timeout=60).read()
    #print weather.encode('utf-8')
    return byhh

#发表微博    
def post_weibo(content, img_name):
    if content:
        filename = r'/alidata/batch/images/' + img_name
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

#nohup python thisfile， then sync app to ftp    
if __name__ == "__main__":
    while(True):
        try:
            #setin
            post_weibo(get_random_setin(), get_share_img())
            time.sleep(60*60*1.5)
            print 'post setin success'
            #byhh
            post_weibo(get_byhh_top10(4), get_share_img())
            time.sleep(60*60*1.5)
            print 'post byhh success'
            #setin
            post_weibo(get_random_setin(), get_share_img())
            time.sleep(60*60*1.5)
            print 'post setin success'
            #weather
            post_weibo(get_weather('%E6%AD%A6%E6%B1%89'), get_share_img())
            print 'post weather success'
        except Exception,ex:  
            print ex
        time.sleep(60*60*1.5)


