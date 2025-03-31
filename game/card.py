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
    
    
# 
class MadCard(Card):
    def __init__(self, index):
        cfg = Config().CARD_CONFIG[index]
        Card.__init__(cfg["point"], cfg["name"], cfg["description"], cfg["isMad"])
        self.madDescription = cfg["madDescription"]

    def useMadEffect(self, player)->int:
        return 1


# 拉莱耶
class Card10(MadCard, Card00):
    def __init__(self):
        MadCard.__init__(10)
        
    def exec(self, player):
        if self.useMadEffect(player):
            
            
            pass
        else:
            Card00.exec(self, player)


# 异教徒
class Card11(MadCard, Card01):
    def __init__(self):
        MadCard.__init__(11)
        
    def exec(self, player):
        if not self.useMadEffect(player):
            Card01.exec(player)
        else:
            Card.exec(player)
            target = Game().choose_player(player)

            card = target.get_hand_card()
            
            if card.point == 1:
                Logger().info(f"猜中了牌的点数({guess}): {card}")
                target.die()
            else:
                # TODO: need to guess here
                guess = random.randint(0, 8)
                if card.point == guess:
                    Logger().info(f"猜中了牌的点数({guess}): {card}")
                    target.die()
                else:
                    Logger().info(f"猜了牌的点数({guess})，猜错了")


# 夜魇
class Card12(MadCard, Card02):
    def __init__(self):
        MadCard.__init__(12)
        
    def exec(self, player):
        if not self.useMadEffect(player):
            Card02.exec(player)
        else:
            Card.exec(player)




class Card13(MadCard, Card03):
    def __init__(self):
        MadCard.__init__(13)
        
    def exec(self, player):
        if self.useMadEffect(player):
            pass
        else:
            Card03.exec(self, player)


# 《死灵之书》
class Card14(MadCard, Card04):
    def __init__(self):
        MadCard.__init__(14)
        
    def exec(self, player):
        if self.useMadEffect(player):
            pass
        else:
            Card04.exec(self, player)


# 偷渡虫
class Card15(MadCard, Card05):
    def __init__(self):
        MadCard.__init__(15)
        
    def exec(self, player):
        if self.useMadEffect(player):
            pass
        else:
            Card05.exec(self, player)

class Card16(MadCard, Card06):
    def __init__(self):
        MadCard.__init__(16)
        
    def exec(self, player):
        if self.useMadEffect(player):
            pass
        else:
            Card06.exec(self, player)

class Card17(MadCard, Card07):
    def __init__(self):
        MadCard.__init__(17)
        
    def exec(self, player):
        if self.useMadEffect(player):
            pass
        else:
            Card07.exec(self, player)

class Card18(MadCard, Card08):
    def __init__(self):
        MadCard.__init__(18)
        
    def exec(self, player):
        if self.useMadEffect(player):
            pass
        else:
            Card08.exec(self, player)

