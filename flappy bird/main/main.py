

# This is the code for the game fly bird by us that is Taico Limited:

import pygame
import sys
import pyttsx3
import time
import random
import os
from pygame.locals import *

pygame.mixer.init() # initialises the mixer needed in the game.

# for the speak function in the game which will give a better taste to the customers :
def speak(say):

    engine=pyttsx3.init()
    engine.say(say)
    engine.runAndWait()

#speak("LOADING GAME!\n")

#speak("loading successful\nwelcome to Taico bird")

time.sleep(1)

# for the main game window and global variables :

FPS = 60 # this is the frames which will be shown to the customer per second to give him a more smoother game_view.

game_width = 500 # width of the whole game.
game_height = 511 # height of the whole game.

game_window=pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption("Taico-Bird.")
ground= game_height * 0.8  # gives the ground required for the game .


# for the different sprites or images or animations that has been used in the game

# Game Sprites or images:

background_list={} # this is the list from where the background will come from.


# numbers used in the game for score:

game_scores_numbers={} # for differnt scores that has been used in the game.

game_scores_numbers["numbers"]=(
pygame.image.load("gallery/sprites/0.png").convert_alpha(),
pygame.image.load("gallery/sprites/1.png").convert_alpha(),
pygame.image.load("gallery/sprites/2.png").convert_alpha(),
pygame.image.load("gallery/sprites/3.png").convert_alpha(),
pygame.image.load("gallery/sprites/4.png").convert_alpha(),
pygame.image.load("gallery/sprites/5.png").convert_alpha(),
pygame.image.load("gallery/sprites/6.png").convert_alpha(),
pygame.image.load("gallery/sprites/7.png").convert_alpha(),
pygame.image.load("gallery/sprites/8.png").convert_alpha(),
pygame.image.load("gallery/sprites/9.png").convert_alpha()
)


# game sound :

# for the different sounds which are played at different parts of the games:

game_sound={}  # sounds which are played for the game

game_sound["die"]= pygame.mixer.Sound("gallery/audio/die.wav")  # when the bird dies
game_sound["hit"]= pygame.mixer.Sound("gallery/audio/hit.wav")   # when bird hits the pipe
game_sound["point"]= pygame.mixer.Sound("gallery/audio/point.wav")  # when crosses a pipe successfully
game_sound["swoosh"]= pygame.mixer.Sound("gallery/audio/swoosh.wav")   # for the swoosh sound in game that is
game_sound["wing"]= pygame.mixer.Sound("gallery/audio/wing.wav")    # for the sound which comes up when the wings of the birds are flapped
game_sound["welcome_sound"]= pygame.mixer.Sound("Warriors (ft. Imagine Dragons) _ Worlds 2014 - League of Legends (320  kbps).mp3")
# the sound played when user comes into the game or simply the theme song ,also will be used after game is over

