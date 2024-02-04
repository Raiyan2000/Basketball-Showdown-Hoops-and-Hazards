import math
import random

import pygame
from pygame import mixer

from explosion import *
from game import Game

# Player
playerImg = pygame.image.load("./Graphics/basketball-player_50.png")
playerX = 480
playerY = 480
playerX_change = 0
playerY_change = 0

# Rim
b_rim = pygame.image.load("./Graphics/basketball.png")
rimX = 200
rimY = 200

# ball
basketball_ball = pygame.image.load("./Graphics/003-basketball-ball.png")
basketballX = 400
basketballY = 200
basketballX_change = 1
basketballY_change = -2
ballState = "ready"

# plane enemy
plane = pygame.image.load("./Graphics/airplane.png")
planeX = 0
planeY = 0
planeX_change = -2
planeState = "ready"

# nuke enemy
nuke = pygame.image.load("./Graphics/nuke_64.png")
nukeX = 800
nukeY = 0
nukeY_change = 2
nukeState = "ready"

# ball Physics
angle = 0
time = 0
power = 0
x = 0
y = 0


def showScore(x, y):
    score_value = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def rim(x, y):
    screen.blit(b_rim, (x, y))


def basketball(x, y):
    screen.blit(basketball_ball, (x, y))


def isCollision(rim_xcor, rim_ycor, ball_xcor, ball_ycor):
    distance = math.sqrt((math.pow(rim_xcor - ball_xcor, 2)) + (math.pow(rim_ycor - ball_ycor, 2)))
    if distance < 27:
        return True
    else:
        return False


def shoot(x, y):
    global ballState
    ballState = "fire"
    screen.blit(basketball_ball, (x + 0, y + 0))  # 16


def gameOverText():
    over_text = over_font.render("Game Over!", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))

def gameWinnerText():
    over_text = over_font.render("Game Winner!", True, (0, 0, 255))
    screen.blit(over_text, (200, 250))


def findAngle(pos):
    sX = basketballX
    sY = basketballY
    try:
        angle1 = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle1 = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle1 = abs(angle1)
    elif pos[1] < sY and pos[0] < sX:
        angle1 = math.pi - angle1
    elif pos[1] > sY and pos[0] < sX:
        angle1 = math.pi + abs(angle1)
    elif pos[1] > sY and pos[0] > sX:
        angle1 = (math.pi * 2) - angle1

    return angle1


def ballPath(startx, starty, power, ang, time):
    angles = ang
    velx = math.cos(angles) * power
    vely = math.sin(angles) * power

    distX = velx * time
    distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

    newx = round(distX + startx)
    newy = round(starty - distY)

    return (newx, newy)


explosion_group = pygame.sprite.Group()
g = Game()
choice = True
while(choice):
    g.curr_menu.display_menu()
    if(g.curr_menu.get_gamePlaying() == False):
        choice = False


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
fps = 60

# Game background Image
background = pygame.image.load("./Graphics/final_court.jpg")

# Game running: background sound
mixer.music.load("./Graphics/background.wav")
mixer.music.play(-1)

# Game window configuration
pygame.display.set_caption("Score to 15!")
icon = pygame.image.load("./Graphics/spaceship.png")
pygame.display.set_icon(icon)

# User interface
score = 0
gameover = False
font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)
textX = 10
textY = 10

game_is_on = True

