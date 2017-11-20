# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://192.168.1.63:8080/login.html")
sleep(2)
driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div/div[1]/div[1]").click()
driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div/div[2]/div[1]/input").clear()
driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div/div[2]/div[1]/input").send_keys("17717564981")
driver.find_element_by_id("mm").clear()
driver.find_element_by_id("mm").send_keys("1234qwer")
driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div/div[2]/div[4]/div").click()
sleep(2)
driver.find_element_by_class_name("startbd").click()
sleep(1)
tianxiepage = driver.find_element_by_xpath("html/body/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]").text
print tianxiepage
driver.find_element_by_id("xm").clear()
driver.find_element_by_id("xm").send_keys(unicode("靳生顺"))
driver.find_element_by_id("sfz").clear()
driver.find_element_by_id("sfz").send_keys("632124199210262816")
driver.find_element_by_id("sjh").clear()
driver.find_element_by_id("sjh").send_keys("17717564981")
driver.find_element_by_xpath("html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]").click()
sleep(3)
text = driver.find_element_by_xpath("html/body/div[8]/div/p").text
print text
driver.find_element_by_xpath("html/body/div[8]/div/div").click()