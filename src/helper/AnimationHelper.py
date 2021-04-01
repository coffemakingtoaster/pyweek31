from .. import config


class AnimatedGameObject():
    def __init__(self,x,y,assets):
        self.x = 0
        self.y = 0
        self.ticks_passed = 0
        self.assets = assets
    
    def get_current_asset(self,needs_update):
        if needs_update:
             self.ticks_passed +=1
        print("tick:{}".format(self.ticks_passed))
        if self.ticks_passed < config.FRAME_TIME:          
            return self.assets[0]
        elif self.ticks_passed == config.FRAME_TIME*2:
            self.ticks_passed = 0          
        return self.assets[1]
            
        
            