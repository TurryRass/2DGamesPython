
import pygame
import random

pygame.init()

width = 300
height =450

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('race-em-all')


def main():

    game_on = True

    background_list = random.choice (['back_ground.jpg', 'back_ground0.jpg'])
    background = pygame.transform.scale (pygame.image.load (background_list).convert_alpha (), (width, height))
    back_road = 0
    back_road_1 = -600

    my_car = pygame.image.load ('car.png')
    my_car_x = width / 2
    my_car_y = height - my_car.get_height ()

    # for enemy car in the game:
    enemy_car_list = random.choice (['enemy_car_1.png', 'enemy_car_2.png'])
    enemy_car = pygame.transform.flip (pygame.image.load (enemy_car_list).convert_alpha (), False, True)

    enemy_car_range_x = random.randrange (0 + my_car.get_width (),width - (my_car.get_width () + my_car.get_width ()))
    enemy_car_range_y = random.randrange (-600, height)
    enemy_car_x = enemy_car_range_x
    enemy_car_y = enemy_car_range_y

    FPS = 60
    game_clock = pygame.time.Clock ()

    FONT = pygame.font.SysFont('lucida',20,bold=True)
    score = 0

    while game_on:

        score_text = FONT.render(f'Score:{score}',1,(255,255,255),(0,0,0))

        screen.fill ((255, 255, 255))
        screen.blit (background, (0, back_road))
        screen.blit (background, (0, back_road_1))
        screen.blit (my_car, (my_car_x, my_car_y))
        screen.blit (enemy_car, (enemy_car_x, enemy_car_y))
        screen.blit(score_text,(width/2 - score_text.get_width()/2,30))

        if score > 100:
            enemy_car_y += 1
        if score > 500:
            enemy_car_y += 2
        if score > 1000:
            enemy_car_y += 3

        # to move the enemy car in the y cordinate:
        enemy_car_y += random.randrange (3, 5)

        if enemy_car_y >= height:
            enemy_car_list = random.choice (['enemy_car_1.png', 'enemy_car_2.png'])
            enemy_car = pygame.transform.flip (pygame.image.load (enemy_car_list).convert_alpha (), False, True)

            enemy_car_y = 0 - enemy_car.get_height ()
            enemy_car_x = random.randrange (0 + my_car.get_width (), width - (my_car.get_width () + my_car.get_width ()))

            score += 1 * 50

        for events in pygame.event.get ():
            if events.type == pygame.QUIT:
                game_on = False
                pygame.quit ()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_a:
                    my_car_x += -20
                if events.key == pygame.K_d:
                    my_car_x += 20

        if my_car_y <= enemy_car_y + enemy_car.get_height ():
            if my_car_x > enemy_car_x and my_car_x < enemy_car_x + 49 or my_car_x + 49 > enemy_car_x and my_car_x + 49 < enemy_car_x + 49:
                game_on = False

        if my_car_x > width - (my_car.get_width () + my_car.get_width ()) + 10:
            game_on = False
        if my_car_x < 0 + my_car.get_width ():
            game_on = False

        if game_on == False:
            game_over ()

        pygame.display.update ()
        game_clock.tick (FPS)


if __name__ == '__main__':
    def game_over():
        game_over = True

        # font:
        font = pygame.font.SysFont('timesnewroman',40,bold=True)
        # clock
        clock = pygame.time.Clock()

        restart = font.render ('Restart', 1, (0, 255, 0))
        exit = font.render ('Exit', 1, (255, 0, 0))

        while game_over:

            screen.fill ((255,0,0))

            screen.blit(restart,(width//2 - restart.get_width()//2,height//2))

            for events in pygame.event.get():

                if events.type == pygame.QUIT:
                    pygame.quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos() >= (width//2 - restart.get_width()//2,height//2):
                        if pygame.mouse.get_pos() <= (width//2 + restart.get_width()//2 ,height//2 + restart.get_height()//2):
                            main()

            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    main()

exit()
