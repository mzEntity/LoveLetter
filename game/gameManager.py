from game.game import Game, GameOverException, CthulhuException
from game.card import *
from common.logger import Logger
    
class GameManager:
    def __init__(self, player_count):
        self.player_count = player_count
        
        self.game = Game()
        self.game.init_players(self.player_count)
        self.game.init_cards(CardBuilder())
        
        self.win_point = {}
        for i in range(self.player_count):
            self.win_point[i] = {
                "lucid": 0,
                "mad": 0
            }
        
        
    def start(self):
        try:
            for i in range(self.player_count):
                DrawToHandCommand(self.game.players[i], 1).run()
            while not self.game.over:
                self.one_round()
        except GameOverException as e:
            if self.game.onlyWinner is None:
                winners = self.game.compare()
            else:
                winners = [self.game.onlyWinner]
            
            final_winners = []
            for winner in winners:
                if winner.isMad:
                    self.win_point[winner.id]["mad"] += 1
                    if self.win_point[winner.id]["mad"] >= 3:
                        Logger().info(f"{winner} 获得三个发疯标记")
                        final_winners.append(winner)
                else:
                    self.win_point[winner.id]["lucid"] += 1
                    if self.win_point[winner.id]["lucid"] >= 2:
                        Logger().info(f"{winner} 获得两个清醒标记")
                        final_winners.append(winner)
            if final_winners:
                self.all_over(final_winners)
        except CthulhuException as e:
            Logger().info(f"{e.player} 打出了克苏鲁")
            self.all_over([e.player])
            
    def all_over(self, players):
        Logger().info(f"{players} is the final winner.")
    
    
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
        # if game ends, calc result now
    
    
if __name__ == "__main__":
    g = GameManager(3)
    g.start()