from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait      #Permite esperar um tempo antes de jogar um erro
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions   # Lança diferetes tipos de erros conforme indicado
import openpyxl
from time import sleep
import os



class PesquisaSiteCorreios:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver.exe',options=chrome_options)
        #self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException]
        )
        
        
    def iniciar(self):    
        self.paginaCorreios()
        self.preencheLista()
        self.pesquisaObjetos()
        self.resultadoPesquisa()
        print("Finalizando Programa")


    def paginaCorreios(self):
        self.driver.get("https://www2.correios.com.br/sistemas/rastreamento/default.cfm")
          
    
    def preencheLista(self):
        while True:
            resposta = str(input("Digite o(s) código(s) de rastreio ou caso queira sair digite 'sair':")).lower()
            if resposta == 'sair' or resposta == '': 
                break
            lista_objetos.append(resposta)
            self.lista_objetos2 = lista_objetos
            print(lista_objetos)
          


    def pesquisaObjetos(self):
        for obj in self.lista_objetos2:
            pesquisa_objetos = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, 'objetos')))
            pesquisa_objetos.send_keys(obj + " ")
        pesquisa_objetos.send_keys(Keys.ENTER)


    def resultadoPesquisa(self):    
        response = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, f'div[class=column2]'))).text
        valor = 1732
        response_tratado = response[valor:]
        print(response_tratado)

lista_objetos = []
curso = PesquisaSiteCorreios()
curso.iniciar()


