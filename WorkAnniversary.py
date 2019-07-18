class WorkAnniv:

    """ Takes a csv file containing Linkin urls as input. Automatically logs into Linkedin.
    Uses webdrivers to access Linkedin profiles and scrapes them for their most
    most recent job experience. Outputs the name of the user and the date of their
    work anniversary into a csv file """

import pandas as pd
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from linkedin_scraper import Person, actions
from selenium import webdriver
from parsel import Selector
import jsonpickle

def __init__(self, filename):
    self.filename = filename

def read_csv(self):
            with open(filename, newline='') as filename:
                rd = pd.read_csv(filename, sep=',')
            return rd

def client_url(self):
        client_urls = []
        rd = read_csv(filename)
        url_list = rd
        for line in list(rd):
            client_urls.append(url_list)
            print(client_urls)
        return client_urls

def li_login_scrape(self):
    driver = webdriver.Chrome('/Users/Nick/chromedriver.exe')
    email = 'nanderson993@gmail.com'
    password = 'Nickmike93!'
    actions.login(driver, email, password)
    client_urls = client_url(self.filename)
    df = pd.DataFrame(columns=['Name', 'Work Anniversary'])
    for idx, url in enumerate(client_urls):
        experience = driver.find_elements_by_css_selector('#experience-section .pv-profile-section')
        print(experience)
        for item in experience:
            for idx2, item in enumerate(experience[0:1]):
                df.loc[idx, 'Work Anniversary'] = item.text
    return print(df)
