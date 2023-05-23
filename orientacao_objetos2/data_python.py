from datetime import date
from datetime import datetime, timezone, timedelta

#%d - O dia do mês representado por um número decimal (de 01 a 31)
#%m - O mês representado por um número decimal (de 01 a 12)
#%Y - O ano representado por um número decimal incluindo o século
#%H - A hora representada por um número decimal usando um relógio de 24 horas (de 00 a 23)
#%M - O minuto representado por um número decimal (de 00 a 59)

data_atual = date.today()
print(data_atual)
print("day:", data_atual.day, "month: ", data_atual.month, "year:", data_atual.year)
print(data_atual.strftime("%d/%m/%Y"))
print('----------- xxx ---------------')
date_time = datetime.today()
print(date_time)
print(date_time.strftime("%d/%m/%y %H:%M%S"))
print('----------- xxx ---------------')

#Convertendo um String em datetime
data_e_hora_em_texto = '01/03/2018 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
print(data_e_hora.strftime('%d/%m/%Y %H:%M'))
print('----------- xxx ---------------')
#Timezone
data_e_hora_atuais = datetime.now()
#Fuso horario Brasil
diferenca = timedelta(hours= -3)
#fuso horario - Portugal
#diferenca = timedelta(hours= +1)

fuso_horario = timezone(diferenca)
print(fuso_horario)

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("‘%d/%m/%Y %H:%M")

print(data_e_hora_sao_paulo_em_texto)


#from pytz import timezone
import pytz
print('-------- pytz ---------------')
data_e_hora_atuais = datetime.now()
fuso_horario = pytz.timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)

#Lista de fuso horarios suportados
#for tz in pytz.all_timezones:
    #print(tz)