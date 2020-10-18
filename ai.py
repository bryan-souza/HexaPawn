import validators
from validators import Validator
from objects import Pawn

class Node():
    # Constructor
    def __init__(self, node_id, children):
        self.node_id = node_id  # Movecode for that node
        self.children = children  # Nodes generated by this node
        self.weight = 0  # Choosing criteria for this node, more is better

class Ai():
    # Constructor
    def __init__(self):
        self.pawns = [
            Pawn("black", "a3", silent=True),
            Pawn("black", "b3", silent=True),
            Pawn("black", "c3", silent=True),
            Pawn("white", "a1", silent=True),
            Pawn("white", "b1", silent=True),
            Pawn("white", "c1", silent=True)
        ]
        self.judge = Validator(self.pawns)
        self.nodes = []
        
        entry_moves = ['a2', 'b2', 'c2']
        # Test all entry moves and create all possible nodes
        for move in entry_moves:
            self.nodes.append( self.__make_nodes([move]) )

    # Generates nodes based on the current board state
    def __make_nodes(self, movecode):
        # Reset the judge, so it can make 
        # all moves from the beginning
        self.judge.reset(True)

        # Execute the moves
        for code in movecode:
            self.judge.check(code, silent=True)

        # Results for this state
        children = []

        # Check if the moves resulted in victory
        self.judge.victory_validator(True)
        if (self.judge.white_wins == 1):
            self.judge.white_wins = 0
            return Node(movecode[::-1][0], children=[])
        elif (self.judge.black_wins == 1):
            self.judge.black_wins = 0
            return Node(movecode[::-1][0], children=[])

        # Column capture resolver
        col_dict = {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"]
        }
        
        # Sort pawns by color
        blacks = []
        whites = []
        for pawn in self.judge.group:
            if (pawn.color == 'black'):
                blacks.append(pawn)
            else:
                whites.append(pawn)

        # Check for all possible movements
        for pawn in ( whites if (len(movecode) % 2 == 0) else blacks ):
            # Check for movements
            if ( self.judge.move_check(pawn.id)[0] == True):
                children.append(f'{pawn.id[0]}{int(pawn.id[1]) + (-1 if (pawn.color == "black") else 1)}')
            
            # Check for captures
            for col in col_dict[ pawn.id[0] ]:
                if ( self.judge.capture_check(pawn.id, f'{col}{int(pawn.id[1]) + (-1 if (pawn.color == "black") else 1)}')[0] == True):
                    children.append(f'{pawn.id[0]}x{col}{int(pawn.id[1]) + (-1 if (pawn.color == "black") else 1)}')

        for node in children:
            idx = children.index(node)
            test = movecode.copy()
            test.append(node)
            children[idx] = self.__make_nodes(test)

        return Node(movecode[::-1][0], children)