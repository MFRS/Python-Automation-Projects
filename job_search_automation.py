# search through website and attempt different links until it finds the careers or jobs section

from bs4 import BeautifulSoup
import urllib.request
import urllib.robotparser as urobot
import hashlib
import re
import pandas as pd
from bs4 import BeautifulSoup as Soup
import os
from time import sleep
import importlib.util
import sys
import os.path
import sys
import os.path
import os
from typing_extensions import final
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from usp.tree import sitemap_tree_for_homepage
import requests

try:
    spec = importlib.util.spec_from_file_location("generalfunctions", r"E:\GitHub\AdobeScripts\functionsOnly\classes\generalfunctions.py")
    gf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gf)
except:
    try:
        spec = importlib.util.spec_from_file_location("generalfunctions", r"/Users/miguelsalvador1/Documents/GitHub/AdobeScripts/functionsOnly/classes/generalfunctions.py")
        gf = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gf)
    except:
        spec = importlib.util.spec_from_file_location("generalfunctions", r"C:\Users\Migue\Documents\GitHub\AdobeScripts\functionsOnly\classes\generalfunctions.py")
        gf = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gf)
sys.modules["generalfunctions"] = gf
from generalfunctions import generalFunctions as gfi

# open html file and extract all href with "games"

def writeDownJobListings(array_vars):
    iComesFrom = array_vars[0]
    mainWebsite = array_vars[1]
    jobTitle = array_vars[2]
    jobUrl = array_vars[3]
    # ^Coming from non scraped website
    if iComesFrom == 1:
        # pass
        print(f"{mainWebsite} There is a {jobTitle} position here - {jobUrl}")



def get_game_websites():
    with open(game_websites_page, encoding="utf-8") as file:
        data = file.read()
    return data




def searchDomainsForSpecificJobRoles(array_vars):
    url = array_vars[0]
    aButtonNames = array_vars[1]
    aDesiredJobTitles = array_vars[2]
    cookiesNames = array_vars[3]
    import sys
    import os.path
    import os
    from typing_extensions import final
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep
    # os.environ['PATH'] += r"C:\PathPrograms\seleniumDrivers\chromedriver.exe"
    sChromeDriverPath = r"C:\PathPrograms\seleniumDrivers\chromedriver.exe"
    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = ChromeService(executable_path=sChromeDriverPath)
    driver = webdriver.Chrome(options=options)
    # ^ find button with one of text in array
    # print(url)
    driver.get(url)
    # wait till website loads
    sleep(6)
    for current_button in aButtonNames:
        # print(current_button)
        try:
            # element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '{current_button}')]")))            # click on button that contains text equals to current_button
            # print(element)
            # element.click()
            driver.find_element(by=By.XPATH, value=f"//*[contains(text(), '{current_button}')]").click()
            sleep(6)
            # ^try to find the button with cookies by using cookiesNames
            # for current_cookie_name in cookiesNames:
            #     try:
            #         driver.find_element(by=By.XPATH, value=f"//*[contains(text(), '{current_cookie_name}')]").click()
            #         sleep(2)
            #     except:
            #         pass
            # else:
            #     for current_cookie_name in cookiesNames:
            #         # upper case the cookie name
            #         current_cookie_name = current_cookie_name.upper()
            #         try:
            #             driver.find_element(by=By.XPATH, value=f"//*[contains(text(), '{current_cookie_name}')]").click()
            #             sleep(2)
            #         except:
            #             pass
            # while doesnt find name, keep looking from database 

            # wait for new page
            # get all jobs containing word from array using beautiful soup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # print(soup)
            # look for all title inside a tags
            all_job_titles = []
            for a in soup.find_all('a'):
                # print(a.string)
                # get text from "a"
                if a.text != None:
                    current_job_titles = {}
                    current_job_titles['job_title'] = a.text
                    current_job_titles['company_url'] = a['href']
                    all_job_titles.append(current_job_titles)
            # print(all_job_titles)
              # if your find a job that contains a word from an array print it

            # ^ loop through all_job_titles['job_title'] and check if it contains a word from aDesiredJobTitles
            for current_job in all_job_titles:
                # lower all variables
                current_job_title = current_job['job_title'] 
                current_job_title = str(current_job_title.lower())
                # lower all variables in aDesiredJobTitles
                lowerSearch =  [current_desired_job_title.lower() for current_desired_job_title in aDesiredJobTitles]
                # print(lowerSearch)
                for current_desired_job_title in lowerSearch:
                    current_desired_job_title = str(current_desired_job_title)
                    if current_desired_job_title in current_job_title:
                        writeDownJobListings([1,url, current_job_title, current_job['company_url']])
            # break
        except Exception as e:
            print(e)
            pass


