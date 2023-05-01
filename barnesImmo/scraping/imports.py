from bs4 import BeautifulSoup
import requests, re
from collections import OrderedDict

# sur wsl mieux chromium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent