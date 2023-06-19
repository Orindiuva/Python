from abc import abstractmethod, ABCMeta
class Conta(metaclass=ABCMeta):

    def __init__(self, numero):
        self._numero = numero
        self._saldo = 0

    def deposita_conta(self, valor):
        self._saldo += valor

    def __str__(self):
        return "<< Número: {} - Saldo: {}".format(self._numero, self._saldo)

    @abstractmethod
    def passa_um_mes(self):
        pass


#Tupla
print(' ------------ Tupla ------------------')
#Variação funcional (separa o comportamento dos dados)
def deposita(conta):
    saldo = conta[1] + 100
    conta = conta[0]
    return (conta, saldo)

marcelo = (123, 1000)
print(marcelo)
print(deposita(marcelo))
print(marcelo)
marcelo = deposita(marcelo)
print(marcelo)

#Aqui tenho uma tupla de contas que são imutáveis, no entanto, os objetos que estão dentro da tupla, continuam sendo mutáveis.

class ContaCorrente(Conta):

    def passa_um_mes(self):
        self._saldo -=2

class ContaPoupanca(Conta):
    def passa_um_mes(self):
        self._saldo *=1.01
        self._saldo -=3

class ContaInvestimento(Conta):
    pass
    #def passa_um_mes(self):
        #print("metodo abstrato implementado!")

#conta_inv = ContaInvestimento(1111)

conta16 = ContaCorrente(16)
conta16.deposita_conta(1000)
conta17 = ContaPoupanca(17)
conta17.deposita_conta(1000)

contas = [conta16, conta17]
for conta in contas:
    conta.passa_um_mes() #duck type
    print(conta)

print("---------------- xxxxxxxxxxxxxxxxxx ----------------")

class Outra:
    pass


print(isinstance(conta16, Conta))
print(isinstance(conta17, Conta))
print(isinstance(Outra(), Conta))