if __name__ == '__main__':

    pygame.init() # this finction just initializes all the function in the game from here or allow the module functions
                  # to be runned from here.


    # for the clock in the game to control the fps

    game_clock=pygame.time.Clock()

    def main():

        global score,level,font,finsih_text

        # all things:

        # for the background of the game.
        bg1 = 'background.png'
        bg2 = 'bg_night.png'
        bg_list = random.choice ([bg1, bg2])
        background_wallpaper = bg_list

        background_list["background"] = pygame.transform.scale (
            pygame.image.load (f"gallery/sprites/{background_wallpaper}"), (game_width, 511))
        background_list["game_over"] = pygame.image.load ("gallery/sprites/game over.png")  # for the game window

        # for random background:
        # background_for_game=random.choice("")

        # to be continued for inserting in the background list.

        # pipes in the game:
        red_pipe = 'pipe-red.png'
        green_pipe = 'pipe.png'
        list_of_pipe = random.choice ([red_pipe, green_pipe])
        pipe = list_of_pipe

        if pipe == red_pipe:
            background_list["base"] = pygame.transform.scale (pygame.image.load ("gallery/sprites/red_base.png"), (
                500, 112))  # for the base for which ground variable has been designed

        else:

            background_list["base"] = pygame.transform.scale (pygame.image.load ("gallery/sprites/green_base.png"), (
                500, 112))  # for the base for which ground variable has been designed

        background_list["pipe"] = (
            pygame.transform.rotate (pygame.image.load (f"gallery/sprites/{pipe}").convert_alpha (), 180),
            pygame.image.load (f"gallery/sprites/{pipe}").convert_alpha ()  # for rotating the pipe in the game
        )  # for the pipes shown in the game

        # for the different birds in th game:

        bird_1 = pygame.image.load ("gallery/sprites/red_bird.png").convert_alpha ()
        bird_2 = pygame.transform.scale (pygame.image.load ("gallery/sprites/yellow_bird.png").convert_alpha (),
                                         (34, 24))
        bird_3 = pygame.transform.scale (pygame.image.load ("gallery/sprites/blue_bird.png").convert_alpha (), (34, 24))

        list_of_birds = random.choice ([bird_1, bird_2, bird_3])
        bird = list_of_birds

        background_list["bird"] = bird  # for the flying bird in the game



        # random pipe function:
        def random_pipe():

            '''Generate positions for two pipes(one bottom staright and one top rotated)
            for blitting on the screen'''
            pip_height = background_list['pipe'][0].get_height()
            # offset is how much should be the distance of my lower pipe from above
            # x of the width of the screen:

            offset = game_width/3

            # generate lower pipe y at the position gven below between offset(at least that much distance is
            # mandatory and along with it add the random number generated.
            # and it will add the offset to both the range we got like 10 offset added with
            # 10 and will become 10 + offset .
            # the follwing is kind of obvious so just if unable to understand then go and watch videos of
            # code with harry flappy bird.
            # i have added - 1.2 * offset so that some pipes can be very small too and not only in a single
            # range just what can yu understand is that i have just given a greater range to the
            # pipe position by doing this.
            y2 = offset + random.randrange(0, int(game_height - background_list['base'].get_height() - 1.2 * offset))
            pipe_x = game_width + 10


            # now for the upper pipe on the screen:
            # this follwing concept is extremely easy you believe me and you will be able to understand it
            # easily because i have had understood it.
            # height of the upper pipe from the screen should be
            # the +offset is done because there will be a large gap between both pipes if its no done:
            y1 = pip_height - y2 + offset
            pipes = [{'x':pipe_x , 'y':-y1}, # for upper pipes
                     {'x':pipe_x,  'y':y2}]  # for the lower pipes
            return pipes  # now i can use it in my game with variables.

        score = 0
        player_x = int(game_width/4)
        player_y = int(game_height/2)
        base_x = 0

        # create two pipes for blitting on the screen:

        # it contains a list as i am returning pipes in this function which is
        # a list and you can also see this
        # and remember return in func means that a variable intialised with it
        # will have return as the content ,here it is: pipes.

        new_pipe1 = random_pipe()
        new_pipe2 = random_pipe()

        # my list of upper pipes:
        upper_pipes = [{'x':game_width + 200,'y':new_pipe1[0]['y']}, # this means that i want first pip at 200 pixels BEYOND SCREEEN  and y is what i want.
                       {'x':game_width + 200 + game_width/2,'y':new_pipe2[0]['y']}] # for long upper pipes y is chnaged.

        # my list of lower pipes:
        # my list of upper pipes:
        lower_pipes = [{'x':game_width + 200,'y':new_pipe1[1]['y']}, # this means that i want first pip at 200 pixels BEYOND SCREEEN  and y is what i want.
                       {'x':game_width + 200 + game_width/2,'y':new_pipe2[1]['y']}]

        # vel at which pipe would move towards the bird
        pipe_vel_x = -4

        # variables for the player or the bird and what can he do when at his best
        player_vel_y = -9   # initial vel of the bird when game starts
        player_max_vel_y = 10 # max vel of the game when the player clicks the up arrow key to stop the bird to fly out into heaven.
        player_min_vel_y = -8 # min vel which would be if the player is falling and will be max initially.
        player_acc_y = 1 # acceleration at which the player will fall towards the ground of taico studio.

        # as a player i would like tochnage the vel of the bird.
        bird_flap_vel =       -8 # velocity of the bird while flapping.
        bird_flapped = False # will giev us true if the bird once starts flapping.

        # game-varaibles:
        game_run = True

        while game_run:

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # the main game how to be controlled has start from here:
                if events.type == pygame.KEYDOWN and (events.key == pygame.K_UP):
                    if player_y > 0:
                        player_vel_y = bird_flap_vel
                        bird_flapped = True
                        game_sound['wing'].play()

            crash_test = iscollide(player_x,player_y,upper_pipes,lower_pipes) # this func will return true if the
                                                                          # player is crashed.

            # if collide becomes true then crash-test becomes true and if crash test true then the loop is false
            # and the game is over and just go to the screen of game_over now.! that is the concept

            if crash_test:
                return game_run == False

            # check for score:
            player_body_midpos = player_x + background_list['bird'].get_width()/2 # and here i get the mid pos of the bird.

            for pipes in upper_pipes:
                pipe_mid_pos = pipes['x'] + background_list['pipe'][0].get_width()/2
                if pipe_mid_pos <= player_body_midpos < pipe_mid_pos + 4: # use your iq and you will understand.
                    score += 1
                    game_sound['point'].play()

            if player_vel_y < player_max_vel_y and not bird_flapped:
                player_vel_y += player_acc_y  # I want to bring the bird down.

            if bird_flapped:
                bird_flapped = False # actually this and the upper part is giving me the falling animation
                # OF THE BIRD AND NOT ALLOWING MY BIRD TO GET OFF THE SCREEN.

            bird_height = background_list['bird'].get_height()
            player_y = player_y + min(player_vel_y,ground - player_y - bird_height)

            # move pipes to the left:
            for upper_pipe,lower_pipe in zip(upper_pipes,lower_pipes):
                upper_pipe['x'] += pipe_vel_x  # if a negative no is added then it will get small and not big
                lower_pipe['x'] += pipe_vel_x

            # add a new pipe when the first pipe is about to go out of the screen:
            if 0 < upper_pipes[0]['x'] < 5:
                new_pipe = random_pipe()
                upper_pipes.append(new_pipe[0])
                lower_pipes.append(new_pipe[1])

            # lets blit now all of the above in the screen:
            game_window.blit(background_list['background'],(0,0))
            # move pipes to the left:
            for upper_pipe,lower_pipe in zip(upper_pipes,lower_pipes):
                game_window.blit(background_list['pipe'][0],(upper_pipe['x'],upper_pipe['y']))
                game_window.blit(background_list['pipe'][1],(lower_pipe['x'],lower_pipe['y']))

            # if the pipe is out of th screen while moving left then just remove it:
            if upper_pipes[0]['x'] < -background_list['pipe'][0].get_width():
                upper_pipes.pop(0)
                lower_pipes.pop(0)

            game_window.blit(background_list['base'],(base_x,ground))
            game_window.blit(background_list['bird'],(player_x,player_y))

            my_digits = [int (x) for x in list(str(score))]
            widthi = 0

            for digit in my_digits:
                widthi += game_scores_numbers["numbers"][digit].get_width()

            xoffset = (game_width - widthi)/2

            for digit in my_digits:
                game_window.blit(game_scores_numbers['numbers'][digit],(xoffset,game_height*0.12))
                xoffset += (game_scores_numbers['numbers'][digit].get_width())

            pygame.display.update()
            game_clock.tick(FPS)

    def iscollide(player_x, player_y, upper_pipes, lower_pipes):

        global font,finsih_text

        if player_y > ground - 25 or player_y < 0:
            game_sound['die'].play()
            time.sleep(1)
            game_sound['welcome_sound'].play ()
            game_over_screen()

            return True

        # to check collisions with the upper pipes:
        for pipe in upper_pipes:
            pipe_height = background_list['pipe'][0].get_height()
            if player_y < pipe_height + pipe['y'] and abs(player_x - pipe['x']) < background_list['pipe'][0].get_width():
                game_sound['hit'].play()
                time.sleep (1)
                game_sound['welcome_sound'].play ()
                game_over_screen ()

                return True

        # check collisions with the lower pipes:
        for pipe in lower_pipes:
            if player_y + background_list['bird'].get_height() >  + pipe['y'] and abs(player_x - pipe['x']) < background_list['pipe'][0].get_width():
                game_sound['hit'].play()
                time.sleep (1)
                game_sound['welcome_sound'].play()
                game_over_screen ()

                return True

        return False

