import Enemy

class Magician(Enemy):
  
  def __init__ (self):
    Enemy.__init__(self, damage, range, score)
    self.damage = 30
    self.range = 60
    self.score = 60
    
  # the magician can fire an AOE fireball attack at the player  
  def area_attack():
    pass
    
