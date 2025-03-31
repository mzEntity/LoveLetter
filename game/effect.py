from config import Config
from game.game import Game
import random
from common.logger import Logger
from game.command import *
from game.player import Player


class Effect:
    def __init__(self, description):
        self.description = description
    
    def exec(self, player:Player):
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
        

# 拉莱耶        
class Mad10(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[10]["description"])
        
    def exec(self, player):
        super().exec(player)
        Game().isDeckReversed = True
        Game().rlyehPlayer = player


# 异教徒
class Mad11(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[11]["description"])
        
    def exec(self, player):
        super().exec(player)
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
class Mad12(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[12]["description"])
        
    def exec(self, player):
        super().exec(player)
        Lucid02().exec(player)

        player.skipSanCheck = True
        PerformTurnCommand()


# 深潜者
class Mad13(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[13]["description"])
        
    def exec(self, player):
        super().exec(player)

        target:Player = Game().choose_other_player(player, lambda p: not p.isMad)
        target.die()


# 《死灵之书》
class Mad14(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[14]["description"])
        
    def exec(self, player):
        super().exec(player)
        player.protectedByNecro = True


# 偷渡虫
class Mad15(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[15]["description"])
        
    def exec(self, player):
        super().exec(player)
        
        target:Player = Game().choose_other_player(player)
        player.hand_deck.put_top(target.hand_deck.get_all())
        target.hand_deck.put_top(Game().special_deck.get_all())


# 兰道尔·蒂林哈斯特
class Mad16(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[16]["description"])
        
    def exec(self, player):
        super().exec(player)
        for target in [p for p in Game().players if p != player]:
            player.hand_deck.put_top(target.hand_deck.getall())
        # TODO: should ask
        for target in [p for p in Game().players if p != player]:
            target.hand_deck.put_top(player.hand_deck.get_bottom())


# 修格斯
class Mad17(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[17]["description"])
        
    def exec(self, player):
        super().exec(player)
        if player.get_hand_card().point >= 5:
            Game().onlyWinner = player
            Game().game_over(f"{player.id} played Shoggoth.")


# 克苏鲁
class Mad18(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[18]["description"])
        
    def exec(self, player):
        super().exec(player)


# 偷渡虫蛋
class Mad20(Effect):
    def __init__(self):
        super().__init__(Config().EFFECT_CONFIG[20]["description"])

    def exec(self, player):
        super().exec(player)