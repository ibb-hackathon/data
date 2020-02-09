import pandas as pd
from selenium import webdriver
import time
import random
import os
from selenium.common.exceptions import *


path_driver = os.path.expanduser('~/Downloads/chromedriver-3')
driver = webdriver.Chrome(executable_path=path_driver)
url = 'http://www.istanbulhastaneleri.net/devlet-hastaneleri.html'
os.chdir('/Users/boyaronur/Desktop/IBB')

def go_to_target_page(url):
    driver.get(url)


def get_hospital_information(list_hospital_information):
    lis = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/ul/li')
    counter_for_lis = 0
    for li in lis:
        list_hospitals = []
        a_list = li.find_elements_by_xpath('.//a')
        for a in a_list:
            print(a.text)
            list_hospitals.append(a.text)
        br_list = li.find_elements_by_xpath('.//strong')
        for br in br_list:
            print(br.text)
            list_hospitals.append(br.text)
        try:
            list_hospital_information.append({'hastane_ismi': list_hospitals[0],
                                                'hastane_ilce': list_hospitals[2],
                                                'hastane_telefon': list_hospitals[3],
                                                'hastane_adres': list_hospitals[4]})
        except Exception as e:
            print(str(e))
    return list_hospital_information


def main():
    list_hospital_information = []
    go_to_target_page(url)
    list_hospitals = get_hospital_information(list_hospital_information)
    df_hospitals = pd.DataFrame(list_hospitals)
    df_hospitals.to_csv('hospitals.csv', index = False)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("crawler_hospital has unexpectedly stopped. \n " + str(e))
