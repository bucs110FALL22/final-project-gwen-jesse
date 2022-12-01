class Controller:
  
  def __init__(self):
    pygame.init()
    pygame.display.init()
    x , y = 640, 400
    window = pygame.display.set_mode((x,y))

  def mainloop(self):
    def riddle():
      while True:
        for attempts in range(4):
          for answers in print_dictionary():
            if answers == True:
              print(square_1())
              if attempts in print_dictionary <= 3 and answers == True:
                print(square_2())
                if attempts in print_dictionary <= 2 and answers == True:
                  print(square_3())
                  if attempts in print_dictionary <= 1 and answers == True:
                    print(square_4())
                    pygame.time.wait(2000)
                    print(picture())
                    pygame.time.wait(3000)
                    print("Yay you unlocked this image")
                    if attempts in print_dictionary < 1: 
                      break 
                    else:
                      return False 
                      print("Try again"

  
  def menuloop(self):
    
    def picture():
      image = pygame.transform.scale(pygame.image.load('shrek.png'),(640,400))
      window.blit(image,(0,0))
      pygame.display.update()
      pygame.display.flip()
      pygame.time.wait(2000)
    
    def square_1():
      location_1 = pygame.Rect(0, 0, 100, 90)
      pygame.draw.rect(window,"red", location_1)
      pygame.display.flip()
      pygame.time.wait(2000)
    
    def square_2():
      location_2 = pygame.Rect(0, 0, 200, 100)
      pygame.draw.rect(window,"red", location_2)
      pygame.display.flip()
      pygame.time.wait(2000)
    
    def square_3():
      location_3 = pygame.Rect(0, 0, 440, 200)
      pygame.draw.rect(window,"red", location_3)
      pygame.display.flip()
      pygame.time.wait(2000)
    
    def square_4():
      location_4 = pygame.Rect(0, 0, 640, 400)
      pygame.draw.rect(window,"red", location_4)
      pygame.display.flip()
      pygame.time.wait(2000)
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
