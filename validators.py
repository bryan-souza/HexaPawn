import pygame

class Validator:
    """
    Put some proper documentation on me, you punk
    """

    # Constructor
    def __init__(self, group):
        self.group = group
        self.ids = {}
        
        # Create a dictionary containing all pawn ids
        # and its respective position in the group
        for p in range(6):
            self.ids.update({p: group[p].id})

    # Move validator
    def move_tester(self, pawn_id):
        """
        Tests if the pawn can properly move foward
        """

        # Tries to fetch the required pawn object;
        # raises an error if the object is not found
        try:
            pawn = self.ids[pawn_id]
        except KeyError:
            print("[ERROR] Pawn id not found!")

        # Create a new pawn group that doesn't contain
        # the target pawn
        test_group = []
        for p in self.group:
            if (p.id == pawn_id):
                pass
            else:
                test_group.append(p)

        # Color-based testing
        if (pawn.color == "white"):
            # Upwards testing
            test_list = [ True if ( (test.x == pawn.x) and (test.y == ( pawn.y -= 214 )) ) else False for test in test_group ]
        else:
            # Downwards testing
            test_list = [ True if ( (test.x == pawn.x) and (test.y == ( pawn.y += 214 )) ) else False for test in test_group ]
        
        # Check if the pawn will collide with another pawn if it moves
        if (test_list.count(True) > 0):
            # It will collide, return False (invalid move)
            return False
        else:
            # It won't collide, return True (valid move)
            return True