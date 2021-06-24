import game
import Powerup

# replaces shield with a shield that can absorb incoming projectiles
class Absorb_shield (Powerup):
  
  def __init__(self):
    Powerup.__init__(self, type)
    self.type = "shield"
  
  # absorbing projectiles can heal the player
  def absorb ():
    pass
