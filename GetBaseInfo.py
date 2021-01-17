# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/22 11:48
@Auth ： HRH_theRenegade
@File ：GetBaseInfo.py
@IDE ：PyCharm
@Motto：To the time to life, rather than to life in time.
"""
import datetime

import requests
import CenterToken
import json
from Decorations.testGetBaseInfo import testResultGetBaseInfo_json
from Decorations.RedoWhenFail import RedoWhenFail

class GetBaseInfo:
    # 此处修改账号密码
    userID = '201841413111'
    passwd ='Hrh756810279'

    def __init__(self):
        # 此处获取页面源码，以及cookie
        self.raw, self.cookies = CenterToken.getRawResonse()
        # 从页面源码获取token
        self.token = CenterToken.SearchToken(self.raw.text)
    @RedoWhenFail
    def GetAuth(self):
        """
        获取Authentication
        :return:
        """
        url = 'https://cas.dgut.edu.cn/home/Oauth/getToken/appid/illnessProtectionHome/state/home.html'
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Origin": "https://cas.dgut.edu.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://cas.dgut.edu.cn/home/Oauth/getToken/appid/illnessProtectionHome/state/home.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "languageIndex=0; last_oauth_appid=illnessProtectionHome; last_oauth_state=home; PHPSESSID=" + self.cookies
        }

        data = {
            'username': self.userID,
            'password': self.passwd,
            '__token__': self.token
        }
        response = requests.post(url=url, headers=headers, data=data)
        f = json.loads(response.json())
        response2 = requests.get(f['info'])

        self.Auth = 'Bearer ' + response2.history[0].headers['Location'][22:]
        return self.Auth
    @RedoWhenFail
    def GetBaseInfo_Raw(self):
        """
        获取未处理过的表单信息
        :return:
        """
        url = 'https://yqfk.dgut.edu.cn/home/base_info/getBaseInfo'
        headers = {
            "Accept": "application/json",
            "authorization": self.GetAuth(),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://yqfk.dgut.edu.cn/main",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "_ga=GA1.3.1085698636.1567594517; UM_distinctid=17666b41075c41-0d0f1aed6335ee-5a301e42-1fa400-17666b41076ab6; _gid=GA1.3.747935397.1608554081; PHPSESSID=" + self.cookies
        }

        response = requests.get(url=url, headers=headers)

        baseInfo_json = json.loads(response.text)
        self.baseInfo_json = baseInfo_json



        return self.baseInfo_json

    def GetBaseInfo(self):
        """
        主API，处理表单信息,并写入文件，如果文件已存在则在文件中读
        :return: 处理过的表单信息，可以直接当做header
        """
        baseinfo = self.GetBaseInfo_Raw()['info']
        del baseinfo["whitelist"]
        del baseinfo["msg"]
        # del baseinfo['importantAreaMsg']
        flag = True
        while flag:
            try:
                with open('baseInfo.txt', 'r', encoding='utf8') as f:
                    content = f.read()

                    if len(content) == 0:
                        raise FileNotFoundError
                    content_json = json.loads(content)
                    content_json["submit_time"] = datetime.date.today().__str__()
                    print(content_json["submit_time"])
                    flag = False
            except FileNotFoundError:
                with open('baseInfo.txt', 'w', encoding='utf8') as f:
                    print('第一次运行吗？\n保存数据')
                    f.write(json.dumps(baseinfo, ensure_ascii=False))
        self.content_json = content_json
        return self.content_json
    @RedoWhenFail
    # @testResultGetBaseInfo_json
    def GetBaseInfo_json(self):
        """
        主API，处理表单信息,并写入文件，如果文件已存在则在文件中读
        :return: 处理过的表单信息，可以直接当做header
        """
        baseinfo = self.GetBaseInfo_Raw()['info']
        del baseinfo["whitelist"]
        del baseinfo["msg"]
        # del baseinfo['importantAreaMsg']
        flag = True
        while flag:
            try:
                with open('baseInfo.json', 'r', encoding='utf8') as f:
                    content = f.read()

                    if len(content) == 0:
                        raise FileNotFoundError
                    content_json = json.loads(content)
                    content_json["submit_time"] = datetime.date.today().__str__()
                    flag = False
            except FileNotFoundError:
                with open('baseInfo.json', 'w', encoding='utf8') as f:
                    print('第一次运行吗？\n保存数据')
                    json.dump(baseinfo, f)
        self.content_json = content_json
        return self.content_json

b = GetBaseInfo()
b.GetBaseInfo_json()


