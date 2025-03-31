from config import Config
from game.game import Game
from common.singleton import singleton
import random
from common.logger import Logger
from game.effect import *


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

class Card:
    def __init__(self, index, point, name, isMad):
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
        

class LucidCard(Card):
    def __init__(self, index, point, name, effect):
        super().__init__(index, point, name, False)
        self.effect = effect
    
    def exec(self, player):
        super().exec(player)
        self.effect.exec(player)


class MadCard(Card):
    def __init__(self, index, point, name, lucidEffect, madEffect):
        super().__init__(index, point, name, True)
        self.lucidEffect = lucidEffect
        self.madEffect = madEffect

    def useMadEffect(self, player)->int:
        return 1
    
    def exec(self, player):
        super().exec(player)
        if self.useMadEffect(player):
            self.madEffect.exec(player)
        else:
            self.lucidEffect.exec(player)


class Card00(LucidCard):
    def __init__(self):
        super().__init__(0, Config().CARD_CONFIG[0]["point"], 
                         Config().CARD_CONFIG[0]["name"], Lucid00())

       
class Card01(LucidCard):
    def __init__(self):
        super().__init__(1, Config().CARD_CONFIG[1]["point"], 
                         Config().CARD_CONFIG[1]["name"], Lucid01())
        
        
    
class Card02(LucidCard):
    def __init__(self):
        super().__init__(2, Config().CARD_CONFIG[2]["point"], 
                         Config().CARD_CONFIG[2]["name"], Lucid02())
        
        
        
class Card03(LucidCard):
    def __init__(self):
        super().__init__(3, Config().CARD_CONFIG[3]["point"], 
                         Config().CARD_CONFIG[3]["name"], Lucid03())

            
            
        
class Card04(LucidCard):
    def __init__(self):
        super().__init__(4, Config().CARD_CONFIG[4]["point"], 
                         Config().CARD_CONFIG[4]["name"], Lucid04())

        
        
class Card05(LucidCard):
    def __init__(self):
        super().__init__(5, Config().CARD_CONFIG[5]["point"], 
                         Config().CARD_CONFIG[5]["name"], Lucid05())

        
        
class Card06(LucidCard):
    def __init__(self):
        super().__init__(6, Config().CARD_CONFIG[6]["point"], 
                         Config().CARD_CONFIG[6]["name"], Lucid06())

        
        
class Card07(LucidCard):
    def __init__(self):
        super().__init__(7, Config().CARD_CONFIG[7]["point"], 
                         Config().CARD_CONFIG[7]["name"], Lucid07())

        
        
class Card08(LucidCard):
    def __init__(self):
        super().__init__(8, Config().CARD_CONFIG[8]["point"], 
                         Config().CARD_CONFIG[8]["name"], Lucid08())

# 拉莱耶
class Card10(MadCard):
    def __init__(self):
        super().__init__(9, Config().CARD_CONFIG[10]["point"], 
                         Config().CARD_CONFIG[10]["name"], Lucid00(), Mad10())
        
    


# 异教徒
class Card11(MadCard):
    def __init__(self):
        super().__init__(11, Config().CARD_CONFIG[11]["point"], 
                         Config().CARD_CONFIG[11]["name"], Lucid01(), Mad11())


# 夜魇
class Card12(MadCard):
    def __init__(self):
        super().__init__(12, Config().CARD_CONFIG[12]["point"], 
                         Config().CARD_CONFIG[12]["name"], Lucid02(), Mad12())
        


class Card13(MadCard):
    def __init__(self):
        super().__init__(13, Config().CARD_CONFIG[13]["point"], 
                         Config().CARD_CONFIG[13]["name"], Lucid03(), Mad13())
        


# 《死灵之书》
class Card14(MadCard):
    def __init__(self):
        super().__init__(14, Config().CARD_CONFIG[14]["point"], 
                         Config().CARD_CONFIG[14]["name"], Lucid04(), Mad14())
        


# 偷渡虫
class Card15(MadCard):
    def __init__(self):
        super().__init__(15, Config().CARD_CONFIG[15]["point"], 
                         Config().CARD_CONFIG[15]["name"], Lucid05(), Mad15())
        

class Card16(MadCard):
    def __init__(self):
        super().__init__(16, Config().CARD_CONFIG[16]["point"], 
                         Config().CARD_CONFIG[16]["name"], Lucid06(), Mad16())
        

class Card17(MadCard):
    def __init__(self):
        super().__init__(17, Config().CARD_CONFIG[17]["point"], 
                         Config().CARD_CONFIG[17]["name"], Lucid07(), Mad17())
        

class Card18(MadCard):
    def __init__(self):
        super().__init__(18, Config().CARD_CONFIG[18]["point"], 
                         Config().CARD_CONFIG[18]["name"], Lucid08(), Mad18())


if __name__ == "__main__":
    cb = CardBuilder()
    cb.build()
    cards = cb.cards
    for c in cards:
        print(c)