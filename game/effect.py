from config import Config
from game.game import Game
import random
from common.logger import Logger
from game.command import *


class Effect:
    def __init__(self, description):
        self.description = description
    
    def exec(self, player):
        print(f"player{player.id} 执行 '{self.description}' 效果")


class Lucid00(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[0]["description"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        DiscardFromPublicCommand(target, 2).run()
        
        
class Lucid01(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[1]["description"])
        
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
        
        
class Lucid02(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[2]["description"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        card = target.get_hand_card()
        Logger().info(f"查看了牌: {card}")
        
        
class Lucid03(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[3]["description"])
        
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
            
        
class Lucid04(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[4]["description"])
        
    def exec(self, player):
        super().exec(player)
        Logger().info(f"本回合player{player.id}不能被其他人的牌选中")
        player.escape = True
        
        
class Lucid05(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[5]["description"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        DiscardFromHandCommand(target, 1).run()
        DrawToHandCommand(target, 1).run()
        
        
class Lucid06(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[6]["description"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        ExchangeHandCommand(player, target).run()
        
        
class Lucid07(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[7]["description"])
        
    def exec(self, player):
        super().exec(player)
        
        
class Lucid08(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[8]["description"])
        
    def exec(self, player):
        super().exec(player)
        player.die()
        
        
        
class Mad10(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[10]["description"])
        
    def exec(self, player):
        super().exec(player)
        pass
        
        
class Mad11(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[11]["description"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        
        card = target.get_hand_card()
        if card.point == 1:
            Logger().info(f"存在点数为1的卡牌：{card}")
            target.die()
            return
        
        Logger().info(f"不存在点数为1的卡牌")
        guess = random.randint(0, 8)    
        if card.point == guess:
            Logger().info(f"猜中了牌的点数({guess}): {card}")
            target.die()
        else:
            Logger().info(f"猜了牌的点数({guess})，猜错了")
        
        
class Mad12(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[12]["description"])
        
    def exec(self, player):
        super().exec(player)
        Lucid02().exec(player)
        PerformTurnCommand(player).run()
        
        
class Mad13(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[13]["description"])
        
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
            
        
class Mad14(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[14]["description"])
        
    def exec(self, player):
        super().exec(player)
        Logger().info(f"本回合player{player.id}不能被其他人的牌选中")
        player.escape = True
        
        
class Mad15(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[15]["description"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        DiscardFromHandCommand(target, 1).run()
        DrawToHandCommand(target, 1).run()
        
        
class Mad16(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[16]["description"])
        
    def exec(self, player):
        super().exec(player)
        target = Game().choose_player(player)
        ExchangeHandCommand(player, target).run()
        
        
class Mad17(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[17]["description"])
        
    def exec(self, player):
        super().exec(player)
        
        
class Mad18(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[18]["description"])
        
    def exec(self, player):
        super().exec(player)
        player.die()