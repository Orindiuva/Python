from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, "pt_BR")

class DataBr():

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mes_cadastro(self):
        #mes_lista = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                 #"julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        #mes = self.momento_cadastro.month -1
        #return mes_lista[mes]
        return self.momento_cadastro.strftime("%B")

    def dia_semana(self):
        #dias_semana_lista = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
        #dia = self.momento_cadastro.weekday()
        #return dias_semana_lista[dia]
        return self.momento_cadastro.strftime("%A")

    def data_formatada(self):
      return self.momento_cadastro.strftime("%d/%m/%Y %H:%M:%S")

    def tempo_cadastro(self):
        #simula um mês de cadastro
        return (datetime.today() + timedelta(days=30)) - self.momento_cadastro