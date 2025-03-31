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
        self.survived_players = []
        self.player_count = 0

        self.onlyWinner = None
        self.isDeckReversed = False
        self.rlyehPlayer = None
        
    
    def init_players(self, player_count):
        self.player_count = player_count
        self.players = []
        for i in range(self.player_count):
            self.players.append(Player(i))
        self.survived_players = self.players[:]
            
            
    def init_cards(self, card_builder):
        self.public_deck = Deck(card_builder.cards[:])
        self.public_deck.shuffle()
        self.special_deck = Deck([card_builder.cardEgg])

            
    def game_over(self, reason):
        self.over = True
        Logger().info(f"游戏结束: {reason}")
        raise GameOverException(reason)
        
    def compare(self):
        return [self.survived_players[0]]
        
            
    def choose_any_player(self, player, filter = None):
        current_player_id = player.id
        for i in range(self.player_count):
            if i == current_player_id:
                continue
            chosen = self.players[i]
            if filter is not None:
                if not filter(chosen):
                    Logger().info(f"准备选择player{chosen.id} 但不是合法目标") 
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

    def choose_other_player(self, player, filter = None):
        current_player_id = player.id
        for i in range(self.player_count):
            if i == current_player_id:
                continue
            chosen = self.players[i]
            if filter:
                if not filter(chosen):
                    Logger().info(f"准备选择player{chosen.id} 但不是合法目标") 
            if chosen.escape:
                Logger().info(f"准备选择player{chosen.id} 但不可被选中") 
                continue
            elif chosen.dead:
                Logger().info(f"准备选择player{chosen.id} 但已经出局") 
                continue
            Logger().info(f"选择了player{chosen.id}")
            return chosen
        Logger().info(f"无法选择任何角色")
        return None
    
class GameOverException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
    
    
class CthulhuException(Exception):
    def __init__(self, player):
        self.player = player
    
    def __str__(self):
        return f"{self.player} played Cthulhu."