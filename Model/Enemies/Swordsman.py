import Enemy

# melee enemy, short range attacks
class Swordsman (Enemy):
  
  def  __init__ (self):
    Enemy.__init__(self, damage, score)
    self.damage = 10
    self.range = 5
    self.score = 30
