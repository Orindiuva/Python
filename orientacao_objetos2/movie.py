class Programa:
    def __init__(self, nome, ano):
        self._nome  = nome.title(),
        self._ano   = ano,
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes +=1

    def teste(self):
        print("Isso é um teste!!!!")

    def __str__(self):
        return f"Nome: {self.nome} Ano {self.ano} - Likes {self.likes}"

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self.nome} Ano {self.ano} - Duração: {self.duracao} minutos - Likes {self.likes}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self.nome} Ano {self.ano} - {self.temporadas} temporadas - Likes {self.likes}"

class PlayList():

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    #@property
    #def tamanho(self):
        #return len(self._programas)
    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("frieds - o retorno", 2022, 11)
vingadores.dar_like()
vingadores.dar_like()


lista_programas = [vingadores, atlanta]

play_list = PlayList("meus filmes", lista_programas)

friends_1 = Serie("frieds - first seasson", 1999, 300)
play_list._programas.append(friends_1)
#print(f"Nome: {play_list.nome} - Tamanho: {play_list.tamanho}")
print(f"Nome: {play_list.nome} - Tamanho: {len(play_list)}")

#for programa in play_list.listagem:
for programa in play_list:
    #detalhe = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #print(f'{programa.nome} - {programa.ano} - {programa.likes} - D: {detalhe}')
    #programa.imprime()
    print(programa)

#Adicionando mais um filme a playlist
#cats = Filme("Cats", 2019, 140)
#play_list.programas(cats)

print(type(play_list))

#print(f"Estou ou não na lista?",  friends_1 in play_list.listagem)
print(f"Estou ou não na lista?",  friends_1 in play_list)



