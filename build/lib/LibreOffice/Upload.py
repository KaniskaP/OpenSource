__author__ = 'Kan!skA'

import unittest
import csv
import win32com.client
import time, os
from selenium import webdriver
from ddt import ddt, data, unpack
from selenium.webdriver.support.ui import Select


def get_data(data):
    rows = []
    data_file = open(data, "r")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        time.sleep(22)
        self.driver.maximize_window()
        self.driver.get("https://translations.documentfoundation.org/")
        assert "Document Foundation – Pootle server" in self.driver.title

    @data(*get_data('Data.csv'))
    @unpack
    def test_Login(self, username, password, lang):
        self.driver.find_element_by_xpath(".//*[@id='nav-main']/li[2]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='id_username']").send_keys(username)
        self.driver.find_element_by_xpath(".//*[@id='id_password']").send_keys(password)
        self.driver.find_element_by_xpath(".//*[@id='loginform']/p[4]/input[1]").submit()

        str1 = str(".//*[@href='/")
        str2 = str("/']")
        str3 = str1 + lang + str2
        self.driver.find_element_by_xpath(str3).click()
        self.driver.find_element_by_xpath(".//*[@id='language']/tbody/tr[2]/td[1]/a/span").click()

        self.driver.find_element_by_xpath(".//*[@id='overview-actions-translate-offline']/div[2]/ul/li[2]/a/span").click()
        # text = Select(self.driver.find_element_by_xpath(".//*[@id='id_upload_to']"))
        time.sleep(2)
        comboBoxCompleteText = self.driver.find_element_by_xpath(".//*[@id='id_upload_to']")
        comboBoxCompleteTextList = comboBoxCompleteText.text.split()
        time.sleep(2)
        for comboBoxElementText in comboBoxCompleteTextList:
            if comboBoxElementText == '---------':
                continue
            time.sleep(2)
            Select(self.driver.find_element_by_xpath(".//*[@id='id_upload_to']")).select_by_visible_text(comboBoxElementText)
            time.sleep(2)
            #click on browse button
            self.driver.find_element_by_xpath(".//*[@id='id_file']").click()
            time.sleep(2)
            shell = win32com.client.Dispatch("WScript.Shell")
            selectedFile = os.getcwd() + '\\' + lang + '\\' + comboBoxElementText
            selectedFile = selectedFile.replace("/", "\\")
            shell.SendKeys(selectedFile, 0)
            #self.driver.implicitly_wait(2000)
            time.sleep(2)
            #shell.SendKeys("{ESC}", 0)
            shell.SendKeys("{ENTER}", 0)
            #click upload button
            self.driver.find_element_by_xpath(".//*[@id='upload']/form/p[6]/input").click()
            time.sleep(5)
            self.driver.find_element_by_xpath(".//*[@id='overview-actions-translate-offline']/div[2]/ul/li[2]/a/span").click()
            time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='nav-main']/li[2]/a")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()