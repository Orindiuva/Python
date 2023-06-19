class IteradorHttp():

    def __init__(self):
        self.registro = open('log.txt', 'r')
        self.linha_atual = ''

    def __iter__(self):
        return self

    def __next__(self):
        self.linha_atual = self.registro.readline()

        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()

        if self.linha_atual:
            return self.linha_atual

        raise StopIteration

    #Le todo o arquivo
    def read_file(self):
        log_file = open('log.txt', 'r')
        print(log_file)
        urls = [url for url in log_file if url.startswith('http://')]

iterador  = IteradorHttp()
#iteradorHttp.read_file()
#print(next(iterador))
#print(next(iterador))
#print(next(iterador))
#print(next(iterador))
#print(next(iterador))
#print(next(iterador))
#print(next(iterador))
#print(next(iterador, 'Fim do iterador'))

for url in iterador:
    print(url)

