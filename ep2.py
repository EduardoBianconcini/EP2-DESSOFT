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