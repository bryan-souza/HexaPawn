import pygame
import random
from Display import whiteTable, blackTable, capture_pawn, move_pawn

# Sinapses do codigo genetico


def auto_play(): # Jogar automaticamente (brancas)
    took_turn = False # Variavel de controle
    while took_turn == False: # Loop principal
        pawn = random.choice(whiteTable) # Escolher um peao branco aleatorio
        cap = [] # Array de capturas possiveis
        last_x = pawn.x # Ultima posicao x
        last_y = pawn.y # Ultima posicao y
        
        for p in range(len(blackTable)): # Laço p/ identificar capturas possiveis
            if ((blackTable[p].y == (pawn.y - 218)) and ((blackTable[p].x == (pawn.x + 218)) or
                                                        (blackTable[p].x == (pawn.x - 218)))):
                cap.append(blackTable[p]) # Caso possivel, adicionar a cap
        
        if pawn.trn != 0: # Checar variavel de controle (ver Classe Pawn)
            sel = random.choice(cap) # Escolher uma das capturas possiveis
            if not (capture_pawn(pawn, sel) == False): # Caso seja possivel capturar...
                capture_pawn(pawn, sel) # MATA ELE
        else:
            move_pawn(pawn) # Mover peao

        if pawn.x == last_x and pawn.y == last_y: # Caso o peao nao tenha sido movido...
            took_turn = False # Reiniciar loop
        else: # Senao...
            pawn.trn += 1 # Alterar variavel de controle em Pawn
            took_turn = True # Parar laço principal

