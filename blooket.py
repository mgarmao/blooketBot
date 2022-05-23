import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

blooketId = "908995"
mihirAmount = 10
mihirStartNumber = 0


driver = webdriver.Chrome('/Users/mgarm/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('http://www.google.com/')
time.sleep(1)
mihirNumber = 0

for x in range(mihirAmount):
    driver.get("https://dashboard.blooket.com/play")
    notClicked = True
    while(notClicked):
        if(driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/input')):
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/input').send_keys(blooketId)
            notClicked = False
    blooketCodeSubmit = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]')    
    blooketCodeSubmit.click()

    
    notClicked = True
    while(notClicked): 
        if driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input'):
            blooketNameField = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
            blooketNameField.send_keys('mihir'+str(mihirStartNumber))
            notClicked = False
         
    blooketNameSubmit = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/i')
    blooketNameSubmit.click()

    mihirNumber=mihirNumber+1
    mihirStartNumber = mihirStartNumber+1

    print(mihirNumber)
    
    if(mihirNumber<mihirAmount):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[mihirNumber])

while(True):
    if driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]'):
        pickOptionNumber = 0
        time.sleep(7)
        while(x in range(mihirStartNumber)):
            driver.switch_to.window(driver.window_handles[pickOptionNumber])
            randomNum = random.randint(1,4)
            if(randomNum==1):
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]').click()
            if(randomNum==2):
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]').click()
            if(randomNum==3):
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]').click()
            if(randomNum==4):
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]').click()
            
            pickOptionNumber = pickOptionNumber+1
        # //*[@id="app"]/div/div/div[2]/div[2]/div[1]
        # //*[@id="app"]/div/div/div[2]/div[2]/div[2]
        # //*[@id="app"]/div/div/div[2]/div[2]/div[3]
        # //*[@id="app"]/div/div/div[2]/div[2]/div[4]
driver.quit()