def search_domains_for_careers_pages(uUrl):
    paths = ['jobs', 'careers', 'opportunities', 'join-us']
    # if domain already has one of the paths, skip it
    domains = uUrl
    results = []
    # apply all paths to the domain
    for path in paths:
        url = f'{domains}/{path}'
        r = requests.get(url)
        # print(r.status_code)
        if r.status_code == requests.codes.OK:
            results.append(url)
            break
            # print(url)
    return results



def selenium_tryand_search_for_buttons(array_vars):
    url = array_vars[0]
    aButtonNames = array_vars[1]
    aDesiredJobTitles = array_vars[2]
    driver = selenium_launch([url, aDesiredJobTitles])
    sleep(5)
    #the idea is to keep pressing the button with text from aButtonNames until there's no more buttons with that name
    for current_button in aButtonNames:
        print("\n"*2)
        print(current_button)
        hasMoreButtons = True
        while hasMoreButtons == True:
            try:
                
                driver.find_element(by=By.XPATH, value=f"//*[contains(text(), '{current_button}')]").click()
                print("\n"*5)
                print("found button")
                print("\n"*5)
                sleep(1.5)
            except:
                print("\n"*2)
                print("no more buttons")
                hasMoreButtons = False
    # ^ go through all divs and get text
    selenium_goThroughAllDivsAngGetText([url, aDesiredJobTitles, driver])


def selenium_launch(array_vars):
    url = array_vars[0]
    aDesiredJobTitles = array_vars[1]
    import sys
    import os.path
    import os
    from typing_extensions import final
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep
    # os.environ['PATH'] += r"C:\PathPrograms\seleniumDrivers\chromedriver.exe"
    sChromeDriverPath = r"C:\PathPrograms\seleniumDrivers\chromedriver.exe"
    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = ChromeService(executable_path=sChromeDriverPath)
    driver = webdriver.Chrome(options=options)
    # ^ find button with one of text in array
    # print(url)
    driver.get(url)
    sleep(5)
    return driver
    # go through all divs and get text
    
def selenium_goThroughAllDivsAngGetText(array_vars):
    url = array_vars[0]
    aDesiredJobTitles = array_vars[1]
    driver = array_vars[2]
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for current_job in aDesiredJobTitles:
        for current_tag in soup.findAll(text=re.compile(current_job)):
            writeDownJobListings([1,url, current_job, current_tag.parent])

def searchForDesiredJobs(array_vars):
    url = array_vars[0]
    aButtonNames = array_vars[1]
    aDesiredJobTitles = array_vars[2]
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")
    # print(soup)
    # get all text from all tags
    # print(aDesiredJobTitles[0])
    for current_job in aDesiredJobTitles:
        child_soup = soup.findAll(text=re.compile(current_job))
        if len(child_soup) == 0:
            print("ran searchForDesiredJobs, child_soup was empty")
            driver = selenium_launch([url, aDesiredJobTitles])
            selenium_goThroughAllDivsAngGetText([url, aDesiredJobTitles,driver])
        else:
            # search for next href after div containing child_soup text
            for current_tag in child_soup:
                # if current_tag contains a href
                if current_tag.parent.name == "a":
                    # print(current_tag.parent['href'])
                    if "https" not in str(current_tag.parent['href']):
                        # remove everything after the last / from url
                        url = url[:url.rfind('/')]

                        writeDownJobListings([1,url, current_job, url + str(current_tag.parent['href'])])
                    else:
                        writeDownJobListings([1,url, current_job, current_tag.parent['href']])
            # ^ if nothing was found in child_soup, call selenium_tryand search for buttons with text
            else:
                selenium_tryand_search_for_buttons([url, aButtonNames,aDesiredJobTitles])
            # writeDownJobListings([1,url, current_job, ])
    # print(child_soup)
    # for current_job in aDesiredJobTitles:
    #     if 


    # print(child_soup)
    # for current_job_desired_title in aDesiredJobTitles:
    #     for current_tag in soup.findAll(current_job_desired_title):
    #         print(current_tag)
            # print(current_tag.parent.parent.parent)
            # print(current_tag.parent.parent.parent.parent)
            # print(current_tag.parent.parent.parent.parent.parent)
            # print(current_tag.parent.parent.parent.parent.parent.parent)
            # print(current_tag.parent.parent.parent.parent.parent.parent.parent)
            # print(current_tag.parent.parent.parent.parent.parent.parent.parent.parent)
            # print(current_tag.parent.parent.parent.parent.parent.parent.parent.parent.parent)
            # print(current_tag.parent.parent.parent.p
        


