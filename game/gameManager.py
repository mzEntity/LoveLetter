from game.game import Game
from game.card import *
from common.logger import Logger
    
class GameManager:
    def __init__(self, player_count):
        self.player_count = player_count
        
        self.game = Game()
        self.game.init_players(self.player_count)
        CardBuilder().build()
        self.game.init_cards(CardBuilder().cards)
                
        
    def start(self):
        for i in range(self.player_count):
            DrawToHandCommand(self.game.players[i], 1).run()
        while not self.game.over:
            self.one_round()
    
    
    def one_round(self):
        Logger().info(f"新的一轮开始...")
        for idx, player in enumerate(self.game.players):
            if self.game.over:
                break
            if player.dead:
                Logger().info(f"{player}已死亡，跳过回合")
                continue
            self.one_turn(player)
            
            
    def one_turn(self, player):
        id = player.id
        print(f"player {id} start")
        PerformTurnCommand(player).run()
    
    
if __name__ == "__main__":
    g = GameManager(3)
    g.start()