#Primeiramente, declara-se as funções que serão utilizadas no código

#implementa-se a função que cria o mapa vazio, n x n
def cria_mapa(n):
    mapa = [[' ' for a in range(n)] for a in range(n)]
    return mapa
#----------------------------------------------

#implementa-se a função que verifica se, a posição escolhida para a peça, é suportada, com base no mapa, e em peças posicionadas anteriormente
def posicao_suporta(mapa, blocos, l, c, ori):
    if blocos == 1:
        if mapa[l][c] == "N":
            return False
        else:
            return True
    
    elif blocos > 1:
        if ori in ["V", "v"]:
            for i in range(blocos):
                if (l + i ) >= len(mapa) or mapa[(l + i)][c] == "N":
                    return False 
            return True
                
        elif ori in ["h", "H"]:
            for j in range(blocos):
                if (c + j ) >= len(mapa[l]) or mapa[l][(c + j)] == "N":
                    return False
            
            return True

#---------------------------------------------------
import random

#implementa-se uma função que aloca navios, aleatoriamente, para o computador(um dos jogadores)
def aloca_navios(mapa, blocos_cada_navio):
    for tamanho_navio in blocos_cada_navio:
        alocado = False

        while not alocado:
            l = random.randint(0, len(mapa)-1)
            c = random.randint(0, len(mapa[0])-1)
            ori = random.choice(['h', 'v'])
            pode = posicao_suporta(mapa, tamanho_navio, l, c, ori)

            if pode:
                if ori == "v":
                    for i in range(tamanho_navio):
                        mapa[l+i][c] = "N"

                    alocado = True

                elif ori == "h":
                    for j in range(tamanho_navio):
                        mapa[l][c+j] = "N"
                    alocado = True

    return mapa

#--------------------------------------------------------------

#implementa-se uma função que verifica se, algum dos jogadores, foi derrotado, ou seja, se teve todos os seus navios afundados, atingidos
#A função "foi derrotado" foi modificada para o melhor funcionamento desse código em específico. Agora, ela recebe dois argumentos, ou seja, cada um dos mapas
#E verifica quem ganhou, ou melhor, qual perdeu
def foi_derrotado(mapa_jogador, mapa_computador):
    cont_jogador = 0
    for l_j in mapa_jogador:
        if 'N' not in l_j:
            cont_jogador += 1
    if cont_jogador == len(mapa_jogador):
        return "Acabou para jogador"
    
    cont_computador = 0
    for l_c in mapa_computador:
        if 'N' not in l_c:
            cont_computador += 1
    if cont_computador == len(mapa_computador):
        return "Acabou para computador"

#Caso necessite do uso dessa função em específico, o código estará comentado. Ele funcionará da mesma forma.
# def foi_derrotado(mapa):
#     cont = 0
#     for l in mapa:
#         if 'N' not in l:
#             cont += 1
#     if cont == len(mapa):
#         return True
#     else:
#         return False


#--------------------------------------------------------------

#implementa-se uma função que printa o mapa. Esta leva em consideração se algum navio foi posicionado, se algum navio foi atingido, ou se o tiro caiu na água
#para o jogador, não pode-se ter visão dos navios do computador, logo, há no total, 3 mapas.
#Um mapa é o do jogador, outro é o do computador, e o 3° é um mapa do computador que é visivel para o jogador
#Este por sua vez printa se o tiro do jogador atingiu algum navio, ou se caiu na água
def print_mapa(mapa_computador, mapa_jogador):
    print(f" COMPUTADOR - {mapa_computador}                                        JOGADOR - {mapa_jogador}                  ")
    print("    A    B    C    D    E    F    G    H    I    J              A    B    C    D    E    F    G    H    I    J   ")

    for i in range(10):

        linha_c = '  '.join('\033[41m X \033[0m' if celula == 'X' else '\033[44m   \033[0m' if celula == 'A' else '   ' for celula in mapa_computador[i])

        linha_j = '  '.join('\033[41m X \033[0m' if celula == 'X' else ('\033[42m N \033[0m' if celula == 'N' else '\033[44m   \033[0m' if celula == 'A' else '   ') for celula in mapa_jogador[i])

        n_linha = f"{i + 1:2}"  

        print(f"{n_linha} {linha_c} {n_linha}      {n_linha} {linha_j} {n_linha}")

    print("    A    B    C    D    E    F    G    H    I    J              A    B    C    D    E    F    G    H    I    J   ")
    return ''

