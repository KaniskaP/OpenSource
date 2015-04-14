__author__ = 'Kan!skA'

import unittest, csv
from selenium import webdriver
from ddt import ddt, data, unpack
from selenium.webdriver.common.keys import Keys

def get_data(Data):
    rows = []
    data_file = open(Data, "r")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(11)
        self.driver.maximize_window()
        self.driver.get("https://translations.documentfoundation.org/")
        assert "Document Foundation – Pootle server" in self.driver.title

    @data(*get_data('Data.csv'))
    @unpack
    def runLogin(self, Username, Password, Lang):
        self.driver.find_element_by_xpath(".//*[@id='nav-main']/li[2]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='id_username']").send_keys(Username)
        self.driver.find_element_by_xpath(".//*[@id='id_password']").send_keys(Password)
        self.driver.find_element_by_xpath(".//*[@id='loginform']/p[4]/input[1]").submit()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
