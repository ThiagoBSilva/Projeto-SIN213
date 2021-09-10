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

#Função de ordenação por inserção
def insertion_sort(vetor_elementos):
    for i in range(1, len(vetor_elementos), 1):
        j = i-1
        valor = vetor_elementos[i]
        while(j >= 0 and valor < vetor_elementos[j]):
            vetor_elementos[j+1], vetor_elementos[j] = vetor_elementos[j], valor
            j-=1

#Main
if __name__ == "__main__":
    vetor = carregar_dados()

    inicio = time.time()
    insertion_sort(vetor)
    fim = time.time()

    print(f'### Tempo decorrido ###: {fim - inicio}')
