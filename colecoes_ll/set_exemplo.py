
marcelo = [9, 8, 9, 10, 10]
katia = [10, 10, 10, 10, 9]
notas = []
notas = marcelo.copy()
notas.extend(katia)
notas = set(notas)

for i in notas:
    print(i)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
conj = sorted(set([1, 2, 3, 3, 3, 99, 99, 100, 1, 10, 10]))

for i in conj:
    print(i)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
x= {1, 2, 3, 3, 3, 99, 99, 100, 1, 10, 10}
for i in x:
    print(i)

print('xxxxxxxxxxxxxxxxxxx - Uniao - xxxxxxxxxxxxxxxxxxxxxxxx')
data_science = {1, 3, 100, 10}
marchine_learning = {1, 3, 9}

uniao = data_science | marchine_learning
for i in uniao:
    print(i)

print('xxxxxxxxxxxxxxxxxxx - Intersecao - xxxxxxxxxxxxxxxxxxxxxxxx')
interseccao = data_science & marchine_learning

for i in interseccao:
    print(i)

print('xxxxxxxxxxxxxxxxxxx - Exclusão - xxxxxxxxxxxxxxxxxxxxxxxx')
#Todos que fizeram data science, mas nao fizeram machine learning

exclusao = data_science - marchine_learning

for i in exclusao:
    print(i)


print("xxxxxxxxxxxxxxxxx - Ou exclusivo xxxxxxxxxxxxxxxxxxxxxxxx")
#Fez data science ou machine learning
ou_exclusivo = data_science ^ marchine_learning
for i in ou_exclusivo:
    print(i)


print("xxxxxxxxxxxxxxxxx - Frozen set xxxxxxxxxxxxxxxxxxxxxxxx")
#Deixa o conjunto imutável
lista = {1, 2, 3, 5 , 6}
print(type(lista))
lista.add(100)
print(lista)
lista = frozenset(lista)
print(type(lista))
#lista.add(10000)

texto = "Ola meu nome e marcelo e eu gosto muito de nome e o nome do meu cachorro e marcelo nome muito criativo"

txt = set(texto.split())
print(txt)
