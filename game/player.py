from game.deck import Deck
from common.logger import Logger

class Player:
    def __init__(self, id):
        self.id = id
        self.hand_deck = Deck()
        self.discard_deck = Deck()
        
        self.escape = False
        self.dead = False
        self.skipSanCheck = False
        self.protectedByNecro = False
        self.isMad = False
        
    def __repr__(self):
        if self.dead:
            return f"player{self.id}(已出局)"
        elif self.escape:
            return f"player{self.id}(无法选中)"
        else:
            return f"player{self.id}"
        
    def get_hand_card(self):
        if len(self.hand_deck) != 1:
            Logger().warning("调用get_hand_card时手牌数不为1，这可能导致一些问题")
        return self.hand_deck[0]
    
    def die(self):
        if self.protectedByNecro: return
        self.dead = True