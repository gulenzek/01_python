# -*- coding: utf-8 -*-
"""
https://anaconda.org/anaconda/selenium

Anaconda prompt acalim:
conda install -c anaconda selenium

headless

web scraping al
scrapy
"""
from selenium import webdriver

def main():
    url = "https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun"
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()  # Caglar only
    driver.get(url)
    source = driver.page_source
    print(source)

    search_box = driver.find_element_by_id("search-query")
    search_box.send_keys("usd")

    search_a_element = driver.find_element_by_xpath("/html/body/header/div/div[2]/div/form/a")
    search_a_element.submit()


if __name__ == "__main__":
    main()
