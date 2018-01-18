# -*- coding:utf-8 -*-
# Write By Sunwl
# 2017/10/24
#
# 模拟浏览器进入有道翻译网页，命令行输入字符，爬取网站翻译出的字符
#
# python 2.7
# 运行环境 Win，Mac
# 注意：

import urllib
import urllib2

###########
####定制化的Handler
#http_hander = urllib2.HTTPHandler()
#urllib2.build_opener(http_hander)
#request = urllib2.Request("http://fanyi.youdao.com")
###########

# 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# 完整的headers
headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    }

# 用户接口输入
key = raw_input("请输入需要翻译的文字:")

# 构造post数据
formdata = {
    "i":key,
    "from":"auto",
    "to":"auto",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1511219405946",
    "sign":"f8965f67a1d3eee8a69ddf8ccc5f582b",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
    }

# 对post的数据做urlencode转码
data = urllib.urlencode(formdata)

# 如果Request()方法里的data参数有值，那么这个请求就是POST，如果没有，就是Get
request = urllib2.Request(url, data = data, headers = headers)
html = urllib2.urlopen(request)
print (html.read().decode('utf-8'))
# resultInfo = urllib2.urlopen(request).read().decode("unicode_escape")
# jInfo = json.loads(resultInfo)
# print(jInfo['translateResult'][0])
# jsonInfo = json.load(str(urllib2.urlopen(request).read().decode('utf-8')))
# print(jsonInfo)
