import pygame
import random
from tkinter import *

pygame.init()

width = 1040
height = 650

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("PING -PONG")

# color for the line:
white=(255,255,255)

# for the paddle
green = (124,252,0)
orange_colour = (255, 165, 0)
orange = ((255,128,0))
sea_green = (84,255,159)

dash_color = random.choice([orange_colour,sea_green,green,orange])

red=(255,0,0)
med_purple = (147,112,219)
peacock = ((0,128,128))

ball_color = random.choice([red,med_purple,peacock])

dark_violet = (76, 0, 153)
blue = (0,191,255)

score_color = random.choice([dark_violet,blue])

bg_color_1 = pygame.Color('#2F373F')
bg_color = random.choice([bg_color_1])

# for the shapes:
# 1.dash
width_dash = 5
height_dash = 140
pos_x = 0 + 10
speed_dash = 50
pos_y = height//2

# 2.ball
ball_x_speed = 10
ball_y_speed = 10


dash_player = pygame.Rect(pos_x,pos_y,20,height_dash)
dash_opponent = pygame.Rect (width - 30, pos_y, 20, height_dash)

score_player = 0
player_speed = 0

score_opponent = 0
opponent_speed = 12

player = ''
opponent = ''

ball_x = random.choice([width//2,width//2+1,width//2+2])
ball_y = random.choice([height//2,height//2+1,height//2+2])
ball = pygame.Rect(ball_x,ball_y - 50,30,30)

score_time = True
target_points = 0


# class initializer:

def ball_animation():

    global ball_x_speed,ball_y_speed,score_player,score_opponent,score_time

    ball.x += ball_x_speed
    ball.y += ball_y_speed

    if ball.top <= 0 or ball.bottom >= height:
        ball_y_speed *= -1

    if ball.left <= 0:
        score_opponent += 1
        pygame.mixer.music.load('score.ogg')
        pygame.mixer.music.play()
        print(f'{opponent}',score_opponent)
        score_time = pygame.time.get_ticks()

    if ball.right >= width:
        score_player += 1
        pygame.mixer.music.load('score.ogg')
        pygame.mixer.music.play()
        print(f'{player}',score_player)
        score_time = pygame.time.get_ticks()

    if ball.colliderect (dash_player) and ball_x_speed < 0 :
        pygame.mixer.music.stop()
        pygame.mixer.music.load('pong.ogg')
        pygame.mixer.music.play()
        ball_x_speed *= -1

    if ball.colliderect (dash_opponent) and ball_x_speed > 0 :
        pygame.mixer.music.stop()
        pygame.mixer.music.load('pong.ogg')
        pygame.mixer.music.play()

        ball_x_speed *= -1

def ball_start_pos():
    global ball_x_speed,ball_y_speed,score_time

    current_time = pygame.time.get_ticks()
    ball.center = width//2,height//2

    if current_time - score_time < 2100:
        ball_x_speed = 0
        ball_y_speed = 0
    else:
        ball_x_speed = 10 * random.choice([1,-1])
        ball_y_speed = 10 * random.choice([1,-1])
        score_time = None

font = pygame.font.SysFont('timesnewroman',300,bold = True)
font_target = pygame.font.SysFont('timesnewroman',30,bold = True)
fonT_winner = pygame.font.SysFont('timesnewroman',150,bold=True)

def text_maker(text,colour,x,y):
    text = font.render(text,False,colour)
    window.blit(text,(x,y))

def target_maker(text,colour,x,y):
    text = font_target.render(text,False,colour)
    window.blit(text,(x,y))

def winner_maker(text,colour,x,y):
    text = fonT_winner.render(text,False,colour)
    window.blit(text,(x,y))

def blitter():
    pygame.draw.rect(window,dash_color,dash_player)
    pygame.draw.rect(window,dash_color,dash_opponent)
    pygame.draw.ellipse(window,ball_color,ball)

def opponent_ai():
    if dash_opponent.top < ball.y:
        dash_opponent.top += opponent_speed
    if dash_player.top <= 0:
        dash_player.top = 0
    if dash_player.bottom >= height:
        dash_player.bottom = height
    if dash_opponent.bottom     > ball.y:
        dash_opponent.bottom -= opponent_speed

def player_move():
    dash_player.y += player_speed

    if dash_player.top <= 0:
        dash_player.top = 0
    if dash_player.bottom >= height:
        dash_player.bottom = height


def winner():

    global target_points,ball_x_speed,ball_y_speed,player_speed,opponent_speed

    if score_player == target_points and not(score_opponent == target_points - 1):
        winner_maker(f"{player} Won!", orange, width // 2 - 400, height // 2)
        ball_x_speed,ball_y_speed = 0,0
        player_speed = 0
        opponent_speed = 0


    elif score_opponent == target_points and not(score_player == target_points - 1):
        winner_maker(f"{opponent} Won!",orange, width//2 - 520,height//2)
        ball_x_speed,ball_y_speed = 0,0
        opponent_speed = 0
        player_speed = 0

    elif score_opponent == target_points and score_player == target_points - 1:
        target_points += 1

    elif score_player == target_points and score_opponent == target_points - 1:
        target_points += 1

def Ping_Pong_main():

    # global variables:
    global ball_x_speed,ball_y_speed,score_opponent,score_player,player_speed,opponent_speed

    # game variables:
    game_on = True
    FPS = 60
    ping_clock = pygame.time.Clock()

    while game_on:

        window.fill(bg_color)
        pygame.draw.line(window,white,(width//2,0),(width//2 , height),3)

        text_maker(f'{score_player}',score_color,width // 2 - 300,100)
        text_maker(f'{score_opponent}',score_color,width//2 + 100,100)
        target_maker(f'Target Points:{target_points}',white,width//2 - 100,20)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                game_on = False

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_w:
                    player_speed += -10

                if events.key == pygame.K_s:
                    player_speed += 10


            if events.type == pygame.KEYUP:
                if events.key == pygame.K_w:
                    player_speed += 10
                if events.key == pygame.K_s:
                    player_speed += -10


        player_move()
        opponent_ai()
        ball_animation()
        winner()

        if score_time:
            ball_start_pos()

        blitter()

        pygame.display.update()
        ping_clock.tick(FPS)

def Tkinter_window():

    global target_points,player,opponent

    screen = Tk()
    width = 400
    height = 300
    screen.geometry(    f'{width}x{height}')
    screen.configure(background = 'green')
    screen.title('Target points')

    def set_target():
        global target_points,player,opponent

        target_points = int(target_entry.get())
        player = player_entry.get()
        opponent = opponent_entry.get()

        try:

            if target_points > 0 and player != ('Enter Player Name') and opponent != ('Enter Opponent Name') :
                print ('Target Points:',target_points)
                screen.destroy()
                Ping_Pong_main()

            else:
                print ('No such target point available to play!')

        except EXCEPTION as e:
            print (e)
            print ("AN ERROR OCCURED!")

    player_entry = Entry(font = 'lucida 10 bold')
    player_entry.place(x =    120, y = 50,width = 170,height = 30)
    player_entry.insert(0,'Enter Player Name')

    opponent_entry = Entry(font = 'lucida 10 bold')
    opponent_entry.place(x = 120, y = 100,width = 170 ,height = 30)
    opponent_entry.insert(0,'Enter Opponent Name')


    target_entry = Entry(font = 'timesnewroman 10 bold')
    target_entry.place(x =   120,y = 150,width = 170,height = 30)
    target_entry.insert(0,'Enter Target Points.')

    Target_taker = Button(text = 'Set Target And Name',font = 'lucida 10 bold',background ='orange',command = set_target)
    Target_taker.place(x =   120 ,y = 200,width = 150,height = 40)

    screen.mainloop()
def welcome():
    while True:
        window.fill(bg_color_1)
        pygame.draw.line(window,white,(width//2,0),(width//2,height),2)
        target_maker('Press Enter to play!',orange,400,height//2)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    Tkinter_window()

        pygame.display.update()

welcome()


exit()