#--------------------------------------------------------------

#implementa-se uma função que modifica o mapa para indicar se o tiro dado acertou algum navio, ou caiu na água
def tiro(mapa, linha, coluna):
    if mapa[linha][coluna] == 'N':
        mapa[linha][coluna] = 'X'
        return "BOOOOOOOMMMMMM!!!!!"
    elif mapa[linha][coluna] == ' ':
        mapa[linha][coluna] = 'A'
        return "Água"

#--------------------------------------------------------------

#implementa-se uma função que substitui no mapa do computador, visivel para o jogador, se o tiro, dado pelo jogador, acertou algum navio do computador, ou caiiu na água
def substitui_para_mapa(mapa_computador, linha, coluna, tiro):
    if tiro == "BOOOOOOOMMMMMM!!!!!":
        mapa_computador[linha][coluna] = 'X'
    elif tiro == "Água":
        mapa_computador[linha][coluna] = 'A'

#---------------------------------------------------------------


# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}


# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

#----------------------------------------------------------------


#Cria-se uma variável para o país que o computador irá representar
computador = random.choice(["Brasil", "França", "Austrália", "Rússia", "Japão"])

#Inicia-se o jogo
print(
"Iniciando o Jogo!"
f'\nComputador está alocando os navios de guerra do país {computador}...'
"\nComputador já está em posição de batalha!")

print(
"1: Brasil"
"\n   1 cruzador"
"\n   2 torpedeiro"
"\n   1 destroyer"
"\n   1 couracado"
"\n   1 porta-avioes")

print("2: França"
"\n   3 cruzador"
"\n   1 torpedeiro"
"\n   1 destroyer"
"\n   1 couracado"
"\n   1 porta-avioes")

print("3: Austrália"
"\n   1 cruzador"
"\n   3 torpedeiro"
"\n   1 destroyer"
"\n   1 couracado"
"\n   1 porta-avioes")

print("4: Rússia"
"\n   1 cruzador"
"\n   1 torpedeiro"
"\n   2 destroyer"
"\n   1 couracado"
"\n   1 porta-avioes")

print("5: Japão"
"\n   2 cruzador"
"\n   1 torpedeiro"
"\n   2 destroyer"
"\n   1 couracado"
"\n   1 porta-avioes")

#Cria-se uma variável e pede ao jogador para escolher alguma nação para representar no jogo
#Repete a escolha até um número válido ser escolhido
jogador = int(input("Qual o número da nação da sua frota?"))
if jogador not in [1, 2, 3, 4, 5]:
    y = False
    while not y:
        print("Número Inválido! Tente novamente")
        jogador = int(input("Qual o número da nação da sua frota?"))
        if jogador in [1, 2, 3, 4, 5]:
            y = True

#Cria-se uma variável com a lista dos países que podem ser escolhidos e cria-se uma variável para armazenar a nação escolhida pelo jogador
pais = ["Brasil", "França", "Austrália", "Rússia", "Japão"]
escolhido = pais[(jogador-1)]

#printa-se qual nação foi escolhida pelo jogador e continua-se o jogo
print(
f'Você escolheu a nação {escolhido}'
"\nAgora é a sua vez de alocar seus navios de guerra!"
)

#Cria-se os mapas utilizados no jogo, o do computador, o do computador visível para o jogador, e o do jogador
mapa_c = cria_mapa(10)
mapa_c_real = cria_mapa(10)
mapa_j = cria_mapa(10)

#Printa-se o tabuleiro
print(
f"  COMPUTADOR - {computador}                   JOGADOR - {escolhido}                  "
"\n   A  B  C  D  E  F  G  H  I  J            A  B  C  D  E  F  G  H  I  J   ")

