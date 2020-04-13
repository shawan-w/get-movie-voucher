from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



chrome_browser = webdriver.Chrome('./chromedriver.exe')



# Open chrome web browser and directs to movie voucher website

chrome_browser.maximize_window()
chrome_browser.get('https://www.freeliving.com.tw/Movie/VisaDebit/index.aspx')

get_ticket_button = chrome_browser.find_element_by_class_name('btn-colorG')
# print(get_ticket_button.get_attribute('innerHTML'))

get_ticket_button.click()


# Wait up to 10s for the first element to return 
user_name = WebDriverWait(chrome_browser, 10).until(
    EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_CardName"))
)
user_name.send_keys('NAME')

user_mobile = chrome_browser.find_element_by_id('ctl00_ContentPlaceHolder1_Mobile')
user_mobile.send_keys('0911333333')

mobile_recheck = chrome_browser.find_element_by_id('ctl00_ContentPlaceHolder1_Mobile_ReCheck')
mobile_recheck.send_keys('0911333333')

user_email = chrome_browser.find_element_by_id('ctl00_ContentPlaceHolder1_EMail')
user_email.send_keys('xxx@gmail.com')

card_num1 = chrome_browser.find_element_by_id('ctl00_ContentPlaceHolder1_CheckCardNo1')
card_num1.send_keys('1234')

card_num2 = chrome_browser.find_element_by_id('ctl00_ContentPlaceHolder1_CheckCardNo2')
card_num2.send_keys('1234')

card_num3 = chrome_browser.find_element_by_id('ctl00_ContentPlaceHolder1_CheckCardNo3')
card_num3.send_keys('1234')

card_num4 = chrome_browser.find_element_by_id('ctl00_ContentPlaceHolder1_CheckCardNo4')
card_num4.send_keys('1234')