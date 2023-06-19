
from operator import attrgetter
from functools import total_ordering

#String - ordem lexigrafica
nomes = ["Rodrigo", "Fatima", "Ana", "Marcelo", ]
print(sorted(nomes))

nomes = ["Rodrigo", "Fatima", "ana", "Marcelo", ]
print(sorted(nomes))

@total_ordering
class ContaSalario:

    def __init__(self, numero):
        self._numero = numero
        self._saldo = 0

    def __eq__(self, other):
        if(type(other) != ContaSalario):
            return False
        return self._numero == other._numero and self._saldo == other._saldo

    def __str__(self):
        return "<< Numero: {} -  Saldo: {} >>".format(self._numero, self._saldo)

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        if self._saldo == other._saldo:
            return self._numero < other._numero

    @property
    def saldo(self):
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor

    def extrai_saldo(conta):
        return conta.saldo

conta_marcelo = ContaSalario(123)
conta_marcelo.deposita(500)

conta_katia = ContaSalario(222)
conta_katia.deposita(1000)

conta_leticia = ContaSalario(333)
conta_leticia.deposita(510)

lista_conta = [conta_marcelo, conta_katia, conta_leticia]

for conta in lista_conta:
    print(conta.saldo)
print('---------------extrai saldo------------------------')
for conta in sorted(lista_conta, key=ContaSalario.extrai_saldo):
    print(conta.saldo)

print('---------------------------------------')
for conta in sorted(lista_conta, key=attrgetter("_saldo")):
  print(conta)

print('---------------Less than----------------------')
print(conta_marcelo < conta_katia)
print(conta_marcelo > conta_katia)

for conta in sorted(lista_conta):
    print(conta)
print('---------------Less than - reverse ----------------------')
for conta in sorted(lista_conta, reverse=True):
    print(conta)

print('---------------Less than - Saldo iguais----------------------')
#Quando os saldos forem iguais quero order pelo id mais baixo
conta_leticia = ContaSalario(1800)
conta_leticia.deposita(500)

conta_katia = ContaSalario(3)
conta_katia.deposita(1500)

conta_marcelo = ContaSalario(223)
conta_marcelo.deposita(500)


lista_conta = [conta_katia, conta_leticia, conta_marcelo]

for conta in sorted(lista_conta):
    print(conta)


print('---- attrgetter -----')
for conta in sorted(lista_conta, key=attrgetter("_saldo", "_numero")):
    print(conta)


print('--------- Total ordering')

print(conta_leticia <= conta_katia)
print(conta_katia <= conta_leticia)
print(conta_katia == conta_leticia)
print(conta_leticia <= conta_marcelo)
print(conta_marcelo <= conta_leticia)