for b in range(10):
    linha_c = '  '.join(mapa_c[b])
    linha_j = '  '.join(mapa_j[b])

    n_linha = f"{b+1:2}" 
    print(f"{n_linha} {linha_c} {n_linha}      {n_linha} {linha_j} {n_linha}")

print ("   A  B  C  D  E  F  G  H  I  J            A  B  C  D  E  F  G  H  I  J   ")

#Cria-se as listas que serão usadas para demonstração das peças que devem ser alocadas pelo jogador
lista_tropas_pais_j = []
lista_nbloco_tropa_pais_j = []

lista_tropas_pais_c = []
lista_nbloco_tropa_pais_c = []

#Cria-se dois loops para preencher as listas corretamente para uso
#Aqui aloca-se as tropas na lista, levando em consideração a sua quantidade 
#Aloca-se, com mesmo índice, o número de blocos que cada tropa ocupa, para a sua devida alocação
for tropa, qnt in PAISES[escolhido].items():
    if qnt == 1:
        lista_tropas_pais_j.append(tropa)
        lista_nbloco_tropa_pais_j.append(CONFIGURACAO[tropa])
    
    elif qnt == 2:
        for i in range(2):
            lista_tropas_pais_j.append(tropa)
            lista_nbloco_tropa_pais_j.append(CONFIGURACAO[tropa])

    elif qnt == 3:
        for i in range(3):
            lista_tropas_pais_j.append(tropa)
            lista_nbloco_tropa_pais_j.append(CONFIGURACAO[tropa])

for tropa, qnt in PAISES[computador].items():
    if qnt == 1:
        lista_tropas_pais_c.append(tropa)
        lista_nbloco_tropa_pais_c.append(CONFIGURACAO[tropa])
    
    elif qnt == 2:
        for i in range(2):
            lista_tropas_pais_c.append(tropa)
            lista_nbloco_tropa_pais_c.append(CONFIGURACAO[tropa])

    elif qnt == 3:
        for i in range(3):
            lista_tropas_pais_c.append(tropa)
            lista_nbloco_tropa_pais_c.append(CONFIGURACAO[tropa])


#Cria-se um loop para a alocação das peças no tabuleiro do jogador
#Printa-se a peça a ser alocada, e o número de blocos que esta ocupa
#Printa-se as próximas peças a serem alocadas pelo jogador
#Pergunta-se qual a posição, no mapa, para alocar-se a peça
#Verifica-se se a posição escolhida é suportada no mapa
#Posiciona-se a peça
#Printa-se o mapa com a peça alocada
for i in range(len(lista_tropas_pais_j)):   

    print(f'Alocar: {lista_tropas_pais_j[0]} ({lista_nbloco_tropa_pais_j[0]} blocos)')

    print(f'Proximos: {", ".join(lista_tropas_pais_j)}')

    pode = False

    while not pode:

        coluna = input("Informe a Letra:")
        if coluna not in ALFABETO and coluna not in ALFABETO.lower():
            print('Coluna Inválida! Tente Novamente')
            continue


        coluna_i = ALFABETO.index(coluna.upper())  

        linha = int(input("Informe a Linha:")) - 1
        if linha not in [0, 1, 2, 3, 4,5, 6, 7, 8, 9,]:
            print('Linha Inválida! Tente Novamente')
            continue


        orientacao = input("Informe a Orientação [v|h]:")
        if orientacao not in ['v', 'V', 'h', 'H']:
            print('Orientação Inválida! Tente Novamente')
            continue

        pode = posicao_suporta(mapa_j, lista_nbloco_tropa_pais_j[0], linha, coluna_i, orientacao)



    if orientacao == "v":
        for i in range(lista_nbloco_tropa_pais_j[0]):
            mapa_j[linha+i][coluna_i] = 'N'

    elif orientacao == "h":
        for j in range(lista_nbloco_tropa_pais_j[0]):
            mapa_j[linha][coluna_i+j] = 'N'

    #Cria-se essa lista para entregar à função uma lista com o número de blocos que a peça ocupa
    lista_nbloco_tropa_pais_c_trans_lista = []
    lista_nbloco_tropa_pais_c_trans_lista.append(lista_nbloco_tropa_pais_c[i])


    print(print_mapa(mapa_c, mapa_j))

    aloca_navios(mapa_c_real, lista_nbloco_tropa_pais_c_trans_lista)

    #Retira-se, da lista de tropas e blocos, a peça que fora alocada
    lista_tropas_pais_j.pop(0)
    lista_nbloco_tropa_pais_j.pop(0)

    #Da-se início ao jogo
