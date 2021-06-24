import Powerup

# increases player's walk speed
class SpeedBoost(Powerup):
  
  def __init__ (self):
    Powerup.__init__(self, type)
    self.type = "movement"
  
  def speed_boost ():
    if(move_right):
          x += 4
      if(move_left):
          x -= 4
      if(move_up):
          y -= 4
      if(move_down):
          y += 4
