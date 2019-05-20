import pygame
from Sprites import Pawn

logo = pygame.image.load("logo32x32.png") # Associar a imagem a variavel logo
pygame.display.set_icon(logo) # Carregar a imagem
pygame.display.set_caption("HexaPawn") # Mudar o titulo do programa

screen = pygame.display.set_mode((660, 660)) # Criar tela de 660x660
background = pygame.Surface(screen.get_size()) # Criar um plano e nomear como BKG
background.fill((255, 0, 255)) # Preencher o fundo com uma cor aleatoria
background = background.convert() # Converter o objeto para otimizar o jogo

# TABULEIRO
A1 = None
A2 = None
A3 = None
B1 = None
B2 = None
B3 = None
C1 = None
C2 = None
C3 = None

# Array usado para preencher o tabuleiro
tab_array = [A1, A2, A3,
                B1, B2, B3,
                C1, C2, C3]

# Array com as posicoes das casas do tabuleiro
tab_pos = [(5, 441)	 , (5, 223)	 , (5, 5),
            (223, 441), (223, 223), (223, 5),
            (441, 441), (441, 223), (441, 5)]

WA1 = Pawn("whitePawn", 5, 441) # Peao Branco em A1
WA2 = Pawn("whitePawn", 223, 441) # Peao Branco em A2
WA3 = Pawn("whitePawn", 441, 441) # Peao Branco em A3
BC1 = Pawn("blackPawn", 5, 5) # Peao Preto em C1
BC2 = Pawn("blackPawn", 223, 5) # Peao Preto em C2
BC3 = Pawn("blackPawn", 441, 5) # Peao Preto em C3

def board_init():
    pygame.init() # Inicializar o pygame

    # Criar os "objetos" representando o tabuleiro
    for x in range(len(tab_array)):
        tab_array[x] = pygame.Surface((213, 213)) # Criar uma superficie de tamanho 213x213
        if (x % 2 == 0): # Mudar a cor conforme o número da casa
            tab_array[x].fill((0,0,0)) # Casa preta
        else:
            tab_array[x].fill((255,255,255)) # Casa branca

        tab_array[x] = tab_array[x].convert() # Converter em objeto
        background.blit(tab_array[x], (tab_pos[x])) # Mostrar na tela

    background.blit(WA1.image, (WA1.x, WA1.y)) # Mostrar peao A1 na tela
    background.blit(WA2.image, (WA2.x, WA2.y)) # Mostrar peao A2 na tela
    background.blit(WA3.image, (WA3.x, WA3.y)) # Mostrar peao A3 na tela
    background.blit(BC1.image, (BC1.x, BC1.y)) # Mostrar peao B1 na tela
    background.blit(BC2.image, (BC2.x, BC2.y)) # Mostrar peao B2 na tela
    background.blit(BC3.image, (BC3.x, BC3.y)) # Mostrar peao B3 na tela

    screen.blit(background, (0,0)) # Imprimir na tela

def board_update(): # Funcao p/ atualizar a tela (tabuleiro)
    for x in range(len(tab_array)):
        tab_array[x] = pygame.Surface((213, 213))
        if (x % 2 == 0):
            tab_array[x].fill((0,0,0))
        else:
            tab_array[x].fill((255,255,255))

        tab_array[x] = tab_array[x].convert()
        background.blit(tab_array[x], (tab_pos[x]))

    background.blit(WA1.image, (WA1.x, WA1.y)) # Mostrar peao A1 na tela
    background.blit(WA2.image, (WA2.x, WA2.y)) # Mostrar peao A2 na tela
    background.blit(WA3.image, (WA3.x, WA3.y)) # Mostrar peao A3 na tela
    background.blit(BC1.image, (BC1.x, BC1.y)) # Mostrar peao B1 na tela
    background.blit(BC2.image, (BC2.x, BC2.y)) # Mostrar peao B2 na tela
    background.blit(BC3.image, (BC3.x, BC3.y)) # Mostrar peao B3 na tela

    screen.blit(background, (0, 0))