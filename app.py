from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://fir-example-9428c-default-rtdb.firebaseio.com/"


})


# chromedriver
# 압축해제한 웹드라이버의 경로와 파일명 지정
driver = webdriver.Chrome()

# Load Page
# chrome을 띄워 네이버 블로그 페이지를 연다.
driver.get(url="http://comci.kr:4082/st")

webdriver.ActionChains(driver).key_down(Keys.F5).perform()

driver.find_element(By.XPATH, r'//*[@id="sc"]').send_keys('천안오성고')

time.sleep(1)

driver.find_element(By.XPATH, r'//*[@id="학교찾기"]/table[1]/tbody/tr[2]/td[2]/input[2]').click()

time.sleep(1)

txt = driver.find_element(By.XPATH, r'//*[@id="학교명단검색"]/tbody/tr[3]/td').text

time.sleep(1)

driver.find_element(By.XPATH, r'//*[@id="학교명단검색"]/tbody/tr[2]/td[2]/a').click()

time.sleep(1)

ref = db.reference('1학년')
CL1=[[] for i in range(14)]
CL2=[[] for i in range(12)]
CL3=[[] for i in range(12)]

for k in range (14):
    driver.find_element(By.XPATH, r'//*[@id="ba"]').click()
    driver.find_element(By.XPATH, f'//*[@id="ba"]/option[{k+2}]').click()
    for i in range (5):
        for j in range (7):
            CL1[k].append(driver.find_element(By.XPATH, f'//*[@id="hour"]/table/tbody/tr[{j+3}]/td[{i+2}]').text)

for k in range (12):
    driver.find_element(By.XPATH, r'//*[@id="ba"]').click()
    driver.find_element(By.XPATH, f'//*[@id="ba"]/option[{k+16}]').click()
    for i in range (5):
        for j in range (7):
            CL2[k].append(driver.find_element(By.XPATH, f'//*[@id="hour"]/table/tbody/tr[{j+3}]/td[{i+2}]').text)

for k in range (12):
    driver.find_element(By.XPATH, r'//*[@id="ba"]').click()
    driver.find_element(By.XPATH, f'//*[@id="ba"]/option[{k+28}]').click()
    for i in range (5):
        for j in range (7):
            CL3[k].append(driver.find_element(By.XPATH, f'//*[@id="hour"]/table/tbody/tr[{j+3}]/td[{i+2}]').text)
print(CL2)
for d in range (14):

    for l in range (35):
       ref = db.reference(f'1학년/{d+1}반')
       ref.update({'교시' : CL1[d]})

for d in range (12):
    for l in range (35):
       ref = db.reference(f'2학년/{d+1}반')
       ref.update({'교시' : CL2[d]})

for d in range (12):
    for l in range (35):
       ref = db.reference(f'3학년/{d+1}반')
       ref.update({'교시' : CL3[d]})

    

#ref.update({'1-11교시' : txt})
#print(txt)

# driver.find_element(By.XPATH, r'//*[@id="hour"]/table/tbody/tr[{j+3}]/td[{i+2}]').click()
# time.sleep(3)
# 현재 URL을 출력
print(driver.current_url)

driver.close()

#//*[@id="ba"]/option[2]
#//*[@id="ba"]/option[3]