import re
import time
from requests.api import get                                 # スリープを使うために必要
from selenium import webdriver  
import requests
from bs4 import BeautifulSoup     # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary                  # パスを通すためのコード
 
driver = webdriver.Chrome()                 # Chromeを準備
driver.get('https://www.google.com/')       # Googleを開く
 
search = driver.find_element_by_name('q')   # HTML内で検索ボックス(name='q')を指定する
search.send_keys('トヨタ 6月20日')             # 検索ワードを送信する
search.submit()
load_url = "https://www.google.com/search?q=%E3%83%88%E3%83%A8%E3%82%BF+8%E6%9C%8820%E6%97%A5&rlz=1C1QABZ_jaJP895JP895&sxsrf=AOaemvLOSazRvcvzt4iyl4dyMU1FST1eMQ%3A1631517374965&ei=vvo-YaWpOsmSoATN54WgCw&oq=%E3%83%88%E3%83%A8%E3%82%BF+8%E6%9C%8820%E6%97%A5&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECc6CAgAELADEM0COgUIABDNAkoECEEYAVCAmQFYh6ABYPmjAWgBcAB4AIABiAGIAY0CkgEDMC4ymAEAoAEByAEBwAEB&sclient=gws-wiz&ved=0ahUKEwilgNHss_vyAhVJCYgKHc1zAbQQ4dUDCA4&uact=5"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
aList = soup.find_all('a')
for sourse in aList:
    if len(sourse.text) > 10:
        get_url = sourse.get('href')
        a = get_url.replace('/url?q=', '')
        driver.get(a)
# time.sleep(5)                               # 5秒間待機
# driver.quit() 
