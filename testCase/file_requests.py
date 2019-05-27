# -*- coding: utf-8 -*-
import time
import sys
import urllib
import requests
from testCase import file_util
import xlwt
import re
from xlrd import open_workbook

from xlutils.copy import copy
import os
from bs4 import BeautifulSoup

"""
一个账号只能查询100条，所以应该需要多个账号的源进行轮流查询




"""


rownum=1
def main(keyword):
    global rownum

    excel_path = os.path.dirname(os.path.abspath('.')) + '/testFile/result.xls'
    if not os.path.exists(excel_path):
        os.makedirs(excel_path)


    # 覆盖保存
    # book=xlwt.Workbook(encoding='gbk')
    # sheet=book.add_sheet('结果',cell_overwrite_ok=True)
    # 不覆盖保存
    book = open_workbook(excel_path)
    wb = copy(book)
    ws = wb.get_sheet('结果')

    txtflile= os.path.dirname(os.path.abspath('.')) + '/testFile/message.txt'
    # excel_path=os.path.dirname(os.path.abspath('.'))+'/testFile/result.xls'


    if os.path.exists(txtflile):
        os.remove(txtflile)


    headers ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'zh-CN,zh;q=0.9',
             'Cache-Control':'no-cache',
             'Connection':'keep-alive',
             'Host':'www.tianyancha.com',
             'Pragma':'no-cache',
              # "Cookie":"aliyungf_tc=AQAAALmSFFEzLg4AKQNZceb9hFTF9JqS; ssuid=2560953996; bannerFlag=undefined; csrfToken=b9oZ6z8DNwHFRc5ph6zgLmlc; TYCID=961361e079cd11e98d29c5003a75a1ca; undefined=961361e079cd11e98d29c5003a75a1ca; _ga=GA1.2.147424696.1558225951; _gid=GA1.2.951873948.1558225951; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1558225951,1558232846,1558232910; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E8%2594%25BA%25E7%259B%25B8%25E5%25A6%2582%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODI2NDQ3MCwiZXhwIjoxNTg5ODAwNDcwfQ.VawvigpX5yxEPbKuhVPHaNlZZJckgVBQQ-xJ7obcF1SujhcgNOyn8L9fGTdokJSp2YUR5P4EzzrDLXYmvpHOhA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215074709134%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODI2NDQ3MCwiZXhwIjoxNTg5ODAwNDcwfQ.VawvigpX5yxEPbKuhVPHaNlZZJckgVBQQ-xJ7obcF1SujhcgNOyn8L9fGTdokJSp2YUR5P4EzzrDLXYmvpHOhA; RTYCID=a144ba90d7684bd297b7664abf35261d; CT_TYCID=4a0b16437726464a87297c5daac758f7; cloud_token=a0687ca285374c279902ea61bb72ba86; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1558324836; token=d6ade0a644d143bc82e26162f11c7253; _utm=774725c7349c4abfaf2271b9ea43d3ce",
             'Upgrade-Insecure-Requests':'1',
             'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
              "token":'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODMzNzY1NiwiZXhwIjoxNTg5ODczNjU2fQ.BGbzr3J8Z4sKbK9x72zuSjkPwRnS3Dke3xhr54bWi3NI6QEtp3FI9FjsOygMwJ6Q-tnIF8VYYzf4uXyVqGIhtw'
             }
    cookies = {"aliyungf_tc": "AQAAALmSFFEzLg4AKQNZceb9hFTF9JqS", "ssuid": "2560953996", "bannerFlag": "undefined",
               "csrfToken": "b9oZ6z8DNwHFRc5ph6zgLmlc",
               "TYCID": "961361e079cd11e98d29c5003a75a1ca", "undefined": "961361e079cd11e98d29c5003a75a1ca",
               "_ga": "GA1.2.147424696.1558225951", "_gid": "GA1.2.951873948.1558225951",
               "Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1558225951,1558232846,1558232910",
               "token": "ae73437ab20b49359e281328f57bd47d", "_utm": "c16c4416241b4497a62af5b6d8d32934",
               "tyc-user-info": "%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E8%2594%25BA%25E7%259B%25B8%25E5%25A6%2582%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODIzNzUzNCwiZXhwIjoxNTg5NzczNTM0fQ.GRNg4BYvpjAGiPSWnTCjmhgQzi79nX6GquZBO2q6MSYtiDMTeiT1lDrZm2ujzODIUQvVo0LG6R-fzOrQCVUeog%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215074709134%2522%257D",
               "auth_token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA3NDcwOTEzNCIsImlhdCI6MTU1ODIzNzUzNCwiZXhwIjoxNTg5NzczNTM0fQ.GRNg4BYvpjAGiPSWnTCjmhgQzi79nX6GquZBO2q6MSYtiDMTeiT1lDrZm2ujzODIUQvVo0LG6R-fzOrQCVUeog",
               "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758": "1558237537"
               }

    for page in range(1,2):
        # startUrl = 'https://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % keyword  # urllib.quote(keyword)
        startUrl= 'https://www.tianyancha.com/search/p{}?key={}'.format(page, keyword)
        resultPage = requests.get(startUrl, headers=headers, cookies=cookies,verify=False)  # 在请求中设定头，cookie
        print(resultPage.text)
        # ls = BeautifulSoup(resultPage.content, "html.parser")
        # tag_soup = ls.findAll(class_='content')
        # print(tag_soup.get_text())


        # reponse=re.findall('<div class="content"><div class="header">(.*?)<span class="site">',resultPage.text,re.S)
        reponse = re.findall(r'<div class="triangle-xcx"><div class="tips">(.*?)<span class="site">', resultPage.text, re.S)

        # for i in reponse:
        #     print(i)
        head=['公司名','链接','法人','电话','邮箱']
        for q in range(len(head)):
            ws.write(0,q,head[q])
        for i in reponse:
            # res=re.findall('<a class="name.*?href="(.*?)".*?>(.*?)</a.*?法定代表人>*?>(.*?)<.*?class="link-hover-click">(.*?)<.*?class="link-hover-click">(.*?)<',str(i),re.S)
            res = re.findall(r'<div class="logo -w88".*?<em>(.*?)</em>.*?href="(.*?)"[\s\S]*?title="(.*?)".*?电话.*?<span.*?>(.*?)<.*?邮箱.*?<span.*?>(.*?)</span>',str(i), re.S)
            # for i in res:
            #     print(i)

            if res !=[]:
                for j in range(len(res[0])):
                    ws.write(rownum, j, res[0][j])
                rownum += 1
                wb.save(excel_path)



        time.sleep(10)

        with open(txtflile, 'w', encoding="utf-8") as of:
            of.write(resultPage.text)


def main_while(keyword):
    get_result = False
    while not get_result:
        try:
            main(keyword)
            get_result = True
        except Exception as e:
            file_util.write_error(e)
            print(e)


if __name__ == '__main__':


    keyword = 'Beijing Mingtai Yanshen Technology Co., Ltd.'

    main(keyword)