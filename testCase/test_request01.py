# -*- coding: utf-8 -*-
import time
import sys
import urllib
import requests
# from testCase import file_util
import xlwt
import re
from xlrd import open_workbook

from xlutils.copy import copy
import os

from bs4 import BeautifulSoup
import random

import urllib3.contrib.pyopenssl
import time
import hashlib
"""
一个账号只能查询100条，所以应该需要多个账号的源进行轮流查询




"""
user_agent_list = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
]
user_agent = random.choice(user_agent_list)



excel_path = os.path.dirname(os.path.abspath('.')) + '/testFile/text.xls'
# excel_path=r'C:\Users\Administrator\Desktop\text.xls'
if not os.path.exists(excel_path):
    os.makedirs(excel_path)

book = open_workbook(excel_path)
wb = copy(book)
ws = wb.get_sheet('Sheet1')



# # 覆盖保存
# book=xlwt.Workbook(encoding='gbk')
# sheet=book.add_sheet('结果',cell_overwrite_ok=True)

# for i in range(len(text)):
#     ws.write(rownum, 5, text[i])
# rownum += 1
# wb.save(excel_path)

file_path =os.path.dirname(os.path.abspath('.')) + '/testFile/test.txt'




def get_params(url, data):
    url = url + '?'
    for key in data:
        url = url + key + '=' + data[key] + '&'
    return url[:-1]

# def get_id():
#     id = 529360398
#
#     for x in range(0, 2):
#         id += x
#         return id








def post():
    global rownum
    try:
        # id
        # id=["529360399"]
        id = 529360399

        li=[]

        for y in range(0, 2):
            id += y


            ur = "https://www.dandb.com/search/"
            data = {"keyword": str(id), "country": "CP", "submit": "SEARCH", "type": "coo",
                    "source": "%2Finternational-credit-reports%2F"}
            url=get_params(ur,data)

            # headers = {
            #
            #
            #     "Host":"www.dandb.com",
            #     "Connection":"keep-alive",
            #     "Upgrade-Insecure-Requests":"1",
            #     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b",
            #     "Referer":"https://www.dandb.com/search/",
            #     "Accept-Encoding":"gzip, deflate, br",
            #     "Accept-Language":"zh-CN,zh;q=0.9",
            #     "Cookie":"_ga=GA1.2.1466823819.1558067591; _gcl_au=1.1.1100793291.1558067591; __adroll_fpc=315cfe4bd95f695af29d7695a1aebba7-1558067634993; _bcvm_vrid_1365765591595680765=648077686639308018TE16D87BDD151059E7FB88D0BFE7A1882AA79FB3DAB0A05186368628BB586E3E239E1479AAF36116703A77859993F75C64006D959F4CD01A2D9C63CA36E32FBBE; _gid=GA1.2.1703627904.1558585859; PHPSRV=ae1-php220-prd|XOjd/|XOjd/; _bcvm_vid_1365765591595680765=648084661233091005T9874F6A401BF1E7B0CE4C0BD3C06F31E4D5C4F28D2759ED87F2013C30EB58C5F1115BE26BC266298B1DA50EA89ED91204D2F2B4CA01A1BAA4089DE4A4E4A398C; __ar_v4=K22H63BX3VDGRG34N5IZ2N%3A20190516%3A41%7CAKEMTQXA7FHFBLGIKFO3F2%3A20190516%3A41%7CC5HQUG33K5GBNF3O4TZTMD%3A20190516%3A41; bc_pv_end=648084660993033144TEE79072DB8CECF414150819F476B350256DBE9AD402EB1E5AFB94AF1B327F0BC29AEF5131C2057EE614B6AA2D6842A873553B721E256935D0E171E7D508E34DD",
            #     "User-Agent": user_agent
            #
            #
            # }
            # proxy ={"https":"218.75.69.50","http":"60.216.101.46","http":"114.239.150.71","http":"60.217.64.237","http":"121.17.174.121	"}

            headers = {

                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
            }
            proxies = {'http':'125.116.199.145:39187',

                       }

            urllib3.contrib.pyopenssl.inject_into_urllib3()


            response = requests.get(url,headers=headers,proxies=proxies,verify=False, allow_redirects=False,timeout=120)
            print(response.content)

            res=re.findall('<span class="company"><h2>(.*?)</h2>',response.text,re.S)
            #包含变量
            results="Shanghai"

            if res is not None:
                if results not in res:
                    li.append(res)

            else:
                print('空值')
            rea = re.findall('<span class="search_results_address">([\s\S]*?)<br />([\s\S]*?)<br />[\s\S]*?</span>',
                             response.text, re.S)
            # if i in res:
            #     try:
            #         li.append(res)
            #     except IndexError:
            #         pass








            # ll = response.content
            # print(ll)
            # ls = BeautifulSoup(ll, "html.parser")
            # tag_soup = ls.find(class_='company')


            x = 0

            # print(tag_soup.children)

            # for i in tag_soup.children:
            #     # print(i)
            #     p = r'<h2>(.*?)</h2>'
            #     html = str(i)
            #     text = re.findall(p, html)
            #
            #     li.append(text)
                # print(text)
            with open(file_path, 'a', encoding='utf-8') as f:
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                f.write("id-" + str(id) + ": " + str(res)+str(rea)+ "\n")
                f.close()
                x = x + 1

                # 如果没有txt文件则新建文件，并执行写入操作

        return li




    except Exception as e:
        print(e)








