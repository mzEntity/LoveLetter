from game.deck import Deck
from common.singleton import singleton

from game.player import Player
from common.logger import Logger


@singleton
class Game:
    def __init__(self):
        self.public_deck = Deck()
        self.removed = Deck()
        self.over = False
        
        self.players = []
        self.player_count = 0

        self.onlyWinner = None
        self.isDeckReversed = False
        self.rlyehPlayer:None|Player = None
        
    
    def init_players(self, player_count):
        self.player_count = player_count
        self.players = []
        for i in range(self.player_count):
            self.players.append(Player(i))
            
            
    def init_cards(self, card_builder):
        self.public_deck = Deck(card_builder.cards[:])
        self.special_deck = Deck([card_builder.cardEgg])

            
    def game_over(self, reason):
        self.over = True
        Logger().info(f"游戏结束: {reason}")
        
        
    def choose_player(self, player):
        current_player_id = player.id
        for i in range(self.player_count):
            if i == current_player_id:
                continue
            chosen = self.players[i]
            if chosen.escape:
                Logger().info(f"准备选择player{chosen.id} 但不可被选中") 
                continue
            elif chosen.dead:
                Logger().info(f"准备选择player{chosen.id} 但已经出局") 
                continue
            Logger().info(f"选择了player{chosen.id}")
            return chosen
        Logger().info(f"选择了player{player.id}")
        return player
    
    def choose_any_player(self, player, filter = None):
        pass

    def choose_other_player(self, player, filter = None):
        pass