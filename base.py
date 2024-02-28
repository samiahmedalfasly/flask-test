from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation", ])
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")
    options.add_argument('start-maximized')
    # options.add_argument("--disable-extensions")
    # options.add_argument("--enable-cookies")
    # options.add_argument("--enable-javascript")
    # options.add_argument("--headless")
    # options.add_argument('--user-data-dir=C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data')
    # options.add_argument('--profile-directory="ندى')
    # options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    # options.add_argument("--incognito")
    # options.add_argument("--ندى")
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager("104.0.5112.20").install()), options=options)
    return driver

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str




# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("excludeSwitches", ["enable-automation", ])
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")
# options.add_argument('start-maximized')
# options.add_argument("---disable-extensions")
# # options.add_argument('--user-data-dir=C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('--profile-directory="ندى')
# # options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
# # options.add_argument("--incognito")
# options.add_argument("--ندى")
# # options.add_argument('--headless')
# # options.add_argument('--no-sandbox')
# # options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
