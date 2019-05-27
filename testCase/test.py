#-*-coding:utf-8 -*-





from bs4 import BeautifulSoup

import requests
import json
import threading
import time
import uuid
import os

import re


file_path = os.path.dirname(os.path.abspath('.')) + '/testFile/test.txt'


def get_params(url, data):
    url = url + '?'
    for key in data:
        url = url + key + '=' + data[key] + '&'
    return url[:-1]






def post():
    try:
        # id
        # id=["529360399"]
        id = 529360399

        for x in range(0, 2):
            id += x

            ur = "https://www.dandb.com/search/"
            data = {"keyword": str(id), "country": "CP", "submit": "SEARCH", "type": "coo",
                    "source": "%2Finternational-credit-reports%2F"}
            url = get_params(ur, data)
            headers = {

                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
            }

            response = requests.get(url, headers=headers, verify=False)
            ll = response.content
            print(ll)
            ls = BeautifulSoup(ll, "html.parser")
            tag_soup = ls.find(class_='company')

            x = 0

            # print(tag_soup.children)

            for i in tag_soup.children:
                # print(i)
                p = r'<h2>(.+?)</h2>'
                html = str(i)
                text = re.findall(p, html)
                print(text)

                # 如果没有txt文件则新建文件，并执行写入操作
                with open(file_path, 'a', encoding='utf-8') as f:
                    if not os.path.exists(file_path):
                        os.makedirs(file_path)
                    f.write("id-" + str(id) + ": " + str(text) + "\n")
                    f.close()
                    x = x + 1




    except Exception as e:
        print(e)






# def kquan_bf():
#     login = postrequests()
#     return login.post()

if __name__ == '__main__':
    post()

# try:
#     i = 0
#     # 开启线程数目
#     tasks_number = 1
#     print('测试启动')
#     time1 = time.clock()
#     while i < tasks_number:
#         t = threading.Thread(target=kquan_bf)
#         t.start()
#         time.sleep(1)
#         i += 1
#     time2 = time.clock()
#     times = time2 - time1
#     print(times / tasks_number)
# except Exception as e:
#     print(e)