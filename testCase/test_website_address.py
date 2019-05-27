# !/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 人可以识别的路径，编码类型为utf-8，即汉语
chinaCompany = "Beijing Mingtai Yanshen Technology Co., Ltd"
testUrl = "https://www.tianyancha.com/search?key=" + chinaCompany
print("visit web:" + testUrl)

# 转化为机器可以识别带中文的网址，编码类型为unicode。只转换汉字部分，不能全部网址进行转换
company = urllib.parse.quote(chinaCompany)
testUrl = "https://www.tianyancha.com/search?key=" + company
print("visit web:" + testUrl)

# 浏览器伪装池，将爬虫伪装成浏览器，避免被网站屏蔽
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

# 爬取第一个页面，即搜索企业名字，获得访问企业信息的跳转链接
searchCompanyRet = urllib.request.urlopen(testUrl).read().decode("utf-8", "ignore")
matchPat = 'tyc-event-ch="CompanySearch.Company".*?href="(.*?)" target='
nextUrls = re.compile(matchPat, re.S).findall(searchCompanyRet)
nextUrl = nextUrls[0]
print("企业详细信息可以查看下一个链接：" + str(nextUrl))

# 爬取第二个页面，即查看企业详细信息，获取出官网链接
companyDetail = urllib.request.urlopen(nextUrl).read().decode("utf-8", "ignore")
matchPat = 'class="company-link".*?href="(.*?)".*?rel'
companyUrl = re.compile(matchPat, re.S).findall(companyDetail)
print(companyUrl)

