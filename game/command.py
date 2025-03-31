from game.game import Game
from common.logger import Logger
from game.player import Player

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
        if Game().over or self.player.dead: 
            return

        if self.player == Game().rlyehPlayer:
            ask_result = self.askForRlyehPlayer()
            if ask_result:
                Game().game_over(f"{self.player}决定提前结束游戏")
                return
            
        if Game().over or self.player.dead: 
            return
        if self.player.skipSanCheck:
            self.player.skipSanCheck = False
        else:
            SanCheckCommand(self.player).run()
        
        if Game().over or self.player.dead:
            return
        # draw card
        DrawToHandCommand(self.player, 1).run()
        
        if Game().over or self.player.dead:
            return
        
        top_deck = self.player.hand_deck.get_top(1)
        card = top_deck[0]
        card.exec(self.player)
        self.player.add_card_to_discard(top_deck)
        
    def askForRlyehPlayer(self):
        return True
        

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
        containsEight = False
        for c in deck:
            if c.point == 8:
                containsEight = True
                
        Logger().info(f"{self.player} 从手牌中弃置了以下牌：{deck}")
        self.player.add_card_to_discard(deck)
        
        if containsEight:
            DieCommand(self.player).run()
        
    

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
        self.player.add_card_to_discard(deck)
    

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
    def __init__(self, player):
        super().__init__(f"{player} 进行神智鉴定")
        self.player = player
        
    def run(self):
        discard_deck = self.player.discard_deck
        mad_count = 0
        for c in discard_deck:
            if c.isMad:
                mad_count += 1

        Logger().info(f"{self.player} 需要进行 {mad_count} 张神智检定")
        deck = Game().public_deck.get_top(mad_count)
        if len(deck) < mad_count:
            Game().game_over("牌堆空了")
            return
        Logger().info(f"判定牌为：{deck}")
        hasMad = False
        for c in deck:
            if c.isMad:
                hasMad = True
        self.player.add_card_to_discard(deck)
        if hasMad:
            DieCommand(self.player).run()
            
            
class DieCommand(Command):
    def __init__(self, player):
        super().__init__(f"{player} 死亡")
        self.player = player
        
    def run(self):
        if self.player.protectedByNecro:
            Logger().info(f"{self.player} 逃避死亡")
            return
        Logger().info(f"{self.player}死亡")
        deck = self.player.hand_deck.get_all()
        self.player.die()
        Game().survived_players.remove(self.player)
        Logger().info(f"{self.player} 从手牌中弃置了以下牌：{deck}")
        self.player.add_card_to_discard(deck)
        
        if len(Game().survived_players) == 1:
            Game().game_over("仅剩一人存活")
        
        