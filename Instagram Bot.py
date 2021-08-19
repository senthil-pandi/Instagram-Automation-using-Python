from selenium import webdriver
import time

chrome_browser = webdriver.Chrome("chromedriver.exe")
chrome_browser.get("https:www.instagram.com")
time.sleep(3)

#Login
user_name = chrome_browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
user_name.send_keys("username")
time.sleep(3)
password = chrome_browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("password")
password.submit()
time.sleep(3)

#Closing the Save Info
not_now1 = chrome_browser.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/div/div/div/button")
not_now1.click()
time.sleep(3)

#Closing the Notification Info
not_now2 = chrome_browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
not_now2.click()
time.sleep(3)


def first_picture():
    '''This function is used to just click on the first 
    picture in your news feed'''
    time.sleep(3)
    picture = chrome_browser.find_element_by_class_name("_9AhH0")
    picture.click()
    
def like_picture():
    '''This function is used to like the first feed'''
    time.sleep(3)
    like = chrome_browser.find_element_by_xpath("/html/body/div[1]/div/div/section/main/section/div[1]/div[2]/div/article[1]/div[3]/section[1]/span[1]/button")
    like.click()

first_picture()
like_picture()

