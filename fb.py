from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
# import requests
import os
import datetime
import csv
# import concurrent.futures
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)

# Facebook
fb_url = 'https://m.facebook.com/'
fb_user = 'jasongame1220@gmail.com'
fb_pwd = 'jasongod'

urls = []
queries = []


logging.info('start')

def transform(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"')
    # chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # sleep(1)
    # Login
    driver.get(fb_url + 'login')

    sleep(2)
    # Credentials
    username_input = driver.find_element_by_css_selector("input[name='email']")
    password_input = driver.find_element_by_css_selector("input[name='pass']")
    username_input.send_keys(fb_user)
    password_input.send_keys(fb_pwd)


    driver.find_element(By.NAME, "login").click()

    sleep(1)
    print('Processing: %s' % url)
    new_url = fb_url + '%s' % url + '/about'
    # driver.execute_script("window.open(" + new_url + ");")
    driver.get(new_url)
    sleep(2)
    # Likes
    aux_likes = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div/span/span[1]')
    likes = aux_likes.text
    likes = likes.partition(' ')[0]
    likes = likes.replace(',', '')
    print(likes)
    # Followers
    aux_followers = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/span/span')
    followers = aux_followers.text
    followers = followers.partition(' ')[0]
    followers = followers.replace(',', '')
    print(followers)
    # Profile picture (avatar)
    aux_profile_picture = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/a')
    profile_picture = aux_profile_picture.get_attribute('href')
    print(profile_picture)
    sleep(1)
    print('UPDATE facebook SET avatar = "%s", likes = "%s", subscriptions = "%s" WHERE url = "%s";' % (profile_picture, likes, followers, url))
    queries.append('UPDATE facebook SET avatar = "%s", likes = "%s", subscriptions = "%s" WHERE url = "%s";' % (profile_picture, likes, followers, url))
    # Closes the Selenium driver (Chrome)
    driver.close()
    return


with open('fb_user_list.csv', 'r') as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        transform(row[0])
        # urls.append(row[0])

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(transform, urls)
    # # Closes the Selenium driver (Chrome)
    # driver.close()

# Write to a file
# with open("output.sql", "w") as txt_file:
#     txt_file.write()
print(queries)