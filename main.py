from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 

class Whatsappbot:
    def __init__(self):
    #Mensagem que você quer enviar 
        self.mensagem = "A mensagem desejada"

    # Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupo_pessoas = ["GRUPO OU/E PESSOAS que deseja enviar a mensagem"] 
        options = webdriver.Chrome()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
    #<span dir="auto" title="Grupo ou pessoa" class="...">Grupo ou pessoa</span>
    #<div tabindex="-1" class="...">
    #<span data-testid="send" data-icon="send" class="">

        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupo_pessoa:
            grupo = self.driver.find_element_by_xpath(f"//span[@tittle='{grupo}']")
            time.sleep(4)
            grupo.click()
            chat_bot = self.driver.find_element_by_class_name('')
            time.sleep(4)
            chat_bot.click()
            chat_bot.send_keys(self.mensagem)
            botao_send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(4)
            botao_send.click()
            time.sleep(5)

bot = Whatsappbot()
bot.EnviarMensagens()


