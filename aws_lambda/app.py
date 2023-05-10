from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict
import re, json

# from fake_useragent import UserAgent


def lambda_handler(event, context):
    # TODO implement
    chrome_options = Options()
    chrome_options.binary_location = '/opt/chrome/chrome'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280x1696")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--remote-debugging-port=9222")
        
    driver = webdriver.Chrome('/opt/chromedriver', options=chrome_options)
    driver.get("https://www.lanutrition.fr/les-aliments-riches-en-oxalate")
    data = OrderedDict()

    ############################################################################

    h4 = driver.find_elements(By.TAG_NAME, 'h4')

    for i, titre in enumerate(h4) :
        if i < 3:
          data[f"tableau{i+1}"] = [[titre.text],[""]] # je crée une fausse ligne pour "span" les entetes des tableaux
        elif i >= 3:
          data[f"tableau4"] = [['Corps gras, (tous à moins de 5mg/portion)'],[""]]         
          data[f"tableau{i+2}"] = [[titre.text],[""]] 
        elif i >= 7:
            break

    # print('titre :', data)

    tableaux = driver.find_elements(By.TAG_NAME, 'table')
    entetes = [] 

    for i, tableau in enumerate(tableaux) :
        
        if i == 0 :
            entetes_list = tableau.find_elements(By.CSS_SELECTOR, 'tbody tr td')[0:3]
            for element in entetes_list:
                entetes.append(element.text)

        sublist = []
        subsublist = []

        # je supprime les mg/portions qui bugguent
        content_temp = tableau.find_elements(By.CSS_SELECTOR, 'tbody tr td')[3:]

        if i == 3:
            # corps gras
            content_temp = tableau.find_elements(By.CSS_SELECTOR, 'tbody tr td')[1:]
            
        for j, element in enumerate(content_temp):
            subsublist.append(element.text)
            if (j+1)%3 == 0:
                sublist.append(subsublist)
                subsublist = []
            if (j+1)%3 != 0 and j == len(content_temp)-1:
                sublist.append(subsublist)

        if i == 3:
            data[f"tableau{i+1}"] += [" "] + [" "] # pour le span de mg/portion
        else:
            data[f"tableau{i+1}"] += [entetes] + [" "] # pour le span de mg/portion

        data[f"tableau{i+1}"] += sublist
        if i >= 7:
            break

    driver.quit()

    return data