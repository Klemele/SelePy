#!/usr/bin/python
#-*- encoding: UTF-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

# Declarations constantes
SITE_URI = 'http://animerush.tv'
SITE_TITLE = 'Watch Anime Online in High Quality for Free - AnimeRush.tv'
ANIMES_PATH = '/home/mikhadho/Desktop/animes.txt'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Recup du driver Firefox
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        
        # On va sur le site animerush en verifiant que c'est le bon site   
        driver.get(SITE_URI)
        self.assertIn(SITE_TITLE, driver.title)

        # Recuperation de la liste d'animes
        f = open(ANIMES_PATH)
        tmp = f.readlines()
        f.close()
        animes = {}
        for e in tmp:
            title = e.replace('\n', '').split(';')[0]
            eps = e.replace('\n', '').split(';')[1]
            animes[title] = eps

        # Recuperation des 5 episodes les plus recents
        err = True
        while err:
            try:
                elements = driver.find_elements_by_class_name('episode')
                for element in elements[:5]:
                    # On check si l'espisode est sous-titré
                    details = element.find_element_by_tag_name('div')
                    infos = details.find_element_by_tag_name('div')
                    res = infos.find_elements_by_tag_name('span')[1]
                    # Si sous-titré, on informe l'utilisateur par mail
                    if 'subbed' in res.text.lower():
                        res = details.find_element_by_tag_name('a')
                        #print res.text

                        res = details.find_element_by_tag_name('a').text.split('-')
                        res[0] = res[0].strip()
                        res[1] = res[1].strip().lower().replace('episode ', '')
                        print res
                        # Anime present dans la liste des animes suivis
                        c1 = res[0] in animes.keys()
                        # Episode non vu
                        c2 = False
                        if c1:
                            c2 = int(res[1]) > int(animes[res[0]])
                        # Si anime suivi et episode non vu, on envoi un mail
                        if c1 and c2:
                            #TODO: implémenter envoi de mail
                            print 'envoi de mail:{0} {1}'.format(res[0], res[1])
                            # Maj de la liste
                            animes[res[0]] = res[1]
                            print animes
                err = False
            except StaleElementReferenceException as e:
                print 'err, redo'

        # Reecriture du fichier animes
        f = open(ANIMES_PATH, 'w')
        for k, v in animes.items():
            f.write('{0};{1}\n'.format(k, v))
        f.close()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
