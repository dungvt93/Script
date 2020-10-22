#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import browser_cookie3
import json

#pip install browser-cookies3
#pip install requests

url = "https://desknets.ndensan.co.jp/scripts/dneo/dneor.exe/schcmdentry/"
cj = browser_cookie3.chrome(domain_name="desknets.ndensan.co.jp")
dnzSid = ''
dnzToken = ''
dnzHashcmd = ''
for cookie in cj:
    if(cookie.name == "dnzSid"):
        dnzSid = cookie.value
    if(cookie.name == "dnzToken"):
        dnzToken = cookie.value
    if(cookie.name == "dnzHashcmd"):
        dnzHashcmd = cookie.value

# test_cookie = 'dnzInfo=783;dnzLeftmenu=0;dnzSv=;dnzPtab=S;dnzSid='+dnzSid+';dnzToken='+dnzToken+';dnzHashcmd='+dnzHashcmd
# print(test_cookie)
test_cookie = {
    'dnzInfo':783,
    'dnzLeftmenu':0,
    'dnzPtab':'S',
    'dnzSid':dnzSid,
    'dnzToken':dnzToken,
    'dnzHashcmd':dnzHashcmd
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    # 'Content-Length': 454,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'desknets.ndensan.co.jp',
    'Origin': 'https://desknets.ndensan.co.jp',
    'Referer': 'https://desknets.ndensan.co.jp/scripts/dneo/dneo.exe?cmd=schindex&log=on',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Cookie': 'dnzInfo=783; dnzLeftmenu=0; dnzSv=; dnzPtab=S; dnzSid=ACeRMTOiH%5COFpPGhLPGEFPVFdLXM; dnzToken=5fa8ee965025a4f895cc8a2fc895fcd2; dnzHashcmd=fin; _ga=GA1.3.1281444685.1540780412',
    'Cookie': json.dumps(test_cookie)
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

# response = requests.post(url, headers=headers, data=json.dumps(form_data), cookies=cj)
session = requests.session()
r_c = session.get("https://desknets.ndensan.co.jp/scripts/dneo/dneo.exe?cmd=schindex&log=on")
# r = session.post(url, headers=headers, data=form_data, cookies=test_cookie)
r = requests.post(url, headers=headers, data=form_data)
r.encoding = r.apparent_encoding
print(r)



