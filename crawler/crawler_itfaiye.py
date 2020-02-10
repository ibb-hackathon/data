import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


def run():
    driver = webdriver.Chrome(
        r"C:\Users\atakan.soztekin\PycharmProjects\ibbhackatonproject\crawler\drivers\chromedriver.exe")
    driver.get("http://itfaiye.ibb.gov.tr/tr/istasyonlarimiz.html")
    list_itfaiye = driver.find_element_by_class_name("listArea")
    location_list = BeautifulSoup(list_itfaiye.get_attribute("innerHTML"), "html.parser")
    itfaiyeler_info = location_list.find_all("li")
    data = list()
    for info in itfaiyeler_info:
        info_labels = info.text.split("\n")
        data.append({
            "Name": info_labels[1],
            "Location": info_labels[2],
            "Telephone": info_labels[3]
        })
    last_df = pd.DataFrame(data)
    last_df.to_csv("../files/itfaiye_info.csv")


if __name__ == '__main__':
    run()
