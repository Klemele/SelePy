# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

class GmailCreateAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.fr/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_gmail_create_account(self):
        #Driver definition
        driver = self.driver
        driver.implicitly_wait(10) # seconds
        driver.get(self.base_url)

        # #Acces to webproxy
        # driver.get(self.base_url)
        # self.find_element_and_wait(By.ID, "lst-ib").clear()
        # self.find_element_and_wait(By.ID, "lst-ib").send_keys("webproxy.to")
        # self.find_element_and_wait(By.NAME, "btnG").click()
        # self.find_element_and_wait(By.LINK_TEXT, "webproxy.to - USA IP web proxy, fast and anonymous!").click()
        #
        # #Acces to google through webproxy
        # self.find_element_and_wait(By.ID, "input").clear()
        # self.find_element_and_wait(By.ID, "input").send_keys("google.fr")
        # self.find_element_and_wait(By.CSS_SELECTOR, "input.button").click()

        #Acces to gmail
        self.find_element_and_wait(By.ID, "lst-ib").clear()
        self.find_element_and_wait(By.ID, "lst-ib").send_keys("gmail")
        self.find_element_and_wait(By.LINK_TEXT, "Gmail - Google").click()

        #Navigate to register form
        self.find_element_and_wait(By.CSS_SELECTOR, "#link-signup > a").click()

        #Fill FirstName
        self.find_element_and_wait(By.ID, "FirstName").clear()
        self.find_element_and_wait(By.ID, "FirstName").send_keys("SeleTest")

        #Fill LastName
        self.find_element_and_wait(By.ID, "LastName").clear()
        self.find_element_and_wait(By.ID,"LastName").send_keys("JKMG")

        #Fill GmailAddress
        self.find_element_and_wait(By.ID, "GmailAddress").clear()
        self.find_element_and_wait(By.ID, "GmailAddress").send_keys("SeleTestJKMG")

        #Fill Passwd
        self.find_element_and_wait(By.ID, "Passwd").clear()
        self.find_element_and_wait(By.ID, "Passwd").send_keys("JKMG123+-")

        #Fill PasswdAgain
        self.find_element_and_wait(By.ID, "PasswdAgain").clear()
        self.find_element_and_wait(By.ID, "PasswdAgain").send_keys("JKMG123+-")

        #Fill BirthDay
        self.find_element_and_wait(By.ID, "BirthDay").clear()
        self.find_element_and_wait(By.ID, "BirthDay").send_keys("24")

        #Fill BirthMonth
        driver.execute_script("return document.getElementById('HiddenBirthMonth').value = '7';")

        #Fill BirthYear
        self.find_element_and_wait(By.ID, "BirthYear").clear()
        self.find_element_and_wait(By.ID, "BirthYear").send_keys("1990")

        #Fill HiddenGender
        driver.execute_script("return document.getElementById('HiddenGender').value = 'OTHER';")

        #Fill Recaptcha
        self.find_element_and_wait(By.ID, "recaptcha_response_field").click()
        captcha_value = driver.execute_script("var win = this.browserbot.getUserWindow(); return win.promptResponse")
        self.find_element_and_wait(By.ID, "recaptcha_response_field").send_keys(captcha_value)

        #Submit form
        self.find_element_and_wait(By.ID, "submitbutton").click()


        t = False
        while t == False:
            print "t"

    def find_element_and_wait(self, how, what):
        while self.is_element_present(how, what) is False:
            print "Loading web page - waiting element %s" % what
        return self.driver.find_element(by=how, value=what)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
