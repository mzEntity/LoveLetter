from game.game import Game
from common.logger import Logger
from player import Player
from card import Card

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
        self.player:Player = player

    def run(self):
        self.player.escape = False

        if Game().over: return

        # TODO: 拉莱耶判断
        if self.player == Game().rlyehPlayer:
            # TODO: should ask
            pass

        if Game().over: return

        # TODO: san check
        # check_count = sum([1 for card in self.player.discard_deck.cards if card.isMad])
        # ls = DiscardFromPublicCommand(self.player, check_count).run()
        SanCheckCommand(self.player).run()

        # draw card
        DrawToHandCommand(self.player, 1).run()
        
        # use card
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

class SanCheckCommand(Command):
    pass