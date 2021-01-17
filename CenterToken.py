"""
@Time ： 2020/12/22 11:32
@Auth ： HRH_theRenegade
@File ：GetBaseInfo.py
@IDE ：PyCharm
@Motto：To the time to life, rather than to life in time.
"""

import requests
from lxml import etree
import re
userID='201841413111'
passwd='Hrh756810279'

def getRawResonse():
    """
    获取页面响应
    :return: 未处理过的页面代码,Cookie
    """
    url='https://cas.dgut.edu.cn/home/Oauth/getToken/appid/illnessProtectionHome/state/home.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        'username': userID,
        'password': passwd
    }
    response=requests.get(url=url, headers=headers)
    # print(str(response.cookies))

    cookies=re.search(r'PHPSESSID=(.*)',str(response.cookies))
    # print(cookies.group())
    # print(cookies.group()[10:36])
    if response.ok:

        cookies=cookies.group()[10:36]
        return response,cookies


def SearchToken(html_str):
    """
    正则表达式匹配token
    :param html_str（未经处理过的页面代码）:
    :return: 处理过匹配到的token
    """
    html_str = etree.HTML(html_str)
    li_list = html_str.xpath('/html/body/script[7]/text()')
    result=re.search(r'var token =(.*)',li_list[0])
    return result.group()[13:-2]


if __name__ == '__main__':
    raw,cookies = getRawResonse()

    result=SearchToken(getRawResonse()[0].text)
    with open('raw.html', 'w+', encoding='utf-8') as f:
        f.write(raw.text)
    print(result)
