import re

class Url:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __str__(self):
        return "Url: " + self.url + "\n" + "Parâmetros:" + self.get_url_param() + "\nUrl Base:" + self.get_url_base()

    def __eq__(self, other):
        return other.url == self.url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if self.url == "":
            raise ValueError("A url está vazia!")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        #padrao_url = re.compile("(http(s)?://)?(www.)?\w*.(com)?(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_param(self):
        indice_interrogacao = self.url.find("?")
        #url_base = url[:indice_interrogacao]
        url_param = self.url[indice_interrogacao+1:]
        return url_param

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    print('---------- Busca valor Parametro --------------')

    def get_param(self, parametro_busca):
        url_param = self.get_url_param()
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

url1 = Url("http://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
url2 = Url("http://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
# Busca o valor de um parâmetro
valor = url1.get_param('moedaDestino')
print(valor)
valor = url1.get_param('moedaOrigem')
print(valor)

print(url1)
print(url1 == url2)