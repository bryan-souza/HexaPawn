import validators
import os
from validators import Validator
from objects import Pawn
from graphviz import Graph
from uuid import uuid1

class Node():
    # Constructor
    def __init__(self, node_id, children, weight=0):
        self.node_id = node_id  # Movecode for that node
        self.children = children  # Nodes generated by this node
        self.weight = weight  # Chance that this node will be chosen

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

        # Plotting
        self.dot = Graph(comment='HexaPawn', filename=os.path.join('plots','HexaPawn.gv'))
        self.dot.attr(center='true', rankdir='LR', ranksep='2.0 equally')

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

        # Split the default chance (weight) between all child nodes
        for node in children:
            node.weight = 100 / len(children)
        return Node(movecode[::-1][0], children)

    # Plot a graph containing all neurons
    def plot_nodes(self):
        # Create entry layer
        layers = {}
        links = []

        # Populate layers
        depth = 0
        parent_nodes = self.nodes
        while True:
            test = [ True if (node.children != []) else False for node in parent_nodes ]
            if (test.count(True) > 0):
                # Create layer nodes
                layer = self.__create_layer(parent_nodes)

                # Store layer
                layers.update({ str(depth): layer })

                # Repeat the process using this layer's children
                next_nodes = []
                link = []
                for node in parent_nodes:
                    for child in node.children:
                        next_nodes.append(child)
                        link.append([node.node_id, child.node_id])

                links.append(link)

                parent_nodes = next_nodes
                depth += 1
            else:
                break

        # Create the links
        for x in range(6):
            self.__linker(layers, links, x)

        # Finally, render the graph
        self.dot.render()

    def __create_layer(self, parent_nodes):
        layer = {}
        for node in parent_nodes:
            node_id = str( uuid1() )
            layer.update({node.node_id: node_id})

        return layer

    def __linker(self, layers, links, depth):
        # Fetch layers
        try:
            layer = layers[f'{depth}']
            sublayer = layers[f'{depth + 1}']
        except:
            return None

        link = links[depth]
        for lk in link:
            self.dot.node(name=layer[ lk[0] ], label=lk[0])
            tail = layer[ lk[0] ]

            self.dot.node(name=sublayer[ lk[1] ], label=lk[1])
            head = sublayer[ lk[1] ]

            self.dot.edge(tail, head)

ai = Ai()
ai.plot_nodes()
