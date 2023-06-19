#Lista são mutáveis e os elementos dentro de uma lista são dos mesmo tipo ou de um tipo base comum a todos os elementos.
#O acesso a um elemento de uma lista é a partir do seu index.

def nova_lista(lista = []):
    print(len(lista), lista)
    lista.append(13)

#Quando chamo o metodo nova_lista mais de uma vez, a variavel default é reutilizada, pois ainda há uma referência dela
#em memória
nova_lista()
nova_lista()
nova_lista()
nova_lista()

#É boa prática ter uma referência imutável, nesse caso, o parâmetro deve ser inicializado com None e a lista
#ser instanciada detro do método.

def nova_lista_boa_pratica(lista = None):
    if lista == None:
        lista = list()
    lista.append(13)
    print(len(lista), lista)

print('xxxxxxxxxxx ---- xxxxxxxxxxxxxxxxxxxxxxxxx')
nova_lista_boa_pratica()
nova_lista_boa_pratica()
nova_lista_boa_pratica()
nova_lista_boa_pratica()
