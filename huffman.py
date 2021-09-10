# -*- coding: utf-8 -*-

#Função para carregar os arquivos de entrada
def carregar_dados():
    nome_arquivo = input("Insira o nome do arquivo: ")

    #Abre o arquivo e armazena os dados na variável entrada (necessário informar
    #a extensão do arquivo .txt ou .dvz)
    if nome_arquivo[-4:] == '.txt':
        with open(nome_arquivo, 'r') as arq:
            entrada = arq.read()

        arq.close()
        return nome_arquivo, entrada
    else:
        return nome_arquivo, ''

#Função para gerar uma lista de frequências
def gerar_tabela(texto):
    dicionario_freq = {}

    #Itera sobre cada caracter e incrementa o número de ocorrências na tabela
    for caracter in texto:
        if caracter in dicionario_freq:
            dicionario_freq[caracter] += 1
        else:
            dicionario_freq[caracter] = 1

    return sorted(dicionario_freq.items(), key=lambda x: x[1])

#Classe Nó de Huffman
class No:
    def __init__(self, simbolo, freq):
        self.simbolo = simbolo
        self.freq = freq
        self.esquerda = None
        self.direita = None
        self.bit = ''       #Define se recebe (0/1)

#Função para retornar um dicionário dos símbolos e seus códigos
def resultado(no, dicionario_cod, codificacao=''):
    codificacao = codificacao + str(no.bit)

    if no.esquerda:
        resultado(no.esquerda, dicionario_cod, codificacao)
    if no.direita:
        resultado(no.direita, dicionario_cod, codificacao)

    if no.esquerda is None and no.direita is None:
        dicionario_cod[no.simbolo] = codificacao

    return dicionario_cod

#Função para criar a árvore de Huffman
def huffman(lista_freq):
    queue = []

    #Cria a fila de nós,inicialmente baseada na lista de frequência
    for tupla in range(0, len(lista_freq)):
        no = No(lista_freq[tupla][0], lista_freq[tupla][1])
        queue.append(no)

    while len(queue) > 1:
        #Reorganiza a fila em ordem crescente com base na frequência
        queue = sorted(queue, key=lambda x: x.freq)

        #Pega os dois nós com menor frequência
        no_esquerda = queue[0]
        no_direita = queue[1]

        no_esquerda.bit = 0
        no_direita.bit = 1

        #Cria um nó maior que aponta para os demais
        novo_no = No(no_esquerda.simbolo + no_direita.simbolo,
                     no_esquerda.freq + no_direita.freq)
        novo_no.esquerda = no_esquerda
        novo_no.direita = no_direita

        #Remove os dois nós colocados na árvore
        #Insere o nó maior na fila
        queue.remove(no_esquerda)
        queue.remove(no_direita)
        queue.append(novo_no)

    #Retorna um dicionário com os símbolos e seus códigos correspondentes
    dicionario_codificacoes = {}
    return resultado(queue[0], dicionario_codificacoes)

#Função para comprimir o texto
def comprimir(dicionario_cod, texto):
    texto_comprimido = ''

    #Codifica cada símbolo de acordo com o seu valor no dicionário
    for simbolo in texto:
        texto_comprimido = texto_comprimido + dicionario_cod[simbolo]
        
    return texto_comprimido

#Função para transformar as informações em bytes
def transformar_bytes(texto_comprimido, lista):
    
    #Transformando o texto
    texto_bytes = bytearray()
    texto_normalizado = '0' * (8 - len(texto_comprimido) % 8) + texto_comprimido
    
    for i in range(0, len(texto_normalizado), 8):
        texto_bytes.append(int(texto_normalizado[i:i+8], 2))
    
    lista.append(8 - len(texto_comprimido) % 8)

    return texto_bytes, lista

#Função para transformar as informações em strings
def transformar_strings(texto_comprimido, lista):
    normalizacao = lista[-1]
    
    if isinstance(texto_comprimido, list):
        texto_comprimido = b''.join(texto_comprimido)
        
    texto_em_string = ''.join('{:08b}'.format(x) for x in texto_comprimido)
    
    texto_em_string = texto_em_string[normalizacao:]
    
    lista = lista[:-1]
    return lista, texto_em_string
    
#Função para descomprimir o texto
def descomprimir(tuplas_simbol_cod, texto):
    texto_descomprimido = ''

    i = 0
    j = 0
    while j <= len(texto):
        for tupla in tuplas_simbol_cod:
            j = len(str(tupla[1])) + i
            if texto[i:j] == tupla[1] and j <= len(texto):
                texto_descomprimido = texto_descomprimido + tupla[0]
                i = j
                break

    return texto_descomprimido

#Função para salvar o texto em um arquivo .dvz
def salvar_dados(nome_arquivo, lista, texto):
    with open(nome_arquivo[:-4] + '.dvz', 'wb') as arq:
        primeira_linha = (str(lista) + '\n')
        arq.write(primeira_linha.encode('utf-8'))
        arq.write(texto)
        
    arq.close()

#Função para carregar arquivos comprimidos
def carregar_dados_comprimidos(nome_arquivo):
    with open(nome_arquivo, 'rb') as arq:
        todas_linhas = arq.readlines()
        lista = eval(todas_linhas[0].decode('utf-8'))
        texto = todas_linhas[1:]
    arq.close()
    return lista, texto

if __name__ == '__main__':

    #Pega o texto do arquivo de entrada
    arquivo, texto_entrada = carregar_dados()

    if '.txt' in arquivo:

        #Gera a tabela de frequências
        frequencias = gerar_tabela(texto_entrada)

        #Recebe um dicionário de símbolos e seus códigos
        dicionario = huffman(frequencias)

        #Comprime o texto de entrada
        texto_comp = comprimir(dicionario, texto_entrada)
        print('\n-- Texto Comprimido: --\n\n' + texto_comp)

        #Ordena o dicionário em ordem 'decrescente', gerando tuplas
        lista_tuplas = sorted(dicionario.items(), key=lambda x: (len(x[1]), x[1]), reverse=True)
        
        #Transforma as informações em bytes
        texto_comp, lista_tuplas = transformar_bytes(texto_comp, lista_tuplas)
        
        #Salva a lista na primeira linha e o texto codificado
        salvar_dados(arquivo, lista_tuplas, texto_comp)

    if '.dvz' in arquivo:

        #Carrega os dados do arquivo comprimido e exibe o resultado da descompressão
        lista_tuplas, texto_comp = carregar_dados_comprimidos(arquivo)
        lista_tuplas, texto_comp = transformar_strings(texto_comp, lista_tuplas)
        
        print('\n-- Texto Descomprimido: --\n\n' + descomprimir(lista_tuplas, texto_comp))
