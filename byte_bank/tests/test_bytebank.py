#pytest --cov=codigo tests/ --cov-report term-missing
#pytest --cov=byte_bank.codigo byte_bank/tests/ --cov-report html
#pytest --cov  --cov-report html - apos adicionar a parametrizacao daexecucao no arquivo .coveragerc
from byte_bank.codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):

        entrada = '13/03/2000' #Given - contexto
        esperado = 23
        funcionario_teste = Funcionario("Marcelo", "13/03/2000", 111111)
        resultado = funcionario_teste.idade() #when - ação
        assert resultado == esperado #Then - desfecho


    def test_quando_sobrenome_recebe_Marcelo_Silva_deve_retornar_Silva(self):
        entrada = "Marcelo Silva"  #Given - contexto
        esperado = "Silva"
        funcionario_teste = Funcionario(entrada, "04/06/1977", 22222222)
        resultado = funcionario_teste.sobrenome()#When - ação
        assert resultado == esperado #Then - desfecho

    #@mark.skip
    def test_quando_decrescimo_salario_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #Given - contexto
        entrada_nome = "Marcelo Andre da Silva"
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, "04/06/1977", entrada_salario)
        funcionario_teste.descrescimo_salario()
        resultado = funcionario_teste.salario
        assert  resultado == esperado

    #@mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000 #Given - contexto
        esperado = 100
        funcionario_teste = Funcionario("Marcelo Silva", "04/06/1977", entrada_salario)
        resultado = funcionario_teste.calcular_bonus() #When - acao
        assert esperado == resultado

    #@mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000  # Given - contexto
            funcionario_teste = Funcionario("Marcelo Silva", "04/06/1977", entrada_salario)
            resultado = funcionario_teste.calcular_bonus()  # When - acao
            assert resultado





