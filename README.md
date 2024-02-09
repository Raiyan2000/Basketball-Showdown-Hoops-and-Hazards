# BasketBall Showdown: Hoops & Hazards
This is an engaging basketball game designed to challenge players to reach a score of 15 points while avoiding obstacles and enemies. Developed using Python and Pygame, this 2-dimensional game offers an immersive experience with intuitive controls and dynamic gameplay elements.
# Motivation
1. 📐 Express Projectile Motion Math:

    * Translate theoretical concepts of projectile motion into practical, real-world code.
    * Implement algorithms that calculate ball trajectories, account for gravity effects, and handle user input interactions.
    * Showcase the ability to bring mathematical concepts to life through an interactive graphical user interface (GUI).

2. 🎮 Understand Game Structure:

    * Gain insights into the core components of game development.
    * Explore game loops, state management, user input handling, collision detection, and graphical rendering.
    * Develop a deep understanding of how to structure and design engaging games.

3. 🚀 Learn Python and Pygame:

    * Dive into the world of Python programming language.
    * Explore the features and capabilities of the Pygame library for game development.
    * Master Python syntax, functions, and object-oriented programming through hands-on coding.

# Key Features

<strong>Objective:</strong> The primary objective of the game is to score 15 points by shooting the basketball into the net while overcoming obstacles and enemies.

<strong>Game Mechanics:</strong> Players control a character using mouse input to navigate across the screen and aim their shots. The distance and direction of the ball are determined by the position of the mouse relative to the character.

<strong>Dynamic Challenges:</strong> As players progress, the game becomes increasingly challenging. The position of the net changes with each score increment, and enemies, including planes and bombs, are introduced to hinder the player's progress.

<strong>Finite-State Machine:</strong> The game operates using a finite-state machine, transitioning between states such as the main menu, gameplay, and end game sequences.

<strong>Physics Simulation:</strong> Realistic ball physics are simulated, incorporating projectile motion and gravity. Players must master the trajectory and power of their shots to succeed.

<strong>Collision Effects:</strong> Collision detection is implemented for interactions between the player, the ball, and obstacles/enemies. Engaging explosion effects accompany collisions, enhancing the gaming experience.
# Video
On maintenance
# Design Implementation
## Game Flow
This is a 2-dimensional game that requires the user to score points up to 15 
without getting hit by the enemies. After the user hits 15 points, the game will automatically end. 
The game operates using a finite-state machine. As shown in the flow chart in the figure below, the game 
starts with the user prompted to a main menu tab for the game. This is the starting state of the 
game. When the user presses the “start game” button, the state changes and initiates the game. 
This state is continuously looped to itself and there are two conditions to trigger the end game 
state. One way is for the user to score 15 points without getting hit by enemies. The other way is 
when the user gets hit by the enemy during the game. The enemies consist of two types: planes 
and bombs. The bombs spawn randomly from the top of the screen and fall vertically down. The 
planes spawn from the right end of the screen and travel horizontally. The planes will first spawn 
at score 5 and the bombs will start dropping at score 10. As the game_is_on state progresses, it
will increment the score if the user hits the net and randomly places the rim.
There are three main components that require both an understanding of theory and 
object-oriented programming. The main components are the math used to calculate the distance 
used to determine the direction and power of the ball, the implementation of the ball physics 
which requires an understanding of projectile motion, and the collision effect.

![gameflowchart](https://github.com/Raiyan2000/LED-Checkers-App-with-Voice-Recognition/assets/77954118/7b7cae1a-582d-40e3-b473-6550a57c0bb4)

## Power Calculation
The power and direction of the ball are determined by the position of the mouse to the 
character. A visible white line displays it for user support. The power is determined by the length 
of the line created from the mouse’s and the character’s X and Y coordinates. The equation used
to calculate this distance:

![distance math](https://github.com/Raiyan2000/LED-Checkers-App-with-Voice-Recognition/assets/77954118/01be635a-1512-47c2-b27f-92bb929f849e)

If the distance of the line is 500 pixels, it would mean the basketball would travel 500m/s across 
the screen. This would mean that the ball will cross the screen without our eyes noticing. Since 
the distance of the line exponentially increases the power of the ball, it was divided by eight. The 
number was found through trial and error of visually testing the ball. To control the direction of 
the ball, at first, the angle needs to be found to calculate the direction of the force vector. As 
shown in Figure 3, two points in a grid produce a right-angle triangle. The findAngle() function is 
used to calculate the angle from the x-axis to the position of the mouse. This angle is used to 
formulate how the ball would move when there is gravity involved.

## Projectile Motion Calculations

Ball physics mainly used in this game is a simulation of how a real-life ball would travel 
across a certain distance when gravity is involved. Air resistance is not ignored. The ballPath() 
function takes in the X and Y coordinates of the ball, the distance of the line, the angle, and a 
variable “time” to calculate the position of the ball at certain points in time. Both X and Y
vectors of velocity are calculated using the cosine of the angle and multiplying it by the length of 
the line. To find the distance the ball should move, the velocity components are multiplied by a
chosen time. The new position at the end is found by adding the distance from the start position 
of both components. This function is called continuously during the game_is_on state and 
disappears when it crosses the border or when it touches the rim. Figure 4 is a representation of 
the coordinate system used and the position of the ball at certain points in time.
When the player and enemies collide, an explosion effect occurs. This occurs also when
the ball touches the rim. This effect was created using the Sprite library and five images that
show three snapshots of an explosion. I created a class called “Explosion” that inherits from the 
sprite class to produce the animation. When the class object is called during the collision, it 
iterates through each of the images and draws the effect at each frame of the game. Thus, the 
animation speed is dependent completely on the frame the game is running on.

![ProjectileMotion](https://github.com/Raiyan2000/LED-Checkers-App-with-Voice-Recognition/assets/77954118/93e5596e-29f0-47b8-b0b3-fcf9b821ef17)
# Quick Start
Clone the repository:
```
git clone https://github.com/Raiyan2000/ece1145--NuclearWarElephants-YRJ-.git
```
Install Pygame if not already (remember to use your version of Python):
```
pip install pygame
```
Navigate to the root directory:
```
Basketball-Showdown-Hoops-and-Hazards
```
Run this file:
```
main.py
```


