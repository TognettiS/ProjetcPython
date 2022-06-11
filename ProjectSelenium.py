from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import requests
import random
import string
import time



navegador = webdriver.Chrome()
navegador.get("https://term.ooo/4/")
time.sleep(3)
navegador.find_element(by=By.XPATH, value= '/html/body/wc-modal/div').click()
i=5

while i == 5:
    palavra = requests.get("http://papalavras-server.herokuapp.com/words/random/")
    teste = palavra.json()
    while teste['count'] != i:
        palavras = requests.get("http://papalavras-server.herokuapp.com/words/random/")
        teste = palavras.json()
    # def random_char(y):
    #     return ''.join(random.choice(string.ascii_letters) for x in range(y))
    x = teste['word']
    time.sleep(2)
    navegador.find_element(by=By.XPATH, value ='/html/body').send_keys(x)
    navegador.find_element(by=By.XPATH, value ='/html/body').send_keys(Keys.ENTER)
    time.sleep(3)
    navegador.find_element(by=By.XPATH, value ='/html/body').send_keys(Keys.BACKSPACE * i)
