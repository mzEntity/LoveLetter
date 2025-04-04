from game.deck import Deck
from common.singleton import singleton

from game.player import Player
from common.logger import Logger
from game.interact import askForNumber, askForChoice

@singleton
class Game:
    def __init__(self):
        self.public_deck = Deck()
        self.removed = Deck()
        
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
        Logger().info(f"游戏结束: {reason}")
        raise GameOverException(reason)
        
    def compare(self):
        return [self.survived_players[0]]
        
            
    def choose_any_player(self, player, filter = None):
        all_list = list(range(self.player_count))
        available_list = []
        for i in all_list:
            target_player = self.players[i]
            if filter is not None:
                if not filter(target_player):
                    continue
            if target_player.escape or target_player.dead:
                continue
            available_list.append(i)
            
        if len(available_list) == 0:
            Logger().info("没有任何玩家可以被选择")
            return None
            
        chosen_id = askForNumber("请选择一位目标玩家：", available_list)
        chosen_player = self.players[chosen_id]
        
        Logger().info(f"选择了{chosen_player}")
        return chosen_player

    def choose_other_player(self, player, filter = None):
        current_player_id = player.id
        all_list = list(range(self.player_count))
        available_list = []
        for i in all_list:
            if current_player_id == i:
                continue
            target_player = self.players[i]
            if filter is not None:
                if not filter(target_player):
                    continue
            if target_player.escape or target_player.dead:
                continue
            available_list.append(i)
        
        if len(available_list) == 0:
            Logger().info("没有任何玩家可以被选择")
            return None
        
        chosen_id = askForNumber("请选择一位目标玩家：", available_list)
        chosen_player = self.players[chosen_id]
        
        Logger().info(f"选择了{chosen_player}")
        return chosen_player
    
    def ask_for_choice(self, prompt, available_choices_dict):
        return askForChoice(prompt, available_choices_dict)
    
    def choose_a_point(self):
        return askForNumber("请选择牌的点数：", [0, 2, 3, 4, 5, 6, 7, 8])
    
    def choose_a_card_in_hand(self, prompt, player):
        card_list = []
        for c in player.hand_deck:
            card_list.append(c)
        choice = self.ask_for_choice(prompt, {str(idx+1): card for idx, card in enumerate(card_list)})
        deck_chosen = player.hand_deck.get_index(int(choice) - 1)
        return deck_chosen
    
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