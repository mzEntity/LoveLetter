from config import Config
from game.game import Game
from common.singleton import singleton
import random
from common.logger import Logger

class Card:
    def __init__(self, point, name, description, isMad):
        self.point = point
        self.name = name
        self.description = description
        self.isMad = isMad
        
    def __repr__(self):
        if self.isMad:
            return f"*[{self.point}]{self.name}*"
        else:
            return f"[{self.point}]{self.name}"
    
    def exec(self, player):
        print(f"player{player.id} 打出 {self} 执行...")
    

class Card00(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[0]["point"], 
                         Config().CARD_CONFIG[0]["name"], 
                         Config().CARD_CONFIG[0]["description"], 
                         Config().CARD_CONFIG[0]["isMadCard"])
        
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        DiscardFromPublicCommand(target, 2).run()
        
        
class Card01(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[1]["point"], 
                         Config().CARD_CONFIG[1]["name"], 
                         Config().CARD_CONFIG[1]["description"], 
                         Config().CARD_CONFIG[1]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        
        guess = random.randint(0, 8)
        card = target.get_hand_card()
        
        if card.point == guess:
            Logger().info(f"猜中了牌的点数({guess}): {card}")
            target.die()
        else:
            Logger().info(f"猜了牌的点数({guess})，猜错了")
        
        
        
class Card02(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[2]["point"], 
                         Config().CARD_CONFIG[2]["name"], 
                         Config().CARD_CONFIG[2]["description"], 
                         Config().CARD_CONFIG[2]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        card = target.get_hand_card()
        Logger().info(f"查看了牌: {card}")
        
        
class Card03(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[3]["point"], 
                         Config().CARD_CONFIG[3]["name"], 
                         Config().CARD_CONFIG[3]["description"], 
                         Config().CARD_CONFIG[3]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        own_card = player.get_hand_card()
        target_card = target.get_hand_card()
        
        Logger().info(f"player{player.id}的手牌点数为{own_card.point}， player{target.id}的手牌点数为{target_card.point}")
        if own_card.point > target_card.point:
            Logger().info(f"player{player.id}赢了")
            target.die()
        elif own_card.point == target_card.point:
            Logger().info("两者平局")
        else:
            Logger().info(f"player{target.id}赢了")
            player.die()
            
        
class Card04(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[4]["point"], 
                         Config().CARD_CONFIG[4]["name"], 
                         Config().CARD_CONFIG[4]["description"], 
                         Config().CARD_CONFIG[4]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        Logger().info(f"本回合player{player.id}不能被其他人的牌选中")
        player.escape = True
        
        
class Card05(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[5]["point"], 
                         Config().CARD_CONFIG[5]["name"], 
                         Config().CARD_CONFIG[5]["description"], 
                         Config().CARD_CONFIG[5]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        DiscardFromHandCommand(target, 1).run()
        DrawToHandCommand(target, 1).run()
        
        
class Card06(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[6]["point"], 
                         Config().CARD_CONFIG[6]["name"], 
                         Config().CARD_CONFIG[6]["description"], 
                         Config().CARD_CONFIG[6]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        ExchangeHandCommand(player, target).run()
        
        
class Card07(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[7]["point"], 
                         Config().CARD_CONFIG[7]["name"], 
                         Config().CARD_CONFIG[7]["description"], 
                         Config().CARD_CONFIG[7]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        
        
class Card08(Card):
    def __init__(self):
        super().__init__(Config().CARD_CONFIG[8]["point"], 
                         Config().CARD_CONFIG[8]["name"], 
                         Config().CARD_CONFIG[8]["description"], 
                         Config().CARD_CONFIG[8]["isMadCard"])
        
    def exec(self, player):
        super().exec(player)
        player.die()


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
    
    
class Command:
    def __init__(self, description):
        self.description = description
    
    def run(self):
        pass
    
    def __repr__(self):
        return self.description
    

class PerformTurnCommand(Command):
    def __init__(self, player):
        super().__init__(f"{player}执行一个回合")
        self.player = player

    def run(self):
        self.player.escape = False
        DrawToHandCommand(self.player, 1).run()
        top_deck = self.player.hand_deck.get_top(1)
        card = top_deck[0]
        card.exec(self.player)
        self.player.discard_deck.put_bottom(top_deck)
        

class DrawToHandCommand(Command):
    def __init__(self, player, count):
        super().__init__(f"{player}从牌堆中抽取{count}张牌")
        self.player = player
        self.count = count
        
    def run(self):
        deck = Game().public_deck.get_top(self.count)
        if len(deck) < self.count:
            Game().game_over("牌堆空了")
            return
        Logger().info(f"{self.player} 从牌库顶抽取了以下牌：{deck}")
        self.player.hand_deck.put_bottom(deck)
    

class DiscardFromHandCommand(Command):
    def __init__(self, player, count):
        super().__init__(f"{player}从手中弃置{count}张牌")
        self.player = player
        self.count = count
        
    def run(self):
        deck = self.player.hand_deck.get_top(self.count)
        if len(deck) < self.count:
            return
        Logger().info(f"{self.player} 从手牌中弃置了以下牌：{deck}")
        self.player.discard_deck.put_bottom(deck)
    

class DiscardFromPublicCommand(Command):
    def __init__(self, player, count):
        super().__init__(f"{player}从牌堆顶弃置{count}张牌")
        self.player = player
        self.count = count
        
    def run(self):
        deck = Game().public_deck.get_top(self.count)
        if len(deck) < self.count:
            Game().game_over("牌堆空了")
            return
        Logger().info(f"{self.player} 从牌堆顶弃置了以下牌：{deck}")
        self.player.discard_deck.put_bottom(deck)
    

class ExchangeHandCommand(Command):
    def __init__(self, player1, player2):
        super().__init__(f"交换{player1}和{player2}的手牌")
        self.player1 = player1
        self.player2 = player2
        
    def run(self):
        deck1 = self.player1.hand_deck.get_all()
        deck2 = self.player2.hand_deck.get_all()
        self.player1.hand_deck.put_top(deck2)
        self.player2.hand_deck.put_top(deck1)
        