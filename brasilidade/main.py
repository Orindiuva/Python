#Aquivo utilizado para testar a lógica antes de enviar para uma classe e após a cliação da classe ela é testada a partir do main.

#https://pypi.org/ - site utilizado para busca de pacotes python

#1 - requisito - verificar se CPF contém 11 digitos

from Documento import Documento
import re

documento = Documento()
documento = documento.cria_documento("25781042806")

print(documento.valida("25781042806"))
#padrão: um numero uma letra um numero
#padrao = "[0-9][a-z][0-9]"
#padrão: três numero três digitos três número
#padrao = "\d{3} \w{3} \d{3}"
#texto = "123 1a1 133"
#padrão: um número duas letras e um número
padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1aa1 133"
resposta = re.search(padrao, texto)
print(resposta)
print(resposta.group())

#valida email- padrao 5 a 50 digitos antes do @, depois do @ de 3 a 10 digitos, um ponto, e depois do ponto de 2 a 3 digitos , um ponto, e depois do ponto de 2 a 3 digitos
print("xxxxxxxxxxxxxx - email xxxxxxxxxxxxxxxxxxx")
padrao = "\w{5,50}@\w{3,10}.\w{2,3}.(\w{2,3})?"
texto = "aaabbbcc rodrigo123@gmail.com.br"
#texto = "aaabbbcc rodrigo123@gmail.com"
resposta = re.search(padrao, texto)

print(resposta)
print(resposta.group())

#valida email- padrao 5 a 50 digitos antes do @, depois do @ de 3 a 10 letras, um ponto, e depois com.br
print("xxxxxxxxxxxxxx - email xxxxxxxxxxxxxxxxxxx")
padrao = "\w{5,50}@[a-z]{2,10}.com.br"
texto = "aaabbbcc rodrigo123@gmail.com.br"
resposta = re.search(padrao, texto)

print(resposta)
print(resposta.group())

print("xxxxxxxxxxxxxx - Telefone -  xxxxxxxxxxxxxxxxxxx")
#padrao_molde = (xx) aaaa-wwww
padrao = "[0-9]{2}[0-9]{4,5}-[0-9]{4}"
telefone = "O meu telefone é 119729-9871 o da Kátia é 1195724-6399"
#resposta = re.search(padrao, telefone)
#Retorna uma lista com todas as referência encontradas no texto
resposta = re.findall(padrao, texto)
#print(resposta)

from TelefonesBr import TelefonesBr
telefone = "5519123451235"
padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
resposta = re.search(padrao, telefone)
print(resposta.group())
print(resposta.group(1))
print(resposta.group(2))
print(resposta.group(3))
print(resposta.group(4))

print("xxxxxxxxxxxxxx - Telefone -  xxxxxxxxxxxxxxxxxxx")

numero = "5511972939871"
telefone = TelefonesBr(numero)
print(telefone)


print("xxxxxxxxxxxxxx - datetime -  xxxxxxxxxxxxxxxxxxx")

from dataBr import DataBr
import locale

locale.setlocale(locale.LC_TIME, "pt_BR")
'''
dataBr = DataBr()
print(dataBr.momento_cadastro)
print(dataBr.momento_cadastro.strftime("%d/%m/%Y %H:%M:%S"))
print(dataBr.momento_cadastro.strftime("%A %m %Y %H:%M:%S"))
print(dataBr.mes_cadastro())
print(dataBr.dia_semana())

dataBr = DataBr()
print(dataBr)
print(dataBr.dia_semana())
print(dataBr.mes_cadastro())

'''

'''
import locale
locale.setlocale(locale.LC_TIME, "pt_BR")
from datetime import datetime, timedelta, date

today = datetime.today()
amanha = datetime.today() + timedelta(days=1)
print(today - amanha)
print(amanha - today)

date_time_str = '04/06/1999 17:00'

inicio = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
print(inicio)

total_together = today - inicio
print(total_together)
print("Years: {:.2f}".format(total_together.days/365))


dataBr = DataBr()
print("tempo de cadastro:", dataBr.tempo_cadastro())
'''
print("xxxxxxxxxxxxxx - Endereço -  xxxxxxxxxxxxxxxxxxx")


from acesso_cep import BuscaEndereco
endereco = BuscaEndereco('04130080')
bairro, localidade, uf = endereco.acessa_via_cep()
print(bairro, localidade, uf)



print('###################### - Currency ########################')

import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

valor_em_dolar_formatado = locale.currency(12.4593681)
print(valor_em_dolar_formatado)

valor_em_dolar_formatado = locale.currency(15000.0, grouping=True)
print(valor_em_dolar_formatado)



usuario = input('Insira seu login: ')
print('‘Olá, ' + usuario)
