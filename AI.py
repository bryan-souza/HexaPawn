import pygame
import random
from Display import whiteTable, blackTable, capture_pawn, move_pawn, move_test

moves = []
wht_mv = True
blk_mv = True

def auto_play(): # Jogar automaticamente (brancas)
    took_turn = False # Variavel de controle
    cap = []
    sel = None

    while took_turn == False: # Loop principal
        pawn = random.choice(whiteTable) # Escolher um peao branco aleatorio
        
        for p in range(len(blackTable)): # Laço p/ identificar capturas possiveis
            if (blackTable[p].y == (pawn.y - 218) and (blackTable[p].x == (pawn.x + 218)) or (blackTable[p].x == (pawn.x - 218))):
                cap.append((blackTable[p])) # Caso possivel, adicionar a cap

        try:
            sel = random.choice(cap)

        except IndexError:
            if move_test(pawn) == True:
                move_pawn(pawn)
                took_turn = True
            else:
                wht_mv = False
                took_turn = True
                return wht_mv
        
        finally:
            capture_pawn(pawn, sel) # MATA ELE
            took_turn = True

        
def gen_arrays(): # Gerar sinapses da IA (até pq dá muito trabalho fazer manualmente...)
    moves.clear()
    for p in range(len(blackTable)):
        for e in range(len(whiteTable)):
            if whiteTable[e].y == (blackTable[p].y + 218): 
                if (whiteTable[e].x == (blackTable[p].x + 218) or whiteTable[e].x == (blackTable[p].x - 218)):
                    # Testar se existem peoes capturaveis
                    moves.append(str(blackTable[p].trn) + "C" + blackTable[p].id + whiteTable[e].id)
                    # Adicionar á lista de movimentos possiveis do peao

    for p in range(len(blackTable)):
        if (move_test(blackTable[p]) != False):
            moves.append(str(blackTable[p].trn) + "M" + blackTable[p].id)
    
    print(moves)
    return moves
        
def make_a_move():
    gen_arrays()
    move = None
    # Make-a-move (credits: Luska E
    try:
        move = random.choice(moves)

    except IndexError:
        blk_mv = False
        return blk_mv

    else:
        # "Desencriptar" o movimento -> N° do Turno + Tipo de movimento + ID do Peao
        # turn = move[0] # Detectar o turno em que deve ser adicionado
        tipo = move[1] # Detectar o tipo da acao (M/C)
        if tipo == "M":
            target = (move[2] + move[3] + move[4]) # Detectar o alvo da acao
        elif tipo == "C":
            pawn = (move[2] + move[3] + move[4])
            target = (move[5] + move[6] + move[7])

        if tipo == "M": # Movimentar
            for p in range(len(blackTable)):
                if blackTable[p].id == target:
                    move_pawn(blackTable[p])
                    blackTable[p].trn += 1

        elif tipo == "C": # Capturar
            for p in range(len(blackTable)):
                if blackTable[p].id == pawn:
                        pwn = blackTable[p]
            for e in range(len(whiteTable)):
                if whiteTable[e].id == target:
                    tgt = whiteTable[e]
            capture_pawn(pwn, tgt)