
from botcity.core import DesktopBot
from decouple import config
from datetime import datetime,timedelta,date
import time


def Acessar_benner(self):
    bot = DesktopBot()
        
    if not self.find( "acesso_remoto", matching=0.97, waiting_time=10000):
        self.not_found("acesso_remoto")
    self.click()

    time.sleep(5)
        
    if not self.find( "maximizar", matching=0.97, waiting_time=10000):
        self.not_found("maximizar")
    self.click()
    time.sleep(15)

    if not self.find( "clicl", matching=0.97, waiting_time=10000):
        self.not_found("clicl")
    self.click()
        
    bot.page_down()
        
    time.sleep(8)  
    if not self.find( "homolog", matching=0.97, waiting_time=10000):
        self.not_found("homolog")
    self.click_relative(10, 15)

    bot.page_down()
        
    if not self.find( "benner", matching=0.97, waiting_time=10000):
        self.not_found("benner")
    self.double_click()
        
    time.sleep(30)
        
    if not self.find( "senha_remote", matching=0.97, waiting_time=10000):
        self.not_found("senha_remote")
    self.click_relative(29, 39)
        

    bot.paste(config('SENHA'))
    bot.enter()
        
def logar_benner(self):
        bot = DesktopBot()

        if not self.find( "Usuario benner", matching=0.97, waiting_time=10000):
            self.not_found("Usuario benner")
        self.click_relative(53, 17)
        

        self.click()
        
        bot.paste(config("LOGIN_BENNER"))
        bot.tab()
        bot.paste(config('SENHA_BENNER'))
        bot.enter()

def cria_coleta_e_copia_cancela(self):
    bot = DesktopBot()
    time.sleep(5)
    if not self.find( "adicionar_coleta", matching=0.97, waiting_time=10000):
        self.not_found("adicionar_coleta")
    self.click()
    
    time.sleep(5)
    if not self.find( "Servico", matching=0.97, waiting_time=10000):
        self.not_found("Servico")
    self.click()
#
    bot.paste("Coleta")
    bot.enter()
    
    time.sleep(5)
    if not self.find( "remetente", matching=0.97, waiting_time=10000):
        self.not_found("remetente")
    self.click_relative(17, 25)
#
    bot.paste("94.389.400/0001-84")
    bot.enter()
#
    if not self.find( "tomador", matching=0.97, waiting_time=10000):
        self.not_found("tomador")
    self.click_relative(18, 24)
    
    bot.paste("Remetente")
    bot.enter()
    
    if not self.find( "datasolicitacao", matching=0.97, waiting_time=10000):
        self.not_found("datasolicitacao")
    self.click_relative(10, 25)
    
    dataatual =datetime.today()
    data_futura = dataatual + timedelta(days=1)
    
    bot.paste(dataatual.strftime('%d/%m/%Y'))
    bot.enter()
    bot.paste("1930")
    bot.tab()
    bot.paste(dataatual.strftime('%d/%m/%Y'))
    bot.tab()
    bot.paste("1930")
    bot.tab()
    bot.paste(data_futura.strftime('%d/%m/%Y'))
    bot.enter()
    bot.paste("1930")
    
    if not self.find( "confirma", matching=0.97, waiting_time=10000):
        self.not_found("confirma")
    self.click_relative(30, 10)
    
    if not self.find( "ok_coleta", matching=0.97, waiting_time=10000):
        self.not_found("ok_coleta")
    self.click_relative(19, 14)
    
    bot.enter()
    time.sleep(2)
    bot.enter()
    
    if not self.find( "funcao", matching=0.97, waiting_time=10000):
        self.not_found("funcao")
    self.click_relative(22, 14)
    
    if not self.find_text( "criar_copia", threshold=230, waiting_time=10000):
        self.not_found("criar_copia")
    
    if not self.find( "confirma_copia", matching=0.97, waiting_time=10000):
        self.not_found("confirma_copia")
    self.click_relative(152, 32)
    
    bot.enter()
    time.sleep(2)

    if not self.find( "cancelado", matching=0.97, waiting_time=10000):
        self.not_found("cancelado")
    self.click_relative(22, 15)
    
    bot.tab()
    time.sleep(1)
    bot.tab()
    time.sleep(1)
    bot.tab()
    
    bot.paste('ERRO DIGITAÇÃO')
    
    bot.tab()
    
    bot.paste('ERRO DIGITAÇÃO')
    
    if not self.find( "confirmar_cancelamento", matching=0.97, waiting_time=10000):
        self.not_found("confirmar_cancelamento")
    self.click_relative(11, 10)

    if not self.find( "volta", matching=0.97, waiting_time=10000):
        self.not_found("volta")
    self.click_relative(11, 12)
    
    
    
def cria_viagem(self):
    bot = DesktopBot()
    motorista ='319.349.458-54'
    veiculo1='FFD2E98'
    veiculo2='MPX6179'

            
    if not self.find( "icon_viagem", matching=0.97, waiting_time=10000):
        self.not_found("icon_viagem")
    self.click_relative(19, 42)
    
    if not self.find( "viagem", matching=0.97, waiting_time=10000):
        self.not_found("viagem")
    self.click_relative(38, 41)
    
    if not self.find( "Nova", matching=0.97, waiting_time=10000):
        self.not_found("Nova")
    self.click()
    
    time.sleep(2)
    if not self.find( "tipo", matching=0.97, waiting_time=10000):
        self.not_found("tipo")
    self.click()

    time.sleep(2)
    bot.paste("Transferência")
    bot.tab()
    time.sleep(2)
    bot.paste('TRANSFERENCIA')
    bot.tab()
    time.sleep(2)
    bot.paste('JMV -> SAO')
    
    if not self.find( "previsa", matching=0.97, waiting_time=10000):
        self.not_found("previsa")
    self.click_relative(9, 22)
        
    bot.paste('2')
    time.sleep(1)
    bot.tab()
    time.sleep(1)
    bot.paste('0000')

    if not self.find( "veiculo1", matching=0.97, waiting_time=10000):
        self.not_found("veiculo1")
    self.click_relative(12, 22)
    bot.paste(veiculo1)
    bot.tab()

    time.sleep(2)
    
    if not self.find( "veiculo2", matching=0.97, waiting_time=10000):
        self.not_found("veiculo2")
    self.click_relative(17, 21)
    bot.paste(veiculo2)
    bot.tab()
    time.sleep(2)
    if not self.find( "motorista", matching=0.97, waiting_time=10000):
        self.not_found("motorista")
    self.click_relative(27, 21)
    
    bot.paste(motorista)

    time.sleep(2)

    


class Bot(DesktopBot):
    def action(self, execution=None):
        #Acessar_benner(self)
        #logar_benner(self)
        cria_coleta_e_copia_cancela(self)
        #cria_viagem(self)
 
        pass
        

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()











