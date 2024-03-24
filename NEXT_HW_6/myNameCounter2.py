from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import csv


chrome_driver_path = "/Users/kim-sangwoo/Desktop/NEXT/Session/NEXT_Session_6/chromedriver-mac-arm64/chromedriver"
user_data_dir = "/Users/kim-sangwoo/Desktop/NEXT/HW/NEXT_HW_6/chrome_cache"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chrome_driver_path)


driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.name-ranking.com/')

name = input('이름을 입력하세요:')

today = datetime.now().strftime('%Y-%m-%d')

file=open(f"{today}MynameCounter2.csv", mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['이름', '사용자수', '랭킹', '남자비율'])

#검색창 열기
searchButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/a/i')
searchButton.click()
time.sleep(3)

#검색창에 이름 검색
input_element = driver.find_element(By.ID ,"keyword")
input_element.send_keys(f"{name}")
input_element.send_keys(Keys.ENTER)
time.sleep(3)

#최상단 이름 클릭
selectName = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/a/span/span')
selectName.click()

#사람 수, 랭킹, 남자 비율 가져오기
cnt = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/ul/li[1]/span[2]').text
rank = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/ul/li[1]/span[3]/span').text
male = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[4]/div[2]/div/div[2]/div[1]/span').text

#저장하자
writer.writerow([name, cnt, rank, male])