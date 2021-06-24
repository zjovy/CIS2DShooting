import Enemy

class Archer (Enemy):
  
  def __init__(self):
    Enemy.__init__(self, damage, range, score)
    self.damage = 10
    self.range = 50
    self.score = 40
