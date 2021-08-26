import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from selenium.webdriver import Chrome
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt
import pandas as pd

def page_make(max_num):
    dial = []
    for i in range(1,max_num+1):
        addr = 'https://pelicana.co.kr/store/stroe_search.html?page='+str(i)
        dial.append(addr)
    return dial

def store_list(lists):
    store_pd2 = []
    path = './webdriver/chromedriver'
    delay = 2
    driver= Chrome(path)
    driver.implicitly_wait(delay)
    for l in lists:
        link = l
        driver.get(link)      
        tr_list = driver.find_elements_by_xpath('//*[@id="contents"]/table/tbody/tr')
        for i in range(1,len(tr_list)+1):
            name = driver.find_element_by_xpath('//*[@id="contents"]/table/tbody/tr['+str(i)+']/td[1]').text
            addr = driver.find_element_by_xpath('//*[@id="contents"]/table/tbody/tr['+str(i)+']/td[2]').text
            if addr == "":
                break
            tel = driver.find_element_by_xpath('//*[@id="contents"]/table/tbody/tr['+str(i)+']/td[3]').text
            tel = tel.split('\n')
            tel = tel[0]
            store_pd2.append([name,addr,tel])                   
    return store_pd2