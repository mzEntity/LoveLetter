from config import Config
from game.game import Game
from common.singleton import singleton
import random
from common.logger import Logger
from game.effect import *


class Card:
    def __init__(self, point, name, isMad):
        self.point = point
        self.name = name
        self.isMad = isMad
        
    def __repr__(self):
        if self.isMad:
            return f"*[{self.point}]{self.name}*"
        else:
            return f"[{self.point}]{self.name}"
    
    def exec(self, player):
        print(f"player{player.id} 打出 {self}")
        

class Card00(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[0]["point"], 
                         Config().CARD_CONFIG[0]["name"], 
                         Config().CARD_CONFIG[0]["isMadCard"])
        self.effect = Lucid00()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)

       
class Card01(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[1]["point"], 
                         Config().CARD_CONFIG[1]["name"], 
                         Config().CARD_CONFIG[1]["isMadCard"])
        self.effect = Lucid01()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
        
        
        
class Card02(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[2]["point"], 
                         Config().CARD_CONFIG[2]["name"], 
                         Config().CARD_CONFIG[2]["isMadCard"])
        self.effect = Lucid02()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
        
        
        
class Card03(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[3]["point"], 
                         Config().CARD_CONFIG[3]["name"], 
                         Config().CARD_CONFIG[3]["isMadCard"])
        self.effect = Lucid03()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
            
            
        
class Card04(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[4]["point"], 
                         Config().CARD_CONFIG[4]["name"], 
                         Config().CARD_CONFIG[4]["isMadCard"])
        self.effect = Lucid04()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
        
        
class Card05(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[5]["point"], 
                         Config().CARD_CONFIG[5]["name"], 
                         Config().CARD_CONFIG[5]["isMadCard"])
        self.effect = Lucid05()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
        
        
class Card06(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[6]["point"], 
                         Config().CARD_CONFIG[6]["name"], 
                         Config().CARD_CONFIG[6]["isMadCard"])
        self.effect = Lucid06()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
        
        
class Card07(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[7]["point"], 
                         Config().CARD_CONFIG[7]["name"], 
                         Config().CARD_CONFIG[7]["isMadCard"])
        self.effect = Lucid07()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
        
        
class Card08(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[8]["point"], 
                         Config().CARD_CONFIG[8]["name"], 
                         Config().CARD_CONFIG[8]["isMadCard"])
        self.effect = Lucid08()
        
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)
        
        
class Card11(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[11]["point"], 
                         Config().CARD_CONFIG[11]["name"], 
                         Config().CARD_CONFIG[11]["isMadCard"])
        self.effect = [Lucid01(), Mad11()]
        
    def exec(self, player):
        super().exec(player)
        self.effect[choose()].exec(player)


def choose():
    return 1


@singleton
class CardBuilder:
    def __init__(self):
        self.cards = []
    
    def build(self):
        self.cards = []
        config = Config().CARD_CONFIG
        for idx, item in config.items():
            class_name_str = "Card" + "{:02d}".format(idx)
            if class_name_str in globals():
                for _ in range(item["count"]):
                    card = globals()[class_name_str]()
                    self.cards.append(card)
    
    

        