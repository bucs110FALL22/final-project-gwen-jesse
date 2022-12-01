import pygame 

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.window = pygame.display.set_mode()
    window_size = pygame.display.get_window_size('the maze')
    self.maze_background = [
      'assets/maze.png'  
    ]
    self.move = True

  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
 
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
