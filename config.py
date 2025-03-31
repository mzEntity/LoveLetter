from common.singleton import singleton
from common.utils import read_json

@singleton
class Config:
    def __init__(self):
        self.CARD_CONFIG_PATH = "config/cards.json"
        self.SERVER_ADDRESS = ('localhost', 12345)
        self.init_card()
        
        
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
            
            self.CARD_CONFIG[item["index"]] = cfg
                

