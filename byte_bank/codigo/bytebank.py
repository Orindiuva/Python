from datetime import date
import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario


    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_completo = nome_completo.split(" ")
        sobre_nome = nome_completo[-1]
        return sobre_nome

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("O salário é muito alto para receber um bônus!")
        return valor

    def descrescimo_salario(self):
        if(self._eh_diretor()):
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def _eh_diretor(self):
        sobreno_diretores = ["Miranda", "Silva", "Barbosa"]
        return self._salario >= 100000 and (self.sobrenome() in sobreno_diretores)

    def __str__(self):
        salario_formatado = locale.currency(self._salario, grouping=True)
        return f'Funcionario({self._nome}, {self._data_nascimento}, {salario_formatado})'