if __name__ == '__main__':

    def Welcome_screen():

        game_sound['welcome_sound'].play ()

        screen = pygame.display.set_mode((game_width,game_height))
        game_loop = True

        # game welcome background:
        screen_1 = pygame.transform.scale(pygame.image.load('gallery/sprites/wp3276758.jpg'),(game_width,game_height))
        screen_2 = pygame.transform.scale(pygame.image.load('gallery/sprites/wp3276788.jpg'),(game_width,game_height))

        welcome_screen_list = random.choice([screen_1,screen_2])
        clock = pygame.time.Clock()

        # main welocme screen loop:
        while game_loop:

            # for text on welcome screen:
            # for font:
            font = pygame.font.SysFont('lucida',60,bold = True)
            font_tut = pygame.font.SysFont('timesnewroman',30,bold = True)
            # setup of what to be shown on the welcome screen:
            game_name = font.render('         Taico-Bird        ',1,(255,255,255),(255,0,0))
            game_tut = font_tut.render('Tap Mouse',1,(0,255,0))

            # blitting thingson the screen:
            screen.blit (welcome_screen_list, (0,game_name.get_height()))
            screen.blit(game_name,(game_width/2 - game_name.get_width()/2,0))
            screen.blit(game_tut,(game_width - game_tut.get_width(),game_height - game_tut.get_height()))

            for evenets in pygame.event.get():
                if evenets.type == pygame.QUIT:
                    pygame.quit()
                    game_loop = False
                    sys.exit()
                if evenets.type == pygame.MOUSEBUTTONUP:
                    game_sound['welcome_sound'].stop()
                    main()

            pygame.display.update()
            clock.tick(FPS)


