
#pytest --cov=codigo tests/ --cov-report term-missing
#pytest --cov=byte_bank.codigo byte_bank/tests/ --cov-report html


from byte_bank.codigo.bytebank import Funcionario
#marcelo = Funcionario("Marcelo", 1977, 20000)
#print(marcelo)
#print(marcelo.idade())


marcelo = Funcionario("Marcelo", '04/06/1977', 100)
print(marcelo)
print(marcelo.calcular_bonus())

