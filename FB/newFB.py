from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
import os
import datetime
import csv

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)

# Facebook
fb_url = 'https://facebook.com/'
fb_user = 'jasongame1220@gmail.com'
fb_pwd = 'jasongod'

urls = []
queries = []


logging.info('start')

def transform(url):
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

    # IPHONE Browser
    # chrome_options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"')
    # MAC Chrome Browser
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"') 

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(1440, 877)
    # sleep(1)
    try : 
        # Login
        driver.get(fb_url + 'login')

        sleep(4)
        logging.info(driver.page_source)
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
    # new_url = fb_url + '%s' % url + '/about'
    new_url = fb_url + '%s' % url + '/community'
    driver.get(new_url)
    sleep(2)
    print(new_url)

    # Likes
    # likes = driver.find_element(By.CSS_SELECTOR, ".taijpn5t:nth-child(3) .d2edcug0 > .d2edcug0:nth-child(1)")
    likes = driver.find_element(By.CSS_SELECTOR, ".s1tcr66n > .d2edcug0")
    likes = likes.text

    print(likes)
    # Followers
    followers = driver.find_element(By.CSS_SELECTOR, ".bp9cbjyn:nth-child(2) > .d2edcug0").text

    print(followers)
    # Profile picture (avatar)
    # aux_profile_picture = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/a')
    # profile_picture = aux_profile_picture.get_attribute('href')
    # print(profile_picture)
    # sleep(1)
    # print('UPDATE facebook SET avatar = "%s", likes = "%s", subscriptions = "%s" WHERE url = "%s";' % (profile_picture, likes, followers, url))
    # queries.append('UPDATE facebook SET avatar = "%s", likes = "%s", subscriptions = "%s" WHERE url = "%s";' % (profile_picture, likes, followers, url))
    # Closes the Selenium driver (Chrome)
    driver.close()
    return


with open('../fb_user_list.csv', 'r') as file:
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