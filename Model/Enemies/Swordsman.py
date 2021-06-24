import Enemy

# melee enemy, short range attacks
class Swordsman (Enemy):
  
  def  __init__ (self, range):
    Enemy.__init__(self, damage, score)
    self.range = range
    self.damage = 10
    self.score = 30
