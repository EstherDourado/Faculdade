"""
Dicas de filmes para adicionar na Fila
Maverick
Predador
Horas de Desespero
Jack Reacher
Jason Bourne
Eclipse Mortal
"""
class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.indice_leitura = 0
        self.indice_escrita = 0
        self.tamanho = 0
#Verifica se a fila está vazia
    def esta_vazia(self):
        return self.tamanho == 0
#Verifica se a fila está cheia
    def esta_cheia(self):
        return self.tamanho == self.capacidade
#Inserindo filmes na fila
    def enfileirar(self, filme):
        if not self.esta_cheia():
            self.fila[self.indice_escrita] = filme
            self.indice_escrita = (self.indice_escrita + 1) % self.capacidade
            self.tamanho += 1
        else:
            print('A fila está cheia. Não é possível adicionar mais filmes.')
#Removendo filmes da fila
    def desenfileirar(self):
        if not self.esta_vazia():
            filme_removido = self.fila[self.indice_leitura]
            self.fila[self.indice_leitura] = None
            self.indice_leitura = (self.indice_leitura + 1) % self.capacidade
            self.tamanho -= 1
            print('Você removeu: ', filme_removido)
        else:
            print('A fila está vazia. Não é possível remover filmes.')

    def quantidade_de_filmes(self):
        return self.tamanho

    def buscar_por_nome(self, nome):
        for i in range(self.tamanho):
            indice = (self.indice_leitura + i) % self.capacidade
            if self.fila[indice] == nome:
                return f'O filme "{nome}" foi encontrado na posição {indice + 1}.'
        return f'O filme "{nome}" não foi encontrado na fila.'
#Mostra todos os filmes inseridos na fila
    def listar_filmes(self):
        if not self.esta_vazia():
            print("Lista de filmes:")
            for i in range(self.tamanho):
                indice = (self.indice_leitura + i) % self.capacidade
                filme = self.fila[indice]
                print(f"Índice {indice + 1}: {filme}")
        else:
            print('A fila está vazia. Não há filmes para listar.')
#Definindo a capacidade da fila
fila_de_filmes = FilaCircular(5)
#Menu 
while True:
    print('''
        [1] Inserir Filme
        [2] Remover Filme
        [3] Quantidade de Filmes
        [4] Busca por nome de Filme
        [5] Listar Filmes
        [6] Sair
    ''')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        if not fila_de_filmes.esta_cheia():
            filme = input('Adicione um filme: ')
            fila_de_filmes.enfileirar(filme)
            print('Você adicionou: ', filme)
        else:
            print('A fila está cheia. Não é possível adicionar mais filmes.')

    elif opcao == 2:
        fila_de_filmes.desenfileirar()

    elif opcao == 3:
        quantidade = fila_de_filmes.quantidade_de_filmes()
        print('Quantidade de filmes:', quantidade)

    elif opcao == 4:
        nome_filme = input('Qual filme você está procurando?: ')
        encontrado = fila_de_filmes.buscar_por_nome(nome_filme)
        print(encontrado)

    elif opcao == 5:
        fila_de_filmes.listar_filmes()

    elif opcao == 6:
        print('Fim do programa')
        break

    else:
        print('Opção inválida. Tente novamente.')