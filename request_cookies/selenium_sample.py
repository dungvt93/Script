#!/usr/bin/env python
# -*- coding: utf-8 -*-
import browser_cookie3
from selenium import webdriver
import datetime
import time
import traceback

try:
    cj = browser_cookie3.chrome(domain_name="desknets.ndensan.co.jp")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome("./chromedriver.exe",options=options) 
    driver.get("https://desknets.ndensan.co.jp/scripts/dneo/dneo.exe?cmd=login")
    for cookie in cj:  # session cookies
        cookie_dict = {'domain': "desknets.ndensan.co.jp", 'name': cookie.name, 'value': cookie.value}
        driver.add_cookie(cookie_dict)

    datenow = datetime.datetime.today().strftime('%Y%m%d')
    #id cua tung nguoi 
    id = "783"
    driver.get("https://desknets.ndensan.co.jp/scripts/dneo/dneo.exe?cmd=schindex&log=on#cmd=schadd&date="+datenow+"&enddate="+datenow+"&displaygroup=&id="+id)
    time.sleep(5)
    element = driver.find_element_by_name("event")
    driver.execute_script('''
        var elem = arguments[0];
        elem.value = "外部接触者";
    ''', element)

    element = driver.find_element_by_name("schcolor")
    driver.execute_script('''
        var elem = arguments[0];
        elem.value = 15;
    ''', element)

    element = driver.find_element_by_name("memo")
    driver.execute_script('''
        var elem = arguments[0];
        elem.value = "無し";
    ''', element)

    element.submit()
    driver.quit()
except Exception as e:
    traceback.print_exc()
