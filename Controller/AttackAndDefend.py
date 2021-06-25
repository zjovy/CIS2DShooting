import pygame

def alternate_attack_defend ():
  current = "attack"
  mouse_presses = pygame.mouse.get_pressed()
  
  if mouse_presses[0] and current = "attack":
    current = "defend"
  elif mouse_presses[0] and current = "defend":
    current = "attack"
  
  return current
