import pygame
import pygame.mixer
from questions import Questions
from constants import *

class Controller():
  def __init__(self):

    pygame.mixer.init()
    pygame.init()
    pygame.display.init()
    x , y = 200 , 400
    self.window = pygame.display.set_mode((x,y))
    background = "white"
    self.window.fill(background)
    pygame.display.flip()
    
    self.window.fill("black")
    red_rect = pygame.Rect(0, 200, 100, 100)
    blue_rect = pygame.Rect(100, 200, 100, 100)
    green_rect = pygame.Rect(0, 300, 100, 100)
    yellow_rect = pygame.Rect(100, 300, 100, 100)
    self.red_guess = pygame.draw.rect(self.window, "red", red_rect)
    self.blue_guess = pygame.draw.rect(self.window, "blue", blue_rect)
    self.green_guess = pygame.draw.rect(self.window, "green", green_rect)
    self.yellow_guess = pygame.draw.rect(self.window, "yellow", yellow_rect)
    pygame.display.flip()
    
    self.questions = [
      Questions(prompt[0], 'red',filename[0]),
      Questions(prompt[1], 'green',filename[1]),
      Questions(prompt[2], 'red',filename[2]),
      Questions(prompt[3], 'blue', filename[3]),
      Questions(prompt[4], 'yellow', filename[4]),
      Questions(prompt[5], 'blue', filename[5]),
      Questions(prompt[6], 'red', filename[6]),
      Questions(prompt[7], 'green', filename[7]),
      Questions(prompt[8], 'yellow', filename[8]),
      Questions(prompt[9], 'red', filename[9])
    ]
  
  
  def quiz_test(self):
    color = ['red','blue','green','yellow']
    score = 0
    q_num = 0
    pygame.mixer.music.load("assets/quiz-121408.mp3")
    pygame.mixer.music.set_volume(4)
    pygame.mixer.music.play()
    for question in self.questions:
      print(question.prompt)
      answer = True
      while answer == True:  
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if self.red_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[0]
              print("Your picked RED")
            elif self.blue_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[1]
              print("You picked BLUE")
            elif self.green_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[2]
              print("You picked GREEN")
            elif self.yellow_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[3]
              print("You picked YELLOW")
        picture = pygame.transform.scale(pygame.image.load(self.questions[q_num].filename),(200,200))
        self.window.blit(picture,(0,0))
        pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(2000)
      if answer == question.answer:
        print("You are correct!")
        score += 1
        q_num += 1
      else:
        print("You are wrong")
        q_num += 1
    print("You got" + str(score) + "/" + str(len(questions) + "correct"))

test = Controller()
test.quiz_test()