华中大导航网 - 新浪微博自动化脚本
===========
这是一个为华中大导航网设计的自动发布微博，自动给关注者回复微博的Python脚本

##搭建方法：
1. 授权码获取：打开https://api.weibo.com/2/oauth2/authorize?client_id=82966982&response_type=token&display=js&redirect_uri=https://api.weibo.com/oauth2/default.html ，授权后出现一个空白页面，不要关闭，按 Ctrl+U 查看源代码，找到"access_token":"2.00tlp********"。嗯，授权码就找到了。

2.修改脚本前面定义的几个变量，python 运行即可。

##注意事项：
 1. 授权有效期如果不使用Weico.apple微博客户端一般是90天，到时记得续期。如果使用苹果客户端。建议替换苹果的APPKEY为安卓的'211160679 '。代码和授权页面都改一下。
 2. 抓取时间和发布时间，请修改脚本。
 
##实例：
 1. [http://www.hust.cc/](http://www.hust.cc/)
 2. [http://weibo.com/husterscn/](http://weibo.com/husterscn/)

