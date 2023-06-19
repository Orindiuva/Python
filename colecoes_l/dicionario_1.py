meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                    'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                        'Luiza': '4567-7654'}

meus_contatos.update(contatos_do_pedro)

for contato in meus_contatos:
    print(contato)

meus_contatos = { nome: '9' + meus_contatos[nome] for nome in meus_contatos}

for key, value in meus_contatos.items():
    print(key, value)

valores = meus_contatos.values()
print(valores)