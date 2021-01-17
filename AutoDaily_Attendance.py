# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/23 0:13
@Auth ： HRH_theRenegade
@File ：AutoDaily_Attendance.py
@IDE ：PyCharm
@Motto：To the time to life, rather than to life in time.
"""
#此处获取页面源码，以及cookie
import json

import requests

import CenterToken
import GetBaseInfo

raw,cookies = CenterToken.getRawResonse()
#从页面源码获取token
token= CenterToken.SearchToken(raw.text)
BaseInfo=GetBaseInfo.GetBaseInfo()
BaseInfo.GetBaseInfo_json()
def AutoDaily_Attendance():
    url='https://yqfk.dgut.edu.cn/home/base_info/addBaseInfo'
    headers={
        'Connection':'keep-alive',
            "Accept":"application/json" ,
            "'Content-Type":"application/json; charset=utf-8",
          "authorization":BaseInfo.Auth,
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
          "Origin":"https://yqfk.dgut.edu.cn",
          "Sec-Fetch-Site":"same-origin",
          "Sec-Fetch-Mode":"cors",
          "Sec-Fetch-Dest":"empty",
          "Referer":"https://yqfk.dgut.edu.cn/main",

          "Accept-Language":"zh-CN,zh;q=0.9",
          "Cookie":"_ga=GA1.3.1085698636.1567594517; PHPSESSID="+BaseInfo.cookies
}
    data=BaseInfo.GetBaseInfo_json()
    response=requests.post(url,headers=headers,json=data)
    while response.text.find("提交") == -1:
        response = requests.post(url, headers=headers, json=data)
    print(response.text)
AutoDaily_Attendance()