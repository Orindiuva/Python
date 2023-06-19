
dicionario = [{"nome": "marcelo", "idade": 46}, {"nome": "katia", "idade": 45}]

print(type(dicionario))
print(type(dicionario[0]))

for registro in dicionario:
    print(registro['nome'], registro['idade'])

registro = {"nome": "marcelo", "idade": 46}
chave_nao_existe = registro.get("xpto", 0)
print(chave_nao_existe)

chave_existe = registro.get("nome", 0)
print(chave_existe)

dicionario = dict(nome="marcelo", idade=46)
print(dicionario)

dicionario['sexo'] = 'masculino'
print(dicionario)

del dicionario['sexo']
print(dicionario)

print('nome' in dicionario)

print("xxxxxxxxxxx keys xxxxxxxxxxxxxxxxx")
for chave in dicionario:
    print(chave)

for chave in dicionario.keys():
    print(chave)
print("xxxxxxxxxxx values xxxxxxxxxxxxxxxxx")
for values in dicionario.values():
    print(values)

print("xxxxxxxxxxx key:values xxxxxxxxxxxxxxxxx")
for elemento in dicionario.keys():
    print(elemento,"-",  dicionario[elemento])

for chave, valor in dicionario.items():
    print(chave,"-",  valor)

all_keys = ["chaves {}".format(chave) for chave in dicionario]
print(all_keys)


print("############## contanto numero de palavras #############################")
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)


print("############## default dict #############################")
from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)
print(aparicoes['gosto'])
print(aparicoes['gostosa'])


print("############## simplificando default dict #############################")
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] += 1

print(aparicoes)


print("xxxxxxxxxxxxxxxxxxxx ---- xxxxxxxxxxxxxxxx")
#quando o defaultdict falhar na busca pela chave, o construtor sera chamado
#Isso pode ser visto com um tipo de cache temporário

class Conta:
    def __init__(self):
        print("Criando uma nova conta")

contas = defaultdict(Conta)
contas[15] = "novaconta"
contas[15]
contas[16]
contas[16]
contas[20]
print(contas)


print("xxxxxxxxxxxxxxxxxxxx -- Counter -- xxxxxxxxxxxxxxxx")
from collections import Counter
print(type(meu_texto.split()))
aparicoes = Counter(meu_texto.split())
print(aparicoes)

print("xxxxxxxxxxxxxxxxxxxx -- Counter nome -- xxxxxxxxxxxxxxxx")
nome = "marcelo andre silva"
aparicoes = Counter(nome)
total_caracteres = sum(Counter(nome).values())

print(aparicoes, " - Total de caracteres:", total_caracteres)
print(Counter(nome.split()))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(aparicoes)
porcetagem_total =0
for letra, total_letra in aparicoes.items():
    porcentagem = round((total_letra/total_caracteres), 2) * 100
    porcetagem_total += porcentagem
    print("letra: {} total de letra: {} porcentagem: {}%".format(letra, total_letra, porcentagem))
print("Porcetagem total: ", porcetagem_total)

print("xxxxxxxxxxxxxxxxxxxxxxxxx - most common  - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
def analisa_frequencia_letra():
    proporcao = [(letra, frequencia/total_caracteres) for letra, frequencia in aparicoes.items()]
    print(type(proporcao))
    proporcao = Counter(dict(proporcao))
    for caracter, proporcao in proporcao.most_common(7):
        print("Caracter {} => {:.2f}%".format(caracter, proporcao*100))

analisa_frequencia_letra()