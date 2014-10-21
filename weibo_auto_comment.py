#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

import os
import sys
import json
import urllib2
import time
import urllib

SOURCE = '3142741993';
APP_KEY = '3142741993';
ACCESS_TOKEN = '2.00ONNQpDzkcg7D62af522f70HkPVXD'#授权码，请打开下面的连接重新获取
#https://api.weibo.com/2/oauth2/authorize?client_id=3142741993&response_type=token&display=js&redirect_uri=https://api.weibo.com/oauth2/default.html

MAX_WEIBO_ID = 3765143533851101

def get_onepage_user(cursor):
    req = 'https://api.weibo.com/2/friendships/friends/ids.json?source={0}&access_token={1}&count=200&uid=3505855672&cursor={2}'.format(SOURCE, ACCESS_TOKEN, cursor)
    users_json = json.loads(urllib2.urlopen(req,timeout=60).read())
    user_ids = users_json['ids']
    next_page = users_json['next_cursor']
    total_user = users_json['total_number']
    return (user_ids, next_page, total_user)

def get_all_user():
    result = []
    while True:
        user_ids, next_cursor, total_user = get_onepage_user(0)
        result = result + user_ids
        if next_cursor == 0:
            continue
        else:
            break
    return result

def get_weiboid_of_userid(userid):
    '''
source	false	string	采用OAuth授权方式不需要此参数，其他授权方式为必填参数，数值为应用的AppKey。
access_token	false	string	采用OAuth授权方式为必填参数，其他授权方式不需要此参数，OAuth授权后获得。
uid	false	int64	需要查询的用户ID。
screen_name	false	string	需要查询的用户昵称。
since_id	false	int64	若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
max_id	false	int64	若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
count	false	int	单页返回的记录条数，最大不超过100，默认为20。
page	false	int	返回结果的页码，默认为1。
base_app	false	int	是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
feature	false	int	过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
'''
    req = 'https://api.weibo.com/2/statuses/user_timeline/ids.json?source={0}&access_token={1}&uid={2}&since_id={3}'.format(SOURCE, ACCESS_TOKEN, userid, 0)
    weibos_json = json.loads(urllib2.urlopen(req,timeout=60).read())
    weibo_ids = weibos_json['statuses']
    if weibo_ids:
        return weibo_ids
    return []
    
def like_weiboid(weiboid):
    data = "Accept-Encoding=gzip,deflate&attitude=smile&access_token={0}&id={1}".format(ACCESS_TOKEN,weiboid)
    rsp = urllib2.urlopen('https://api.weibo.com/2/attitudes/create.json',data=data,timeout=60) 

def get_weibo_ids():
    req = 'https://api.weibo.com/2/statuses/friends_timeline/ids.json?source={0}&access_token={1}&since_id={2}'.format(SOURCE, ACCESS_TOKEN, MAX_WEIBO_ID)
    weibos_json = json.loads(urllib2.urlopen(req,timeout=60).read())
    weibo_ids = weibos_json['statuses']
    if weibo_ids:
        return weibo_ids
    return []

def comment_weiboid(weiboid):
    req = 'https://api.weibo.com/2/comments/create.json'
    post_dict = {
        'source':SOURCE,
        'access_token':ACCESS_TOKEN,
        'comment':'华中大导航网(www.Hust.cc) 前来强势围观...',
        'id':weiboid
    }
    post_data = urllib.urlencode(post_dict)
    f = urllib2.urlopen(req, post_data)
    content = f.read()
    return content


def get_max(ids):
    max_id = 0;
    for i in ids:
        if (i > max_id):
            max_id = i
    return max_id

print 'start auto'
cnt = 0
max_id = 0
while True:
    print cnt
    cnt = cnt + 1
    weibos = []
    try:
        weibos = get_weibo_ids()
    except Exception,ex:  
        continue

    max_id = get_max(weibos)
    time.sleep(5 * 60)#延迟5分钟，防止出现400
    if (MAX_WEIBO_ID < max_id):
        MAX_WEIBO_ID = max_id
    
    for id in weibos:
        try:
            print id
            comment_weiboid(id)
            #like_weiboid(id)
            #60秒发一条评论
        except Exception,ex:
            print ex 
        time.sleep(5) #每条评论间隔5秒钟
    #60 min检查一次
    time.sleep(60 * 60)

