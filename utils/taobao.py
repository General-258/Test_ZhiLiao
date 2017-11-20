# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

#url = "https://item.taobao.com/item.htm?spm=a21bz.7725273.1998564503.10.6d9e3c42yrlwL7&id=558334379721&umpChannel=qianggou&u_channel=qianggou"
#username = '1234qwer'
#password = '1234qwer'
driver = webdriver.Firefox()
def login(url, username, password):
    driver.get(url)
    sleep(3)
    driver.find_element_by_xpath(".//*[@id='J_SiteNavLogin']/div[1]/div[1]/a[1]").click()
    sleep(2)
    driver.find_element_by_xpath(".//*[@id='J_QRCodeLogin']/div[5]/a[1]").click()
    #driver.find_element_by_xpath(".//*[@id='J_Form']/div[2]/span").clear()
    driver.find_element_by_xpath(".//*[@id='J_Form']/div[2]/span").send_keys(username)
    #driver.find_element_by_xpath(".//*[@id='TPL_password_1']").clear()
    driver.find_element_by_xpath(".//*[@id='TPL_password_1']").send_keys(password)
    driver.find_element_by_id("J_SubmitStatic").click()
    sleep(2)



if __name__ == "__main__":
    url = "https://item.taobao.com/item.htm?spm=a21bz.7725273.1998564503.10.6d9e3c42yrlwL7&id=558334379721&umpChannel=qianggou&u_channel=qianggou"
    username = '17717564981'
    password = ''
    login(url,username,password)
