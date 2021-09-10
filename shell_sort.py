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

#Função de ordenação de Shell
def shell_sort(vetor_elementos):
    num_elementos = len(vetor_elementos)
    h = int(num_elementos/2)

    while h > 0:
        for i in range(h, num_elementos):
            valor = vetor_elementos[i]
            j = i
            while j >= h and vetor_elementos[j-h] > valor:
                vetor_elementos[j] = vetor_elementos[j-h]
                j-=h

            vetor_elementos[j] = valor
        h = int(h/2)

#Main
if __name__ == "__main__":
    vetor = carregar_dados()

    inicio = time.time()
    shell_sort(vetor)
    fim = time.time()

    print(f'### Tempo decorrido ###: {fim - inicio}')
