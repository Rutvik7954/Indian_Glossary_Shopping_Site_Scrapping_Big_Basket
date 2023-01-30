import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\BAPS\Downloads\chromedriver.exe")


def get_page(str1):
    driver.get(str1)


def get_elements_using_class(str2):
    elements = driver.find_elements(by=By.CLASS_NAME, value=str2)
    return elements


def get_elements_using_tag(str2):
    elements = driver.find_elements(by=By.TAG_NAME, value=str2)
    return elements


def get_elements_using_xpath(str2):
    elements = driver.find_elements(by=By.XPATH, value=str2)
    return elements


def get_elements_using_css(str2):
    elements = driver.find_elements(by=By.CSS_SELECTOR, value=str2)
    return elements


def get_elements_using_id(str2):
    elements = driver.find_elements(by=By.ID, value=str2)
    return elements


def get_elements_using_name(str2):
    elements = driver.find_elements(by=By.NAME, value=str2)
    return elements

def find_element(element):
    if driver.find_elements(by=By.CLASS_NAME, value='element'):
        return 1

def driver_close():
    driver.close()