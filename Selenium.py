from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import requests
import random
import string
import time
import unidecode

def AbreSite():
    global navegador
    navegador = webdriver.Chrome()
    navegador.get("https://term.ooo/4/")
    time.sleep(3)

def MaximizaGuia():
    navegador.maximize_window()

def RetiraExplicacaoDoSite():
    navegador.find_element(by=By.XPATH, value= '/html/body/wc-modal/div').click()

def GeraPalavra():
    global palavrasite
    palavrasite = requests.get("https://api.dicionario-aberto.net/random")

def TransformaPalavraEmJSON():
    global palavrajson
    palavrajson = palavrasite.json()

def ProcuraPalavraCom5Letras():
    global palavrafinal
    palavrafinal = palavrajson['word']
    while len(palavrafinal) != 5:
        GeraPalavra(), TransformaPalavraEmJSON()
        palavrafinal = palavrajson['word']

def RetiraAcentuacao():
    global palavrafinal
    palavrafinal = unidecode.unidecode(palavrafinal)

def EnviaComandosDoTeclado():
    time.sleep(2)
    navegador.find_element(by=By.XPATH, value ='/html/body').send_keys(palavrafinal)
    navegador.find_element(by=By.XPATH, value ='/html/body').send_keys(Keys.ENTER)
    time.sleep(3)
    navegador.find_element(by=By.XPATH, value ='/html/body').send_keys(Keys.BACKSPACE * 5)

def Iniciar():
    AbreSite(), MaximizaGuia(), RetiraExplicacaoDoSite()
    z = 0
    while z < 9:
         GeraPalavra(), TransformaPalavraEmJSON(), ProcuraPalavraCom5Letras(), RetiraAcentuacao(), EnviaComandosDoTeclado()
         z += 1
    time.sleep(5)
    navegador.quit()

Iniciar()
