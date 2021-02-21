# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""
import requests
import bs4
import html5lib
import selenium
from selenium import webdriver


# class ChromeAuto:
#     def __init__(self):
#         self.driver_path = path


def selenium_web(url):
    source = webdriver.Chrome().page_source()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        browser = webdriver.Chrome(chrome_options)
    try:
        browser.get(url)
        source = browser.page_source()
    except TimeoutError:
        print(TimeoutError.errno)
    finally:
        return source


def web_soup(source: webdriver.Chrome().page_source):
    soup1 = bs4.BeautifulSoup()
    try:
        source.title()
        soup = bs4.BeautifulSoup(content, features="html5lib")
    except ValueError:
        return ""
    finally:
        return soup


def main():

    url = "https://www.amazon.com/Fire-Tablet-7/dp/B07HZQBBKL/ref=sr_1_1?crid=ZWPC86KXCSL0&dchild=1&keywords=amazon+kindle&qid=1604758047&sprefix=amazon+kin%2Caps%2C296&sr=8-1"

    source = selenium_web(url)
    s1 = web_soup(source)
    print(s1)
    # print(type(s1.find_all('title')))
    pass


if __name__ == "__main__":
    main()