if __name__ == '__main__':

    def game_over_screen():

        global score,highscore,level

        # game_over variables:
        game_decide = True

        # screen:
        screen = pygame.display.set_mode((game_width,game_height))
        pygame.display.set_caption(f'TAICO - BIRD')

        # images:
        game_over_wallpaper = pygame.transform.scale(pygame.image.load('gallery/sprites/game over.png'),(game_width,game_height))

        # for the score and highscore saving:

        if not (os.path.exists ('highscore.txt')):
            with open ('highscore.txt', 'w') as f:
                f.write (str (score))

        with open ('highscore.txt', 'r') as f:
            high_score = f.read ()

        if score > int(high_score):
            high_score = score

        if (os.path.exists ('highscore.txt')):
            with open ('highscore.txt', 'w') as f:
                f.write (str (high_score))


        # for text on welcome screen:

        # for font:
        font = pygame.font.SysFont ('lucida', 40, bold=True)
        font_score = pygame.font.SysFont ('timesnewroman', 20, bold=True)
        font_from = pygame.font.SysFont('times',30,bold = True)


        # setup of what to be shown on the welcome screen:
        game_score = font.render (f'     Score:{score}                HighScore:{int(high_score)}   ', 1, (255, 255, 255), (255, 0, 0))
        game_tut = font_score.render ('  Press Enter To play Again!', 1, (0, 255, 0),(0,0,0))
        game_from = font_from.render('BY - TAICO LIMITED  ',1,(0,0,0),(0,255,0))

        # game clock:
        clock = pygame.time.Clock()

        while game_decide:

            # blitting things on the screen:
            screen.blit (game_over_wallpaper, (0,0))
            screen.blit (game_score, (game_width / 2 - game_score.get_width () / 2 - 10, 0))
            screen.blit (game_tut, (game_width/2 - game_score.get_width()/2 + 100 + 50,game_score.get_height ()))
            screen.blit (game_from, (game_width/2 - game_score.get_width()/2 + 100 + 20, game_height - game_score.get_height ()))

            for evenets in pygame.event.get ():
                if evenets.type == pygame.QUIT:
                    pygame.quit ()
                    game_decide = False
                    sys.exit ()
                if evenets.type == pygame.KEYDOWN:
                    if evenets.key == pygame.K_RETURN:
                        game_sound['welcome_sound'].stop()
                        Welcome_screen ()

            pygame.display.update ()
            clock.tick (FPS)

if __name__ == '__main__':
    Welcome_screen()