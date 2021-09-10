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

#Função de ordenação por intercalação
def merge_sort(vetor_elementos):
    if len(vetor_elementos) > 1:
        meio = len(vetor_elementos)//2
        esquerda = vetor_elementos[:meio]
        direita = vetor_elementos[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        vetor_elementos = sorted(esquerda + direita)

#Main
if __name__ == "__main__":
    vetor = carregar_dados()

    inicio = time.time()
    merge_sort(vetor)
    fim = time.time()

    print(f'### Tempo decorrido ###: {fim - inicio}')
