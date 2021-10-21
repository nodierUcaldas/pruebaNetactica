from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd



class Source: #1)

    def __init__(self, domain, articles, urls_list):
        self.source_name=""
        self.domain=domain
        self.articles=articles
        self.urls_list = urls_list

    def build_urls(self, domain, endPoints):#2)
       list_comprehesion = []
       for i in endPoints:
           list_comprehesion.append(domain+i)

       """print(list_comprehesion)"""
       self.urls_list=list_comprehesion

       return list_comprehesion

class Article: #3)

    def _init_(self):
        url=""
        source=""
        parsed=False
        html=None
        title=""
        table_data=None

    def parse_html_title(self, xpath): #4)
        title_xpath=""

if __name__ == '__main__':
    S=Source("http/",["info1","info2","info3"],[])
    print(S.build_urls(S.domain,S.articles))