# Start of Game Loop
while game_is_on:
    clock.tick(fps)
    screen.fill((173, 216, 230))
    screen.blit(background, (0, 0))
    explosion_group.draw(screen)
    explosion_group.update()
    # load_map()
    pos = pygame.mouse.get_pos()
    line = [(playerX, playerY), pos]
    pygame.draw.line(screen, (255, 255, 255), line[0], line[1])

    # For game running all the time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Ball shot when mouse pressed down
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ballState == "ready":
                ballState == "fire"
                ball_sound = mixer.Sound("./Graphics/shootBall.wav")
                ball_sound.play()
                basketballX = playerX
                basketballY = playerY
                x = playerX
                y = playerY
                time = 0

                # power generated from the length of shooting line
                power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][1]) ** 2) / 7.5

                # Angle found from  shooting line and x axis
                angle = findAngle(pos)

                # Shoot
                shoot(basketballX, basketballY)

        # movement with keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_UP:
                playerY_change = -10
            if event.key == pygame.K_DOWN:
                playerY_change = 10
            if event.key == pygame.K_SPACE:
                if ballState == "ready":
                    ball_sound = mixer.Sound(".Graphics/shootBall.wav")
                    ball_sound.play()
                    basketballX = playerX
                    basketballY = playerY
                    x = playerX
                    y = playerY
                    shoot(basketballX, basketballY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # Boundaries for player
    if playerX < 0:
        playerX = 0
    elif playerX > 720:
        playerX = 720
    if playerY > 530:
        playerY = 530
    elif playerY < 300:
        playerY = 300

    # Ball boundaries
    if basketballX > 720:
        basketballX = playerX
        basketballY = playerY
        ballState = "ready"
    if basketballX < 0:
        basketballX = playerX
        basketballY = playerY
        ballState = "ready"
    elif basketballY > 600:
        basketballY = playerY
        basketballX = playerX
        ballState = "ready"
    elif basketballY < 0:
        basketballY = playerY
        basketballX = playerX
        ballState = "ready"

    # Ball Movement
    if ballState == "fire":
        time += 0.35
        po = ballPath(x, y, power, angle, time)
        basketballX = po[0]
        basketballY = po[1]
        shoot(basketballX, basketballY)
    else:
        time = 0

    # collision of ball and rim
    collision_ball_rim = isCollision(rimX, rimY, basketballX, basketballY)
    if collision_ball_rim:
        net_sound = mixer.Sound("Graphics/net_ball.wav")
        net_sound.play()
        explosion = Explosion(rimX, rimY)
        explosion_group.add(explosion)
        basketballY = playerY
        basketballX = playerX
        ballState = "ready"
        score += 1
        rimX = random.randint(200, 700)
        rimY = random.randint(10, 400)
        print(score)

    # Game Winner
    if score > 14:
        gameWinnerText()
        mixer.music.stop()
        end_sound = mixer.Sound("Graphics/basketball-buzzer.wav")
        end_sound.play()
        rimX = 5000
        rimY = 500
        rim(rimX, rimY)
        planeState = "fire"
        nukeState = "fire"

    # plane boundary
    if score > 5 and planeState == "ready":
        planeX = 720
        planeY = random.randint(300, 530)
        plane_sound = mixer.Sound("Graphics/airplane-fly-over-01.wav")
        plane_sound.play()
        screen.blit(plane, (planeX, planeY))
        planeState = "fire"
    planeX += planeX_change
    screen.blit(plane, (planeX, planeY))

    # plane collision
    if planeX < 0:
        planeState = "ready"

    # nuke boundary
    if score > 10 and nukeState == "ready":
        nukeX = random.randint(300, 530)
        nukeY = 0
        nuke_sound = mixer.Sound("Graphics/falling.wav")
        nuke_sound.play()
        screen.blit(nuke, (nukeX, nukeY))
        nukeState = "fire"
    nukeY += nukeY_change
    screen.blit(nuke, (nukeX, nukeY))

    # Game Over: Collision with
    if nukeY > 550 and nukeState == "fire":
        explosion = Explosion(nukeX, nukeY)
        explosion_group.add(explosion)
        nuke2_sound = mixer.Sound("Graphics/Arcade Explo A.wav")
        nuke2_sound.play()
        nukeState = "ready"

    # Game Over: Collision of plane
    collision_plane_player = isCollision(planeX, planeY, playerX, playerY)

    # Game Over: Collision of bomb
    collision_bomb_player = isCollision(nukeX, nukeY, playerX, playerY)
    if collision_plane_player or collision_bomb_player:
        gameover = True

    # Gameover by collision
    if gameover == True:
        gameOverText()
        mixer.music.stop()
        end_sound = mixer.Sound("Graphics/basketball-buzzer.wav")
        end_sound.play()
        rimX = 5000
        rimY = 500
        rim(rimX, rimY)
        planeState = "fire"
        nukeState = "fire"
        nukeY = -10000000

    rim(rimX, rimY)
    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
