from ...config import *
from ...superclasses import Item
import time, threading

class Coffee(Item.Item):
    def __init__(self, logic):
        super().__init__('coffee', logic)
        self.speed_boost = ITEM_COFFEE_SPEED_BOOST
        self.duration = ITEM_COFFEE_DURATION
        
    def drink(self):
        self.logic.player.speed = self.logic.player.speed * self.speed_boost
        threading.Timer(self.duration, self.digest).start()
        print(self.logic.player.speed)
        
    def digest(self):
        print("Coffee is digested") 
        self.logic.player.speed = PLAYER_SPEED