import time
print("Iniciando a batalha naval!")

time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

#Cria-se uma variável que indica se o jogo acabou ou não, ou seja, se há, ainda, navios em algum dos mapas
acabou = False

#Cria-se um loop para seguir com o jogo até que todos os navios, de algum dos jogadores, jogador e computador, sejam afundados
while not acabou:
    #Printa-se os mapas, do computador visível para o jogador, e do jogador
    print(print_mapa(mapa_c, mapa_j))

    #pergunta-se quais as coordenadas do tiro do jogador
    foi = False
    print('Coordenadas do disparo:')

    while not foi:

        coluna = input("Informe a Letra:")
        if coluna not in ALFABETO and coluna not in ALFABETO.lower():
            print('Coluna Inválida! Tente Novamente')
            continue


        coluna_i = ALFABETO.index(coluna.upper())  

        linha = int(input("Informe a Linha:")) - 1
        if linha not in [0, 1, 2, 3, 4,5, 6, 7, 8, 9,]:
            print('Linha Inválida! Tente Novamente')
            continue

        foi = True

    #Escolhe-se, aleatoriamente, as coordenadas do tiro do computador
    coluna_comp = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    coluna_comp_i = ALFABETO.index(coluna_comp.upper()) 
    linha_comp = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    #Verifica-se se as coordenadas escolhidas aleatoriamente já foram escolhidas anteriormente
    #Gera-se novas coordenadas
    if mapa_j[coluna_comp_i][linha_comp] == 'X' or mapa_j[coluna_comp_i][linha_comp] == 'A':
        coluna_comp = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        coluna_comp_i = ALFABETO.index(coluna_comp.upper()) 
        linha_comp = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


    #Modifica-se os mapas, se o tiro acertou ou não
    tiro_jogador = tiro(mapa_c_real, linha, coluna_i)

    tiro_comp = tiro(mapa_j, linha_comp, coluna_comp_i)

    #Substitui-se no mapa visível para o jogador, se o tiro acertou ou não algum navio
    substitui_para_mapa(mapa_c, linha, coluna_i, tiro_jogador)

    #Printa-se as coordenadas dos tiros do jogador e do computador
    print(f'Jogador   ----->>>>> {coluna}{linha+1}       {tiro_jogador}!'
          "\n ''")
    print(f'Computador   ----->>>>> {coluna_comp}{linha_comp+1}       {tiro_comp}!')   

    #Verifica-se se algum dos jogadores teve todos os navios afundados e quebra-se o loop
    if foi_derrotado(mapa_j, mapa_c_real) == "Acabou para computador":
        acabou = True  

    elif foi_derrotado(mapa_j, mapa_c_real) == "Acabou para jogador":
        acabou = True

    #Código para o uso da função "foi_derrotado" como pedido
    #x = 0
    #if foi_derrotado(mapa_j):
    #    x = 1
    #    acabou = True
    
    #elif foi_derrotado(mapa_j):
    #    acabou = True

#Anuncia se o jogador perdeu ou ganhou o jogo!
if foi_derrotado(mapa_j, mapa_c_real) == "Acabou para computador":
    print ("Parabéns! você ganhou!")

elif foi_derrotado(mapa_j, mapa_c_real) == "Acabou para jogador":
    print("Você perdeu!")

#Anuncia se o jogador perdeu ou ganhou
# if x == 1:
#     print("Você perdeu!")

# else:
#     print(" Parabéns, você ganhou!")

