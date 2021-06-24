class Player:
  
  def __init__ (self):
    self.health = 100
    self.powerups = []
    self.damage = 20
    self.speed = 2
    self.score = 0
  
  def score_up (self, score):
    self.score += score
    
  def attack(self, opponent):
    damage_dealt = self.damage
    opponent.take_damage(damage_dealt)
    
  def take_damage(self, damage_dealt):
    self.health -= damage_dealt
    
  def alive(self):
    return self.health > 0