rownum=1
def test(keyword):
    print(keyword)
    global rownum




    # txtflile= os.path.dirname(os.path.abspath('.')) + '/testFile/message01.txt'
    # # excel_path=os.path.dirname(os.path.abspath('.'))+'/testFile/result.xls'
    #
    #
    # if os.path.exists(txtflile):
    #     os.remove(txtflile)


    headers ={'Host':'www.qichacha.com',
             'Connection':'keep-alive',

             'Cache-Control':'max-age=0',
             'X-Requested-With':'XMLHttpRequest',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
             'Referer':'https://www.qichacha.com/',
             'Accept-Encoding':'gzip, deflate, br',
             'User-Agent':user_agent,
              "Accept-Language":'zh-CN,zh;q=0.9',
              # "Proxy-Authorization": auth,
              'Cookie':'QCCSESSID=45ubc3h4fmq1s0ugp89c3bqkd7; zg_did=%7B%22did%22%3A%20%2216ad93ce3017c-05ff8a422620ae-3e38580a-1fa400-16ad93ce30220b%22%7D; UM_distinctid=16ad93ce4422cf-01501ee638a18a-3e38580a-1fa400-16ad93ce4432f0; _uab_collina=155842280809716168119904; acw_tc=7169ab1c15584228109266621e0cd13f669dd3de64c9b7b09cce3f784e; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1558422808,1558594740; CNZZDATA1254842228=328383305-1558419087-https%253A%252F%252Fwww.baidu.com%252F%7C1558606344; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1558608456; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201558607903580%2C%22updated%22%3A%201558608495319%2C%22info%22%3A%201558422807317%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22c516a65e0f393707db7199d3ab83bef9%22%7D'
             }
    # headers = {
    #     "Proxy-Authorization": auth,
    #
    # }

    for page in range(1,2):
        # startUrl = 'https://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % keyword  # urllib.quote(keyword)
        startUrl= 'https://www.qichacha.com/search'
        data={"key":"{}".format(keyword),"ajaxflag":"1","p":"{}".format(page),"": ""}
        resultPage = requests.get(startUrl, headers=headers,params=data,verify=False,allow_redirects=False, timeout=50)  # 在请求中设定头，cookie
        # print(resultPage.text)



        # reponse=re.findall('<td class="imgtd" width="110">(.*?)<div class="cname">',resultPage.text,re.S)
        # print(reponse)
        # res = re.findall(r'<td class="imgtd".*?href="(.*?)".*?class="ma_h1">(.*?)</a> <div class="search-tags"> <span.*?<p class="m-t-xs">[\s\S]*?<a.*?>(.*?)<.*?<p class="m-t-xs">[\s\S]*?邮箱：([\s\S]*?)<span class="m-l">电话：(.*?)</span.*?<p class="m-t-xs">[\s\S]*?地址：([\s\S]*?)</p>', resultPage.text, re.S)
        res = re.findall(r'<td class="imgtd".*?href="(.*?)".*?class="ma_h1">(.*?)</a> <div class="search-tags"> </div.*?class="m-t-xs">[\s\S]*?<a.*?>(.*?)<.*?<p class="m-t-xs">[\s\S]*?邮箱：([\s\S]*?)<span class="m-l">电话：(.*?)</span.*?<p class="m-t-xs">[\s\S]*?地址：([\s\S]*?)</p>',resultPage.text, re.S)

        # if not len(res):
        #     res = re.findall(r'<td class="imgtd".*?href="(.*?)".*?class="ma_h1">(.*?)</a> <div class="search-tags"> </div.*?class="m-t-xs">[\s\S]*?<a.*?>(.*?)<.*?<p class="m-t-xs">[\s\S]*?邮箱：([\s\S]*?)<span class="m-l">电话：(.*?)</span.*?<p class="m-t-xs">[\s\S]*?地址：([\s\S]*?)</p>',resultPage.text, re.S)

        # for i in reponse:
        #     print(i
        head=['链接','公司','法人','邮箱','电话','地址']
        for q in range(len(head)):
            # print(keyword)
            ws.write(0,q,head[q])
        for j in res:
            detail_url='https://www.qichacha.com'+j[0]
            ress=requests.get(detail_url,headers=headers,verify=False,allow_redirects=False, timeout=50)
            # print(ress.text)
            reu=re.findall(r'class="" target="_blank.*?rel="nofollow">(.*?)</a>',ress.text,re.S)
            details_url=reu
            list_infor=list(j)
            list_infor[0]=details_url
            # print(list_infor)
            for i in range(len(list_infor)):
                ws.write(rownum, i, list_infor[i])
            rownum += 1
            wb.save(excel_path)





        time.sleep(7)

        # with open(txtflile, 'w', encoding="utf-8") as of:
        #     of.write(resultPage.text)


# def main_while(keyword):
#     get_result = False
#     while not get_result:
#         try:
#             test(keyword)
#             get_result = True
#         except Exception as e:
#             file_util.write_error(e)
#             print(e)
# #

if __name__ == '__main__':
    # my_list = post()
    #
    # try:
    #     for i in my_list:
    #         try:
    #             test(i[0])
    #             time.sleep(7)
    #         except IndexError:
    #             pass
    #
    # except TypeError:
    #     pass




    # post()
    my_list=['国创元禾','腾讯']
    for i in my_list:
        test(i)