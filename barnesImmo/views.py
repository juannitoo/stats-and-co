from django.shortcuts import render
from bs4 import BeautifulSoup
import requests, re

# sur wsl mieux chromium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent


# https://github.com/SergeyPirogov/webdriver_manager

# Create your views here.
def home(request):

    url_leboncoin = "https://www.leboncoin.fr/"
    url_seloger = "https://www.seloger.com/"
    url_locationsaintjeandeluz = "http://www.locationsaintjeandeluz.fr/"

    ####
    url = url_seloger

    # requests bs4
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')


    # selenium 4
    chrome_options = webdriver.ChromeOptions() 
    ua = UserAgent()
    user_agent = ua.random
    # chrome_options.add_argument('--no-sandbox') # obligé en 1er si nécessaire
    chrome_options.add_argument('--headless') # unlock devtools fail
    chrome_options.add_argument(f'--user-agent={user_agent}') # unlock devtools fail


    driver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), 
        chrome_options=chrome_options
        )
    driver.get(url)
    title = driver.title

    # h1 = driver.find_element(By.TAG_NAME, 'h1')
    # btn_se_connecter = driver.findElement(By.XPATH, "//*[@id='container']/div[2]/div/div[1]/header/nav/div[1]/button")

    html = driver.find_element(By.TAG_NAME, 'html').get_attribute("outerHTML")
    # print(h1)

    driver.quit()


    nom_fichier = re.split(r'\.', url)[1]
    print(f'{nom_fichier}.html')
    with open(f'save_scrap/{nom_fichier}.html', 'w') as fichier:
        fichier.write(str(html))

    context={}
    # context["titre"] = h1

    return render(request, 'barnesImmo/home.html', context)
