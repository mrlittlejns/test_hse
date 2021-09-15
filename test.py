from typing import List

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(r"C:\Users\mrnex\Downloads\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
print ('alohadance')
pages = 7 #количество страниц. по сути цифра, определяющая сколько раз будет проходить цикл for page in range
links = []
total = []
for page in range(0, pages):
    #в цикле я указываю основную ссылку и показываю, что в конце ссылки надо менять число при окончании каждого цикла
    url = 'https://realty.yandex.ru/leningradskaya_oblast/snyat/kvartira/bez-posrednikov/?page=' + str(page) + '&sort=DATE_DESC'
    driver.get(url)
    time.sleep(2)
    event_infoes = driver.find_elements_by_class_name('OffersSerpItem__info')
    for event_info in event_infoes:
        storelinks = event_info.find_element_by_class_name('Link').get_attribute("href")
        print (storelinks)
        new = (storelinks)
        links.append(new)
print (links)

for link in links:
    driver.get(link)
    time.sleep(1)
    event_infoes = driver.find_elements_by_class_name('Offer')
    for event_info in event_infoes:
        try:
            description = event_info.find_element_by_class_name('OfferTextDescription__text').text
        except:
            description = 'Error'
        try:
            price = event_info.find_element_by_class_name('price').text
        except:
            price = 'Error'
        try:
            square = event_info.find_element_by_class_name('ColumnsList__item').text
        except:
            square = 'Error'
        try:
            place = event_info.find_element_by_class_name('OfferHeader__address').text
        except:
            place = 'Error'
        try:
            tittle = event_info.find_element_by_class_name('OfferHeader__title').text
        except:
            tittle = 'Error'
        try:
            metro = event_info.find_element_by_class_name('OfferHeaderLocation__stations').text
        except:
            metro = 'Error'
        try:
            views = event_info.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span').text
        except:
            views = 'Error'
        try:
            date = event_info.find_element_by_class_name('OfferPublishedDate').text
        except:
            date = 'Error'
        try:
            ssilka = link
        except:
            ssilka = 'Error'
        storage = (description, price, square, place, tittle, metro, views, date, ssilka)
        total.append(storage)

driver.close()
df = pd.DataFrame(total, columns=['description','price','square','place','tittle','metro','views','date','ssilka'])
df.to_csv('loyandextrtrt.csv')
print ('389')
