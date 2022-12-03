:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
###   Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)


https://replit.com/join/vmrlclcdfa-gwendolynoh


<< [link to demo presentation slides](#) >>

### Team:  Gwen & Jesse 
####  Gwendolyn Oh, Jesse Fonte 

***

## Project Description
Our project is a Kahoot like game. We ask the user who is this celebrity and provide a picture of the celebrity then ask them to choose a colored box.

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
- class Player
  - '''
Creates the player in our maze game and sets it to the rest position (0,0) on screen. It will allow players to move on screen using the arrow keys. Also imports sprites which shows the different the positon the character can be so it can show movement on screen.
'''
-class Riddle
'''
The Riddle is placed at the end of each level to move on to more challanging levels in the game. It will uses text that displays the riddle using a random generator from a dictionary.
'''

-class Maze 
'''
The Maze line creates the boarders in the game and is used as the "wall" on the surface so that creates the puzzle the players will have to solve. It uses Turtle to draw the lines on the game using position and the turtle interface. 
'''

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 
We worked as a team bouncing ideas off one another. Although, Jesse was responsible for getting the pictures of the celebrites and Gwen was responsible for making the quiz dictionary. Other than that, we both worked together to figure it out. 
## Testing
We did not hesistate to test. Right after we would make a loop we would test it. We also tested each step individually just to make sure that it was working, for example: making the picture appear, next we tested to make sure the picture and the boxes appeared, then we tested to make sure the boxes worked, then we kept testing to see if the quiz would work with the boxes, and so on. 

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
