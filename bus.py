"""
[EN]
Module that stores and shares globals across modules

[PT-BR]
Módulo para armazenar e compartilhar variáveis globais entre modulos
"""

from objects import Pawn
from validators import Validator
from ai import Ai

def init():
    """
    Initialize globals
    """
    # Create a group to store all pawns in the game
    global pawns
    global judge
    global ai

    pawns = [
        Pawn("black", "a3"),
        Pawn("black", "b3"),
        Pawn("black", "c3"),
        Pawn("white", "a1"),
        Pawn("white", "b1"),
        Pawn("white", "c1")
    ]
    judge = Validator(pawns)
    ai = Ai()