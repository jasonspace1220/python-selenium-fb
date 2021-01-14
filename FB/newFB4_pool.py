from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import threading
from multiprocessing import Pool
import multiprocessing as mp

from databases import mysql

from time import sleep
import os
import datetime
import csv
import sys

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)

# Facebook
fb_url = 'https://facebook.com/'
fb_user = 'jasongame1220@gmail.com'
fb_pwd = 'jasongod'

urls = []
queries = []



fbSqlData = mysql.mysql()
threadLocal = threading.local()


def transform(url):


    # logging.info('start')
    # chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument("--no-sandbox") 
    # chrome_options.add_argument("--disable-setuid-sandbox") 
    # chrome_options.add_argument("--remote-debugging-port=9222")  # this
    # chrome_options.add_argument("--disable-dev-shm-using") 
    # chrome_options.add_argument("--disable-extensions") 
    # chrome_options.add_argument("--disable-gpu") 
    # chrome_options.add_argument("start-maximized") 
    # chrome_options.add_argument("disable-infobars") 
    # chrome_options.add_argument("--headless") 
    # chrome_options.add_argument('--ignore-certificate-errors')

    # # MAC Chrome Browser
    # chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"') 

    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.set_window_size(1440, 877)
    driver = get_driver()
    # sleep(1)
    try : 
        # Login
        driver.get(fb_url + 'login')

        sleep(4)
        # Login FaceBook
        username_input = driver.find_element_by_css_selector("input[name='email']")
        password_input = driver.find_element_by_css_selector("input[name='pass']")
        username_input.send_keys(fb_user)
        password_input.send_keys(fb_pwd)
        driver.find_element(By.NAME, "login").click()

    except : 
        print(sys.exc_info()[0])
        # print("is logging")

    sleep(3)
    print('Processing: %s' % url)
    new_url = fb_url + '%s' % url + '/community'
    try : 
        driver.get(new_url)
        sleep(2)
        print(new_url)
    except :
        print("Community Fail")
        print(sys.exc_info()[0])


    # Likes
    try : 
        likes = driver.find_element(By.CSS_SELECTOR, ".s1tcr66n > .d2edcug0")
        likes = likes.text
        fbSqlData.insertOne(url,'likes',likes)
        print(likes)
    except :
        print("Get Likes Fail")
        print(sys.exc_info()[0])


    # Followers
    try : 
        followers = driver.find_element(By.CSS_SELECTOR, ".bp9cbjyn:nth-child(2) > .d2edcug0").text
        fbSqlData.insertOne(url,'followers',followers)
        print(followers)
    except : 
        print("Get Followers Fail")
        print(sys.exc_info()[0])


    driver.close()
    return



def get_driver():
    driver = getattr(threadLocal, 'driver', None)
    if driver is None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-setuid-sandbox") 
        chrome_options.add_argument("--remote-debugging-port=9222")  # this
        chrome_options.add_argument("--disable-dev-shm-using") 
        chrome_options.add_argument("--disable-extensions") 
        chrome_options.add_argument("--disable-gpu") 
        chrome_options.add_argument("start-maximized") 
        chrome_options.add_argument("disable-infobars") 
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument('--ignore-certificate-errors')
        # MAC Chrome Browser
        chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"') 

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.set_window_size(1440, 877)

        setattr(threadLocal, 'driver', driver)
    return driver


keyList = fbSqlData.getFBKey()
keyCount = fbSqlData.getCount()
nowCount = 1


pool = Pool() # Pool() 不放參數則默認使用電腦核的數量
pool.map(transform,keyList) 
pool.close()
pool.join()



## TODO  多線程的狀況下 我可能會需要開多個Tab或是網頁
# print(queries)

# def multip():
#     pool = Pool(processes=3)
#     for i in range(0, keyCount):  
#         pool.apply_async(transform, args={keyList[i]})

#     pool.close()
#     pool.join()
#     driver.close()

# multip()