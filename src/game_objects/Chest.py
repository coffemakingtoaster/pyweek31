from random import choices

from ..superclasses.InteractiveObject import *
from .. import config

class Chest(InteractiveObject):

    def __init__(self,rect):
        super().__init__()
        self.x = rect.x
        self.y = rect.y
        self.height = rect.height
        self.width = rect.width
        self.is_empty = False
        self.possible_items = ["coin","donut","coffee","jammer"]
        self.probabilities = [config.ITEM_COIN_CHANCE,config.ITEM_DONUT_CHANCE,config.ITEM_COFFEE_CHANCE,config.ITEM_JAMMER_CHANCE]

    def update(self):
        pass

    def open(self):
        if self.is_empty:
            return None
        self.is_empty = True
        return choices(population=self.possible_items,weights=self.probabilities)[0]
