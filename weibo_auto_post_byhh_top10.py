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

def get_share_img():
    req = 'http://www.hust.cc/share_img.php'
    img = urllib2.urlopen(req,timeout=60).read()
    #print weather.encode('utf-8')
    return img

def get_byhh_top10(n):
    req = 'http://www.hust.cc/byhh_spider.php?n=' + str(n)
    byhh = urllib2.urlopen(req,timeout=60).read()
    #print weather.encode('utf-8')
    return byhh

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
#3.5h 之后执行，正好8点半
time.sleep(3.5 * 60 * 60)
while True:
    try:
        print get_token()
        #print get_byhh_top10(3)
        #print get_share_img()
        post_weibo(get_byhh_top10(3))
        print 'post success'
    except Exception,ex:  
        print ex
    #6h检查一次
    time.sleep(60*60*6)

