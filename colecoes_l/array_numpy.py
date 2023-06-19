import array as arr
import numpy as np

#Com os arrays temos acesso aleatórios aos elementos. Ele tem uma eficácia melhor principalmente quando trabalhar com números.
#O array permite armazenar dados somente de um mesmo tipo, no entanto,
# quando precisamento de alto desempenho de funções matematias com python utilizamos a biblioteca numpy

arr.array('d', [1, 2.5])
print(arr)


numeros = np.array([1,2,3,4,5,6,7])
print(numeros)
numeros+=2
print(numeros)
print(numeros[3:])


idades = [10, 20, 11, 28, 39, 99, 1, 30]
#for i in range(len(idades)):
    #print(i, idades[i])

print(range(len(idades))) #lazy
print(list(range(len(idades)))) #força a geração dos valores

print(list(enumerate(idades)))

for k, v in enumerate(idades):
    print(k, v)

usuarios = [('marcelo', 46, 1997), ('katia', 45, 1998), ('antonio', 11, 2013)]

#for nome, idade, nascimento in usuarios:
    #print(nome)

print(idades)
print(sorted(idades))
print(idades)
print('---------------------------')
idades.sort()
print(idades)
print(sorted(idades, reverse=True))
print('---------------------------')
print(reversed(idades))
print(list(reversed(idades)))