class Enemy:
  
  def __init__ (self, damage, range, score):
    self.health = 100
    self.damage = damage
    self.range = range
    self.score = score
   
  def attack(self, opponent):
    damage_dealt = self.damage
    opponent.take_damage(damage_dealt)
    
  def take_damage(self, damage_dealt):
    self.health -= damage_dealt
    
  def alive(self):
    return self.health > 0
  
