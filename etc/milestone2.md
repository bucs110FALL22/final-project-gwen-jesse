
# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1
class Character:
'''
Creates the player in our maze game and sets it to the rest position (0,0) on screen. It will allow players to move on screen using the arrow keys. 
'''
  def __init__(self):
    self.position = (0,0)
    self.up()
    self.down()
    self.left()
    self.right()
    self.image = (str)

  
## Class Interface 2
class Riddle:
'''
The Riddle is placed at the end of each level to move on to more challanging levels in the game. It will uses text that displays the riddle using a random generator from a dictionary.
'''
  def __init__(self):
    self.text = str()
    self.answer_space()
    
  def dictionary():
    random_select([#,"associated to the riddle"])
    

## Class Interface 3
class Maze_lines:
'''
The Maze line creates the boarders in the game and is used as the "wall" on the surface so that creates the puzzle the players will have to solve. It uses Turtle to draw the lines on the game using position and the turtle interface. 
'''
  def __init__(self):
    self.pen = turtle.Turtle()
    self.pen_goto = (x,y)
    self.forward()
    self.backward()
    self.pen_up()
    self.pen_down()

======================================================================
