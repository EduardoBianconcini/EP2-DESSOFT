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

#--------------------------------------------------------------