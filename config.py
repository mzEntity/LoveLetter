from common.singleton import singleton
from common.utils import read_json

@singleton
class Config:
    def __init__(self):
        self.CARD_CONFIG_PATH = "config/cards.json"
        self.EFFECT_CONFIG_PATH = "config/effect.json"
        self.SERVER_ADDRESS = ('localhost', 12345)
        self.init_card()
        self.init_effect()
        
        
    def init_card(self):
        self.CARD_CONFIG = {}
        card_config = read_json(self.CARD_CONFIG_PATH)
        for item in card_config:
            cfg = {
                "point": item["point"],
                "name": item["name"],
                "description": item["description"],
                "count": item["count"],
                "isMadCard": item["isMadCard"]
            }
            if cfg["isMadCard"]:
                cfg["madDescription"] = item["madDescription"]
            
            self.CARD_CONFIG[item["index"]] = cfg
                
    def init_effect(self):
        self.EFFECT_CONFIG = {}
        effect_config = read_json(self.EFFECT_CONFIG_PATH)
        for item in effect_config:
            cfg = {
                "description": item["description"],
            }
            self.EFFECT_CONFIG[item["index"]] = cfg
        # print(self.EFFECT_CONFIG)
