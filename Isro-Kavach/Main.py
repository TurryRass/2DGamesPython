# Imported Modules
import pygame
from random import choice,randint
from sys import exit as EXIT

# Pygame Initialization
pygame.init()

# Class For InGame Player - SpaceShip
class SpaceShip(pygame.sprite.Sprite):
    global Health
    def __init__(self):
        super().__init__()
        self.x = 500
        self.image = pygame.image.load('Objects/pixel_ship_yellow.png')
        self.y = 600 - self.image.get_height() - 25
        self.speed_x = 10
        self.rect = self.image.get_rect(midtop = (self.x,self.y))
        self.cooldownA = 0
        self.cooldownM = 0

    def movement(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_a]:
            self.rect.x -= self.speed_x
        elif self.keys[pygame.K_d]:
            self.rect.x += self.speed_x

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= 1000:
             self.rect.right = 1000

    def EarthHealth(self):
        pygame.draw.rect(Screen,'red',(self.rect.x,self.rect.bottom,100,10))
        pygame.draw.rect(Screen,'green',(self.rect.x,self.rect.bottom,Health,10))

    def shoot(self):
        # For Arrows
        if self.keys[pygame.K_s]:
            if self.cooldownA == 0:
                self.cooldownA = 20
                Arrow.add (Arrows (self.rect.x, self.y))
        if self.keys[pygame.K_UP]:
            if self.cooldownM == 0:
                self.cooldownM = 1000
                Missile.add (BrahMos (self.rect.x, self.y))

    def update(self):
        self.movement()
        self.shoot()
        Arrow.update ()
        Missile.update()
        # If Statement Check Player's Firing Action
        if self.cooldownA > 0:
            self.cooldownA -= 1
        if self.cooldownM > 0:
            self.cooldownM -= 1
        self.EarthHealth()