# Pass the headers you want to retrieve from the xml such as ["loc", "lastmod"]
def isCareersDotInUrls(url,array_headers):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")
    for link in soup.findAll('a'):
        # print(link.get('href'))
        for current_header in array_headers:
            if current_header in str(link.get('href')):
                # Some websites only return the /text and not the full url
                if "https" not in str(link.get('href')):
                    # remove the last / from url
                    url = url[:url.rfind('/')]
                    return url + str(link.get('href'))
                else:
                    return str(link.get('href'))
    else:
        return None

def isSitemapAccessible(url):
    rp = urobot.RobotFileParser()
    rp.set_url(url + "/robots.txt")
    rp.read()
    # print(f"{rp.read()}\n\n\n")
    
    if rp.site_maps() != None :
    # if rp.can_fetch("*", url):
        site = urllib.request.urlopen(url)
        sauce = site.read()
        soup = BeautifulSoup(sauce, "html.parser")
        actual_url = site.geturl()[:site.geturl().rfind('/')]
        my_list = soup.find_all("a", href=True)
        # print(f"the list  {my_list}\n\n\n")
        if len(my_list) == 0:
            return False
        # ^ this website is scrapable, use
        else:
            return True
    else:
        return False


def extractSitemap(array_vars):
    urlChosen = array_vars[0]
    aButtonNames = array_vars[1]
    aDesiredJobTitles = array_vars[2]
    cookiesNames = array_vars[3]
    list_page = []
    bIsSitemapAccessible = isSitemapAccessible(urlChosen)
    print(bIsSitemapAccessible)
    # ^ cannot extract sitemap
    if bIsSitemapAccessible is True:
        print("sitemap accessible")
        tree = sitemap_tree_for_homepage(urlChosen)
        # all_pages() returns an Iterator
        for page in tree.all_pages():
            # if theres a "senior-audio-designer" print it
            # if "editor" in page.url:

            list_page.append(page.url)
        print(list_page)
        # for current_page in list_page:
        #     for desiredJobTitle in aDesiredJobTitles:
        #         if desiredJobTitle in current_page:
        #             writeDownJobListings([0,urlChosen, desiredJobTitle, current_page])
    # ^can extract sitemap
    else:
        searchForDesiredJobs([urlChosen, aButtonNames, aDesiredJobTitles])
        # print("sitemap not accessible")
        pass
        # websites = search_domains_for_careers_pages(urlChosen)
        # for website in websites:
        #     searchDomainsForSpecificJobRoles(
        #         [website, aButtonNames, aDesiredJobTitles,cookiesNames])


def add_varieties_to_list(currentList):
    newList = []
    #  add uppercase to the first letter of each word in the currentList
    for current_word in currentList:
        # adds the normal word
        newList.append(current_word)
        # adds the word with the first letter uppercase
        current_word = current_word.title()
        newList.append(current_word)
        # adds the word with all letters uppercase
        current_word = current_word.upper()
        newList.append(current_word)
        
    return newList


# url = "https://www.sumo-digital.com"
game_websites_page = r"C:\Users\Migue\Desktop\scripts\python\job_search\bookmarks.html"
# get all the websites from the game websites page
game_websites = get_game_websites()
# extrace as html
game_websites = game_websites.split("\n")
# remove empty lines
game_websites = [website for website in game_websites if website != ""]
# remove all lines that dont have the TAG "games"
game_websites = [website for website in game_websites if "games" in website]
# extract all hrefs
game_websites = [website.split('"')[1] for website in game_websites]
# print(game_websites)
game_websites = ["https://massivemonster.co/"]
# print(game_websites)
for current_website in game_websites:
    careers_urls = add_varieties_to_list(["careers","jobs","opportunities","join us"])
    button_varieties = ["View All Openings","Load more","jobs","opportunities","join us"]
    isCareerDot = isCareersDotInUrls(current_website, careers_urls)
    job_desired = ["Senior Backend Engineer"]
    accept_cookies_varieties = ['accept all cookies', 'accept all', 'accept all cookies and close', 'accept all cookies and continue']
    # print 20 line breaks
    print("\n"*20)
    print(isCareerDot)
    if isCareerDot != None:
        extractSitemap([isCareerDot, button_varieties,job_desired,accept_cookies_varieties])
    else:
        extractSitemap([current_website, button_varieties,job_desired,accept_cookies_varieties])
    # break

# obtain all urls from "https://rebellion.com/"
# if "careers" in url, then print
# use beautifulsoup to extract all urls

# & try selenium to get job refs
