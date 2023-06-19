import re


texto = "“Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23000-12"
#padrao = re.compile("[0123456789][0123456789][0123456789]-[0123456789][0123456789]")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{2}")

busca = padrao.search(texto)

if busca:
    print("Encontrou: ", busca.group())
else:
    print("Não encontrou")

print('--------------------------------------')
#http://www.bytebank.com/cambio
url = 'http://www.bytebank.brx/cambio'
#url = https://www.bytebank.com.br/cambio

#O metodo search busca um padrao DENTRO de uma string
#O compilte identifica um padrao de string

#padrao = re.compile("(http(s)?://)?(www.)?\w*(.com)?")
padrao = re.compile("(http(s)?://)?(www.)?\w*.(com)?(.br)?/cambio")
match = padrao.match(url)

if match:
    print("Encontrou url valida: ", match.group())
else:
    raise ValueError("Url não é valida!!")
