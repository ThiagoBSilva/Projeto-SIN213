# -*- coding: utf-8 -*-

#Importando as bibliotecas necessárias
import time

#Função para carregar os valores dos arquivos para uma lista
def carregar_dados():
    lista_valores = []
    nome_arquivo = input("Insira o nome do arquivo: ")

    #Abre o arquivo e separa os valores por linha em strings, mapeia o resultado para int
    with open(nome_arquivo + '.txt', 'r') as arquivo:
        lista_valores = list(map(int, arquivo.read().splitlines()))

    arquivo.close()
    return lista_valores

#Função de ordenação por seleção
def selection_sort(vetor_elementos):
    for i in range(0, len(vetor_elementos), 1):
        indice_menor = i
        for j in range(indice_menor+1, len(vetor_elementos), 1):
            if vetor_elementos[indice_menor] > vetor_elementos[j]:
                indice_menor = j

        vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]

#Main
if __name__ == "__main__":
    vetor = carregar_dados()

    inicio = time.time()
    selection_sort(vetor)
    fim = time.time()

    print(f'### Tempo decorrido ###: {fim - inicio}')
