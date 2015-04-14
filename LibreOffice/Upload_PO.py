__author__ = 'Kan!skA'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from ddt import ddt,data,unpack

browser = webdriver.Firefox()
browser.maximize_window()

browser.get("https://translations.documentfoundation.org/")
assert "Document Foundation – Pootle server" in browser.title

def get_data(Data):
    rows = []
    data_file = open(Data, "rb")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


browser.find_element_by_xpath(".//*[@id='nav-main']/li[2]/a").click()
browser.find_element_by_xpath(".//*[@id='id_username']").send_keys("KaniskA")
browser.find_element_by_xpath(".//*[@id='id_password']").send_keys("inDIan")
browser.find_element_by_xpath(".//*[@id='loginform']/p[4]/input[1]").click()

