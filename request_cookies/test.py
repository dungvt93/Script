#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, http.cookiejar, urllib.request
import requests
import browser_cookie3
import json

url = "https://desknets.ndensan.co.jp/scripts/dneo/dneor.exe/schcmdentry/"
cj = browser_cookie3.chrome(domain_name="desknets.ndensan.co.jp")

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    # 'Cookie':'dnzInfo=783; dnzLeftmenu=0; dnzSv=; dnzPtab=S; dnzSid=ACeIFITOVL%60LaLDEC%7D%5EMTFHFRG%5EF; dnzToken=830a89add7e3adb413e2ac04c7b48526; dnzHashcmd=fin; _ga=GA1.3.1281444685.1540780412'
}

form_data = {
    'cmd': 'schcmdentry',
    # 'topmsgid': ,
    'schcolor': 15,
    # 'tagcolor': ,
    # 'iconno': ,
    # 'repeat': ,
    'startdate': '2020-10-20',
    # 'starttime': ,
    'enddate': '2020-10-20',
    # 'endtime': ,
    'event': '外部接触者',
    # 'detail': ,
    # 'place': '--',
    # 'other': ,
    'memo': '無し',
    'outflg': '1',
    # 'reserve': ,
    # 'rankflg': ,
    'flag': 0,
    'otherto': 783,
    # 'approvsts': ,
    'sendhowto': 4,
    # 'public_level': ,
    # 'approvreq': ,
    'approv_notice_kind': 1,
    'alarm': 0,
    # 'alarmtime': ,
    'tvmeeting_chairs': 783,
    'tvmeeting_members': 783,
    # '16031755531225885': ,
    'c9efdbdcbfc3bac4d0050719081aa321': 1,
}

session = requests.Session()
r = requests.post(url, headers=headers, data=form_data, cookies=cj)
r.encoding = r.apparent_encoding
print(r)
