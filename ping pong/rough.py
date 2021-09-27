import pygame, sys


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect (player) or ball.colliderect (opponent):
        ball_speed_x *= -1


# General setup
pygame.init ()
clock = pygame.time.Clock ()

# Main Window
screen_width = 680
screen_height = 760
screen = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption ('Pong')

# Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
dark_violet = (76, 0, 153)
orange_colour = (255, 165, 0)
light_grey = (200, 200, 200)
bg_color = pygame.Color ('grey12')
Y_pos_player1 = 200
# Game Rectangles
pygame.draw.rect (screen,light_grey, [0, Y_pos_player1, 9, 60])
pygame.draw.rect (screen,orange_colour , [590, Y_pos_player1, 10, 60])
opponent = pygame.Rect (10, screen_height / 2 - 70, 10, 140)

# Game Variables
ball_speed_x = 7
ball_speed_y = 7

while True:
    for events in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                Y_pos_player1 -= 70
            if events.key == pygame.K_s:
                Y_pos_player1 += 70
            if events.key == pygame.K_p and not playing:
                ball.move_with ()
                playing = True



    # Game logic
    ball_animation ()

    screen.fill (bg_color)
    pygame.draw.rect (screen, light_grey, player)
    pygame.draw.rect (screen, light_grey, opponent)
    pygame.draw.ellipse (screen, light_grey, ball)
    pygame.draw.aaline (screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.flip ()
    clock.tick (60)