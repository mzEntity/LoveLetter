import random
from common.logger import Logger


class Deck:
    def __init__(self, card_list=[]):
        self.cards = []
        for c in card_list:
            self.cards.append(c)
        self.index = 0
                 
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        value = self.cards[self.index]
        self.index += 1
        return value

    def __getitem__(self, index):
        return self.cards[index]

    def __len__(self):
        return len(self.cards)
    
    def get_top(self, count):
        if len(self.cards) < count:
            Logger().warning(f"get_top: 牌堆数量不够，需要{count}，只有{len(self.cards)}，这可能会出错……")
            count = len(self.cards)
            
        deck = Deck(self.cards[:count])
        self.cards = self.cards[count:]
        return deck
    
    
    def get_bottom(self, count):
        if len(self.cards) < count:
            Logger().warning(f"get_bottom: 牌堆数量不够，需要{count}，只有{len(self.cards)}，这可能会出错……")
            count = len(self.cards)
            
        deck = Deck(self.cards[-count:])
        self.cards = self.cards[:-count]
        return deck
    
    def get_all(self):
        return self.get_top(len(self.cards))
        
    def put_top(self, deck):
        deck.cards.extend(self.cards)
        self.cards = deck.cards
        deck.cards = []
        
    def put_bottom(self, deck):
        self.cards.extend(deck.cards)
        deck.cards = []
            
    def shuffle(self):
        random.shuffle(self.cards)
        
    def printDeck(self):
        for card in self.cards:
            print(card)
            
    def __repr__(self):
        s = "Deck("
        for card in self.cards:
            s += str(card) + ", "
        if self.cards:
            s = s[:-2]
        s += ")"
        return s


if __name__ == "__main__":
    deck = Deck([1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    top3 = deck.get_top(3)
    for i in deck:
        print(i)
        
    for i in top3:
        print(i)
        
    print(top3[2])