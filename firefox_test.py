from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')


browser.find_element_by_class_name("bIiDR").click()

###===============LOG IN==========================###

username_input = browser.find_element_by_xpath("//input[@name='username']")
password_input = browser.find_element_by_xpath("//input[@name='password']")

username_input.send_keys("tie_customs")
password_input.send_keys("m@rkos13")

login_button = browser.find_element_by_class_name("L3NKy")
login_button.click()

save_info_button = browser.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
save_info_button.click()