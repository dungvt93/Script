import browser_cookie3
import requests
import os

chromecookies = os.path.join(os.path.expandvars("%userprofile%"),"AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Cookies")
# cookiejar = browser_cookie3.chrome(cookie_file=chromecookies, domain_name="desknets.ndensan.co.jp")
cookiejar = browser_cookie3.chrome()
resp = requests.get('https://desknets.ndensan.co.jp/scripts/dneo/dneo.exe?cmd=login', cookies=cookiejar)
print(resp.content)