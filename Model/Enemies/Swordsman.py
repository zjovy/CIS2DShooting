import Enemy

# melee enemy, short range attacks
class Swordsman (Enemy):
  
  def  __init__ (self, range):
    Enemy.__init__(self, attack, score)
    self.range = range
    self.score = 30
