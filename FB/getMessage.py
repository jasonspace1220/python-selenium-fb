from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup
from databases import mysql
import json

from time import sleep
import os
import datetime
import csv

# Facebook
fb_url = 'https://facebook.com/'
fb_user = 'jasongame1220@gmail.com'
fb_pwd = 'jasongod'

urls = []
queries = []


# logging.info('start')
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

fbSqlData = mysql.mysql()

def transform(url):

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
        print("is logging")

    sleep(1)
    print('Processing: %s' % url)

    driver.get(url)
    sleep(2)
    print(url)

    # Click 留言 按鈕
    msg_btn = driver.find_element(By.CSS_SELECTOR, "#watch_feed > div > div.c9zspvje.ad2k81qe.f9o22wc5.jb3vyjys.f7vcsfb0.qt6c0cv9.fjf4s8hc.n24pcjkn.l0gotlms.igoxciu3 > div > div > div > div.k4urcfbm > div.sq6gx45u.buofh1pr.cbu4d94t.j83agx80 > div:nth-child(1) > div > div.l9j0dhe7.hpfvmrgz.bkfpd7mw.g5gj957u.buofh1pr.j83agx80 > div > div.pfnyh3mw.j83agx80.bp9cbjyn > div > span")
    msg_count = msg_btn.text.replace("則留言", "")
    fbSqlData.updateFBMessageOne(url,"msg_count",msg_count)
    print("留言數 : ",msg_count)

    msg_btn.click()

    sleep(2)
    

    #查看更多留言
    see_more_msg_btn_selector = "#watch_feed > div > div.c9zspvje.ad2k81qe.f9o22wc5.jb3vyjys.f7vcsfb0.qt6c0cv9.fjf4s8hc.n24pcjkn.l0gotlms.igoxciu3 > div > div > div > div.k4urcfbm > div.sq6gx45u.buofh1pr.cbu4d94t.j83agx80 > div.cwj9ozl2.j83agx80.cbu4d94t.buofh1pr.d76ob5m9.eg9m0zos.du4w35lb > div.l9j0dhe7.tkr6xdv7.buofh1pr.eg9m0zos > div > div.j83agx80.buofh1pr.jklb3kyz.l9j0dhe7 > div.oajrlxb2.bp9cbjyn.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.g5gj957u.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.p8fzw8mz.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.gpro0wi8.m9osqain.buofh1pr > span > span"

    while check_more_msg_btn(driver,see_more_msg_btn_selector) : 
    
        myElem = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, see_more_msg_btn_selector)))

        more_msg_btn = driver.find_element(By.CSS_SELECTOR,see_more_msg_btn_selector)

        more_msg_btn.click()

        print("點查看留言數")

        sleep(2)

    #拉 留言的 List
    msg_ul_selector = "#watch_feed > div > div.c9zspvje.ad2k81qe.f9o22wc5.jb3vyjys.f7vcsfb0.qt6c0cv9.fjf4s8hc.n24pcjkn.l0gotlms.igoxciu3 > div > div > div > div.k4urcfbm > div.sq6gx45u.buofh1pr.cbu4d94t.j83agx80 > div.cwj9ozl2.j83agx80.cbu4d94t.buofh1pr.d76ob5m9.eg9m0zos.du4w35lb > div.l9j0dhe7.tkr6xdv7.buofh1pr.eg9m0zos > ul"
    msg_name_selector = "div:nth-child(1) > div > div.g3eujd1d.ni8dbmo4.stjgntxs.hv4rvrfc > div > div.q9uorilb.bvz0fpym.c1et5uql.sf5mxxl7 > div > div > div > div > div.nc684nl6 > a > span > span"
    msg_ctx_selector = "div:nth-child(1) > div > div.g3eujd1d.ni8dbmo4.stjgntxs.hv4rvrfc > div > div.q9uorilb.bvz0fpym.c1et5uql.sf5mxxl7 > div > div > div > div > div.ecm0bbzt.e5nlhep0.a8c37x1j > span > div"
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    data = {}

    x = 0
    y = 0
    for msg_ul in soup.select(msg_ul_selector):

        for msg_name in msg_ul.select(msg_name_selector):
            data[x] = {}
            data[x]["name"] = msg_name.text
            x+=1

        for msg_ctx_row in msg_ul.select(msg_ctx_selector):
            ctx = ""
            for msg_ctx in msg_ctx_row.select("div") : 
                ctx = ctx + "\n" + msg_ctx.text

            data[y]["ctx"] = ctx
            y+=1

    fbSqlData.updateFBMessageOne(url,"msgs",json.dumps(data ,ensure_ascii=False))
    # print(json.dumps(data ,ensure_ascii=False))
    print(data)

    return

def check_more_msg_btn(driver,selector):
    try:
        myElem = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector)))
        more_msg_btn = driver.find_element(By.CSS_SELECTOR,selector)

        return True
    except: 
        return False

keyList = fbSqlData.getFBMessageUrls()
keyCount = fbSqlData.getFBMessageCount()
nowCount = 1

for row in keyList:
    if nowCount == keyCount : 
        transform(row)
        driver.close()
    else : 
        transform(row)
        nowCount+=1

print(queries)