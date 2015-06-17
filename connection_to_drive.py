#!/usr/bin/python
#-*- encoding: UTF-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Declarations constantes
EMAIL = 'selepyjkmg@gmail.com'
PASSWD = 'validationJKMG'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Recup du driver Firefox
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        
        # On va sur le site de google en verifiant que c'est le bon site   
        driver.get("http://www.google.fr")
        self.assertIn("Google", driver.title)

        # Recup de l'icone de selection d'app google
        driver.find_element_by_css_selector('a.gb_ga.gb_2').click()

        # Click sur l'application drive
        driver.find_element_by_css_selector('#gb49 > span.gb_va').click()

        # On rempli l'email et on passe à la page suivante
        driver.find_element_by_id('Email').send_keys(EMAIL)
        driver.find_element_by_id('next').click()

        # Si la case 'se souvenir de moi' est cochée, on la decoche
        elem = driver.find_element_by_id('PersistentCookie')
        if elem.is_selected():
            elem.click()

        # On entre le mot de passe puis on passe à la page suivante
        elem = driver.find_element_by_id('Passwd')
        elem.send_keys(PASSWD)
        elem.send_keys(Keys.RETURN)


        raw_input('Press a Key to continue...')
        



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
