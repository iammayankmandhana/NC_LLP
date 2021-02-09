from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

# the program is written in main function using chromewebdriver
from selenium import webdriver

# with chrome interface displaying to the user
driver = webdriver.Chrome(r"C:/Users/chromedriver.exe")
driver.get("https://www.saucedemo.com/") 

# login page
folder = driver.find_element_by_xpath("//input[@data-test='username']")
folder.click()
folder.send_keys("standard_user")
folder = driver.find_element_by_xpath("//input[@data-test='password']")
folder.click()
folder.send_keys("secret_sauce")
folder = driver.find_element_by_xpath("//input[@id='login-button']")
folder.click()

# adding products to the cart
folder = driver.find_element_by_xpath("//*[text()='Sauce Labs Bike Light']")
folder.click()
folder = driver.find_element_by_xpath("//*[text()='ADD TO CART']")
folder.click()
folder = driver.find_element_by_xpath("//button[@class='inventory_details_back_button']")
folder.click()
folder = driver.find_element_by_xpath("//*[text()='Sauce Labs Onesie']")
folder.click()
folder = driver.find_element_by_xpath("//*[text()='ADD TO CART']")
folder.click()
folder = driver.find_element_by_xpath("//button[@class='inventory_details_back_button']")
folder.click()
folder = driver.find_element_by_xpath("//div[@id='shopping_cart_container']")
folder.click()
folder = driver.find_element_by_xpath("//*[text()='CHECKOUT']")
folder.click()

# checkout page
folder = driver.find_element_by_xpath("//input[@id='first-name']")
folder.click()
folder.send_keys("Mayank")
folder = driver.find_element_by_xpath("//input[@id='last-name']")
folder.click()
folder.send_keys("Mandhana")
folder = driver.find_element_by_xpath("//input[@id='postal-code']")
folder.click()
folder.send_keys("600089")

folder = driver.find_element_by_xpath("//input[@value='CONTINUE']")
folder.click()

# final landing page
folder = driver.find_element_by_xpath("//*[text()='FINISH']")
folder.click()