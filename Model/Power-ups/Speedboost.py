import Powerup
import Player

# increases player's walk speed
class SpeedBoost(Powerup):
  
  def __init__ (self):
    Powerup.__init__(self, type)
    self.type = "movement"
  
  def speed_boost (self):
    Player.speed = 4
