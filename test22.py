from selenium import webdriver
import time
url = 'https://test.ewezx.com/login'
driver = webdriver.Firefox()
driver.get(url)


driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/section[2]/div/div/ul/li[1]/div/input').send_keys('15901819871')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/section[2]/div/div/ul/li[2]/div/input').send_keys('1111qqqq')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/section[2]/div/div/ul/li[4]/button').click()
time.sleep(1)
print driver.title