# Class For Arrows
class Arrows(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = (pygame.image.load('Objects/Arrow.png'))
        self.rect = self.image.get_rect(midtop = (x + 51,y - self.image.get_height() + 15))

    def update(self):
        self.rect.y -= 5

# Class For BrahMos Missile
class BrahMos(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = ['Objects/BrahMosBlue.png',
                       'Objects/BrahMosGreen.png',
                       'Objects/BrahMosOrange.png'
                       ]
        self.MissileImage = choice(self.images)
        self.image = pygame.transform.scale(pygame.image.load(self.MissileImage),(31,140))
        self.rect = self.image.get_rect(midtop = (x + 48,y - self.image.get_height() + 15))

    def update(self):
        self.rect.y -= 15

# Class for EnemyObjects in Space
class SpaceObject(pygame.sprite.Sprite):
    global Score,Screen
    def __init__(self):
        super().__init__()
        self.x = randint(100,1000 - 120)
        self.y = randint(-1200,-100)
        self.ObjectList = [
            'Objects/A2.png',
            'Objects/A2.png',
            'Objects/A2.png',
            'Objects/A2.png',
            'Objects/A3.jpg',
            'Objects/A3.jpg',
            'Objects/A3.jpg',
            'Objects/A3.jpg',
            'Objects/BlackHole.png',
            'Objects/BlackHole1.jpg'
        ]
        self.choice = choice(self.ObjectList)
        self.image = pygame.image.load(self.choice)
        self.rect = self.image.get_rect(midtop = (self.x,self.y))
        self.health = 100

    def move(self):
        self.rect.y += 3

    def update(self):
        global Score,EnemyHealth

        self.move()
        pygame.draw.rect (Screen, 'red', (self.rect.x + 5, self.rect.y - 10, 100, 10))
        pygame.draw.rect (Screen, 'green', (self.rect.x + 5, self.rect.y - 10, self.health, 10))
        for arrow in Arrow:
            if self.rect.colliderect (arrow) and arrow.rect.bottom > 0:

                if self.choice != 'Objects/BlackHole.png' or 'Objects/BlackHole1.jpg':
                    self.health -= 20
                    Score += 15
                if self.choice == 'Objects/BlackHole.png' or 'Objects/BlackHole1.jpg' :
                    self.health -= 5
                    Score += 10
                if self.health == 0:
                    self.kill ()
                    Explode = Explosions (self.rect.centerx, self.rect.centery, 2)
                    Explosion.add (Explode)
                Arrow.remove (arrow)
                pygame.mixer.music.load ('Objects/Explode.wav')
                pygame.mixer.music.play ()

        for misile in Missile:
            if self.rect.colliderect(misile) and misile.rect.bottom > 0:

                if self.choice != 'Objects/BlackHole.png' or \
                        self .choice != 'Objects/BlackHole1.jpg':
                    self.health -= 100
                    Score += 50
                    print(f'EnemyObjectHealth:{self.health}')
                if self.choice == 'Objects/BlackHole.png' or 'Objects/BlackHole1.jpg':
                    self.health -= 80
                    Score += 100
                    print(f'EnemyObjectHealth:{self.health}')

                print('Collision with Misile!')
                if self.health <= 0:
                    self.kill()
                    Explode = Explosions (self.rect.centerx, self.rect.centery, 4)
                    Explosion.add (Explode)
                Missile.remove(misile)
                pygame.mixer.music.load ('Objects/Explode.wav')
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play ()
        EnemyHealth = self.health

# Class for Explosions Screne:
class Explosions(pygame.sprite.Sprite):

    def __init__(self,x,y,scale):
        pygame.sprite.Sprite.__init__(self)

        self.index = 0
        self.img_list = []

        for exp_anim in range(1,6):
            img = pygame.image.load(f"Objects/explosion/exp{exp_anim}.png").convert_alpha()
            img = pygame.transform.scale(img,(img.get_width() * scale , img.get_height() * scale))
            self.img_list.append(img)

        self.image = self.img_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0

    def update(self):
        Explosion_speed = 4
        self.counter += 1
        if self.counter >= Explosion_speed:
            self.counter = 0
            self.index += 1
            if self.index == len(self.img_list):
                self.kill()
            else:
                self.image = self.img_list[self.index]

def TextScreen(text,size,color,x,y):
    font = pygame.font.Font(None,size)
    mytext = font.render(text,True,color)
    Screen.blit(mytext,(x,y))
    return mytext.get_rect(center = (x,y))

def collison_sprite(obj1,obj2,boolean):
    global Health
    if pygame.sprite.spritecollide(obj1,obj2,boolean):
        Explode = Explosions(obj1.rect.x,obj1.rect.y,3)
        for i in obj2:
            obj2.remove(i)
            Explosion.add(Explode)
            pygame.mixer.music.load('Objects/Explode.wav')
            pygame.mixer.music.set_volume (0.7)
            pygame.mixer.music.play()
        Health -= 5
        print(f'Health:{Health}')

# Game Looks Info
ScreenWidth = 1000
ScreenHeight = 600
Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
icon = pygame.image.load('Objects/icon.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption('Isro-Kavach')

# MadeGame Display
EarthHC = pygame.transform.rotozoom(pygame.image.load('Objects/Earth.jpg'),0,0.4)
EarthPos = EarthHC.get_rect(midtop = (200,600 - 10))

# InGame Active Variables
Health = 100
EnemyHealth = 0
Score = 0

# Game Specific Variables
GameActive = True
GameExit = False
GameOver = False
FPS = pygame.time.Clock()

# Variables For Classes
# ObjectsClasses
Arrow = pygame.sprite.Group()
Missile = pygame.sprite.Group()
attack_objects = pygame.sprite.Group()

# AnimationClass
Explosion = pygame.sprite.Group()

# PlayerClass
Player = pygame.sprite.GroupSingle()
Player.add(SpaceShip())

# Timer for loading enemies
EnemyObject = pygame.USEREVENT + 1
pygame.time.set_timer(EnemyObject,7000)

# Main Game Loop
def Main():
    global GameActive,Health
    while not GameActive:
        for events in pygame.event.get ():
            if events.type == pygame.QUIT:
                GameActive = True
            if events.type == EnemyObject:
                attack_objects.add (SpaceObject ())

        collison_sprite (Player.sprite, attack_objects, False)

        # Game Display And Mother Earth
        Screen.fill ('black')
        Screen.blit (EarthHC, EarthPos)

        # To End The Game When Player's Health is 0
        if Health == 0:
            print ('GameOver!')
            for attacker in attack_objects:
                attack_objects.remove(attacker)
            for arrow in Arrow:
                Arrow.remove(arrow)
            for misile in Missile:
                Missile.remove(misile)
            for explode in Explosion:
                Explosion.remove(explode)
            Health = 100
            GameActive = True
            Health = 100

        # for the blitting from classes

        # Weapons
        Arrow.draw (Screen)
        Missile.draw (Screen)

        # Player
        Player.draw (Screen)
        Player.update ()

        # For the enemy
        attack_objects.draw (Screen)
        attack_objects.update ()

        for Object in attack_objects:

            if EarthPos.colliderect (Object):            # pygame.draw.rect (Screen, 'red', (Object.rect.x + 5, Object.rect.y - 10,100,10))
            # pygame.draw.rect (Screen, 'green', (Object.rect.x + 5, Object.rect.y - 10,EnemyHealth,10))
                attack_objects.remove (Object)
                Health -= 5
                print (f'Health:{Health}')
                Explode = Explosions (Object.rect.x + 30, Object.rect.y + 5, 3)
                Explosion.add (Explode)
                pygame.mixer.music.load ('Objects/Explode.wav')
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play ()

        # to remove misiles and arrows if they don't collide:
        for arrow in Arrow:
            if arrow.rect.bottom == 0:
                Arrow.remove (arrow)
                print ('Arrow!')

        for misile in Missile:
            if misile.rect.bottom == 0:
                Missile.remove (misile)
                print ('Misile!')

        # To Display Score on GameDisplay
        TextScreen (f'Score:{Score}', 25, 'white', 100, 30)

        # For The Explosions
        Explosion.update ()
        Explosion.draw (Screen)

        pygame.display.update ()
        FPS.tick (60)

if GameActive == True:

    choice([
    pygame.mixer.music.load ('Objects/2020-08-11_-_Rise_Up_-_www.FesliyanStudios.com_Steve_Oxen.mp3'),
    pygame.mixer.music.load ('Objects/2020-08-10_-_Go_Beyond_-_David_Fesliyan.mp3')
    ])
    pygame.mixer.music.play ()

    FactsBox = choice ([
        'Sun is the biggest source of energy on earth.',
        'Jupiter is the largest planet in our solar system.',
        'Humans have been continuously making efforts to found ancient lifes on mars.',
        '''India's ISRO has launched more than 100+ satelites in just one go in 2017.''',
        'Our sun itself may someday turn into a BlackHole.',
        'We humans have our own SpaceStation named ISS.',
        'India is looking to make its own SpaceStation.',
        'Our Universe is more than 13 billion years old but its still very young!'
    ])

    while GameActive:
        # Loop Specific Variables
        Choice = 'Objects/background-black.png'

        for events in pygame.event.get():
            if events.type == pygame.MOUSEMOTION:
                Choice = choice (['Objects/background-black.png',
                                  'Objects/SP2.jpg',
                                  'Objects/SP3.jpg',
                                  ])

        # For Background of Welcome Screen
        BGImage = pygame.transform.scale(pygame.image.load(Choice).convert_alpha(),(ScreenWidth,ScreenHeight))

        # For Blitting on Screen
        Screen.blit(BGImage,(0,0))

        # Blitting ButtonText On Screen
        Facts = TextScreen(f'Do You Know:{FactsBox}',30,'green',80,150)
        Start = TextScreen('Start',70,'green',ScreenWidth//2 - 50,ScreenHeight//2 - 80)
        Quit = TextScreen('Quit',70,'green',ScreenWidth//2 - 50,ScreenHeight//2 + 30 - 20)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                print('Start!')
                EXIT()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if Start.collidepoint(events.pos):
                    GameActive = False
                    pygame.mixer.music.stop()
                    FactsBox = choice ([
                        'Sun is the biggest source of energy on earth.',
                        'Jupiter is the largest planet in our solar system.',
                        'Humans have been continuously making efforts to found ancient lifes on mars.',
                        '''India's ISRO has launched more than 100+ satelites in just one go in 2017.''',
                        'Our sun itself may someday turn into a BlackHole.',
                        'We humans have our own SpaceStation named ISS.',
                        'India is looking to make its own SpaceStation.',
                        'Our Universe is more than 13 billion years old but its still very young!'
                    ])
                    Main()
                    pygame.mixer.music.load('Objects/2020-08-10_-_Go_Beyond_-_David_Fesliyan.mp3')
                    pygame.mixer.music.play(1)
                elif Quit.collidepoint(events.pos):
                    EXIT()

        # For Checking Color of the Buttons
        if Choice == 'SP2.jpg':
            color = 'red'
        if Choice == 'SP3.jpg':
            color = 'white'
        if Choice == 'Objects/background-black.png':
            color = 'green'

        # Button Working Mechanism


        pygame.display.update()
        FPS.tick(60)
else:
    Main ()
    # pygame.mixer.music.stop ()

pygame.quit()

