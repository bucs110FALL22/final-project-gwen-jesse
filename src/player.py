import pygame
pyagme.init()
window = pygame.display.set_mode 

class Player(pygame.sprite.Sprite):
  def __init__(self,x,y):
    syper().__init__(self)
    self.image = pygame.image.load("...jpg...").convert_alpha()
    self.rect = self.image.get_rect()
    self.position = (x,y)
    self.player.shirt_color(int(input("Your favorite color")
    self.health = 3 
    self.right = arrowkey right 
    self.left = arrowkey left
    self.up = arrowkey up
    self.down = arrowkey down 
    