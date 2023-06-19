url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

#Sanitização da url
#url = " ".strip()

#Validação da url
if url == "":
    raise ValueError("A url está vazia!")

url_base = url[0:26]
print(f"url base: {url_base}")
url_parm = url[27:43]
print(f"url param: {url_parm}")

print('---------- xxxxxxxxxxxxx --------------')

url_fatiada = url.split('?')
print("Base", url_fatiada[0])
print("Param", url_fatiada[1])

print('---------- xxxxxxxxxxxxx --------------')
indice_interrogacao = url.find("?")
print("Find:", indice_interrogacao)
print("url base:", url[:indice_interrogacao])
url_param = url[indice_interrogacao+1:]
print("url param:", url_param)

print('---------- Busca valor Parametro --------------')

def get_param(parametro_busca):
    indice_parametro = url_param.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    #print("Valor do indice: ", indice_valor)
    indice_e_comercial = url_param.find('&', indice_valor)
    #print("indice_e_ecomerical:", indice_e_comercial)
    valor=""
    if indice_e_comercial == -1:
        valor = url_param[indice_valor:]
    else:
        valor = url_param[indice_valor:indice_e_comercial]
    return valor

# Busca o valor de um parâmetro
valor = get_param('moedaDestino')
print(valor)
valor = get_param('moedaOrigem')
print(valor)