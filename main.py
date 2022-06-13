from sys import exit
import pygame.draw
from pygame import mixer
from pygame import event
import random


def bar_cords():
    sprite_front_rect.x = 650
    sprite_right_rect.x = 650
    sprite_back_rect.x = 650
    sprite_left_rect.x = 650
    sprite_front_rect.y = 550
    sprite_right_rect.y = 550
    sprite_back_rect.y = 550
    sprite_left_rect.y = 550


def restart_cords():
    sprite_front_rect.x = 30
    sprite_right_rect.x = 30
    sprite_back_rect.x = 30
    sprite_left_rect.x = 30


def back_to_path1():
    sprite_front_rect.x = 1280
    sprite_back_rect.x = 1280
    sprite_right_rect.x = 1280
    sprite_left_rect.x = 1280


def move_right():
    sprite_back_rect.x += 30
    sprite_front_rect.x += 30
    sprite_right_rect.x += 30
    sprite_left_rect.x += 30


def move_left():
    sprite_left_rect.x -= 30
    sprite_right_rect.x -= 30
    sprite_back_rect.x -= 30
    sprite_front_rect.x -= 30


def move_up():
    sprite_back_rect.y -= 30
    sprite_front_rect.y -= 30
    sprite_right_rect.y -= 30
    sprite_left_rect.y -= 30


def move_down():
    sprite_back_rect.y += 30
    sprite_front_rect.y += 30
    sprite_right_rect.y += 30
    sprite_left_rect.y += 30


def update_path1():
    global background
    screen.blit(background, (0, 0))
    if sprite_left_rect.x >= 1300:
        restart_cords()
        background = path2
        screen.blit(background, (0, 0))
        screen.blit(house, house_rect)
    elif sprite_right_rect.x <= 0:
        sprite_right_rect.x += 20
    elif sprite_front_rect.y >= 700:
        sprite_front_rect.y -= 20
    elif sprite_back_rect.y >= 0:
        sprite_back_rect.y += 20


def in_bar():
    bar_cords()
    background = bar
    screen.blit(background, (0, 0))


def dice():  # making the different outcomes
    if dice_roll == 1:
        screen.fill((0, 0, 0))
        screen.blit(Outcome1, (0, 0))
    elif dice_roll == 2:
        screen.fill((0, 0, 0))
        screen.blit(Outcome2, (0, 0))
    elif dice_roll == 3:
        screen.fill((0, 0, 0))
        screen.blit(Outcome3, (0, 0))
    elif dice_roll == 4:
        screen.fill((0, 0, 0))
        screen.blit(Outcome4, (0, 0))
    elif dice_roll == 5:
        screen.fill((0, 0, 0))
        screen.blit(Outcome5, (0, 0))
    elif dice_roll == 6:
        screen.fill((0, 0, 0))
        screen.blit(Outcome6, (0, 0))


pygame.init()  # start game
mixer.init()  # initiate music
screen = pygame.display.set_mode((1300, 700))
screen.fill((255, 255, 255))
pygame.display.set_caption('Quest of Glory')  # name the game
clock = pygame.time.Clock()
font = pygame.font.Font('Koulen-Regular.ttf', 40)  # font big
small_font = pygame.font.Font('Koulen-Regular.ttf', 30)  # font small
game_active = True

wipe1 = pygame.image.load('BarTenderWipe1.png').convert_alpha()  # bartender sprite
wipe1_rect = wipe1.get_rect(center=(850, 260))
wipe2 = pygame.image.load('BarTenderWipe2.png').convert_alpha()
wipe2_rect = wipe2.get_rect(center=(850, 260))
wipe3 = pygame.image.load('BarTenderWipe3.png').convert_alpha()
wipe3_rect = wipe3.get_rect(center=(850, 260))
wipe4 = pygame.image.load('BarTenderWipe4.png').convert_alpha()
wipe4_rect = wipe4.get_rect(center=(850, 260))


dragon = pygame.image.load('DragonDown.png').convert_alpha()  # dragon sprite
dragon_rect = dragon.get_rect(center=(800, 500))

start_text = font.render(' If you wish to play, press space ', False, (255, 255, 255))  # starting page text
start_text_rect = start_text.get_rect(center=(650, 350))

dice_roll = random.randint(1, 6)  # roll your dice
dice1 = font.render('''You rolled a :''' + str(dice_roll) + ''' \n Please hit SPACE to see your outcome...''', False, (255, 255, 255)).convert()
dice1_rect = dice1.get_rect(center=(650, 200))

Outcome1 = pygame.image.load('Outcome1.png')  # Outcome images
Outcome2 = pygame.image.load('Outcome2.png')
Outcome3 = pygame.image.load('Outcome3.png')
Outcome4 = pygame.image.load('Outcome4.png')
Outcome5 = pygame.image.load('Outcome5.png')
Outcome6 = pygame.image.load('Outcome6.png')

control_text = small_font.render(' Use WASD to move ', False, (0, 0, 0),)  # movement command text
control_text_rect = start_text.get_rect(center=(840, 650))

mission_text = font.render('Hello traveller. Would you like a quest? Y/N', False, (255, 255, 255))  # mission texts
mission_text_rect = mission_text.get_rect(center=(650, 630))
mission_text1 = small_font.render('hit "y" for yes and "n" for no', False, (255, 255, 255))
mission_text_rect1 = mission_text1.get_rect(center=(650, 675))
mission_text2 = font.render("There is a dragon terrorizing the town, you must slay it. Here's a map. Leave? Y/N", False, (255,255,255))
mission_text_rect2 = mission_text2.get_rect(center=(650, 630))


start = pygame.image.load('download.png').convert()  # backgrounds
bar = pygame.image.load('barbackground.jpg').convert()
path1 = pygame.image.load('path1.png').convert()
path2 = pygame.image.load('path2.png').convert()
house = pygame.image.load('House.png').convert_alpha()
house_rect = house.get_rect(topleft=(1000, 200))
battle = pygame.image.load('Battle.png').convert_alpha()
final_screen = screen.fill((0, 0, 0))
background = path1


sprite_front = pygame.image.load('GirlFront.png').convert_alpha()  # your character sprite files
sprite_front_rect = sprite_front.get_rect(midbottom=(40, 500))
sprite_back = pygame.image.load('GirlBack.png').convert_alpha()
sprite_back_rect = sprite_back.get_rect(midbottom=(40, 500))
sprite_left = pygame.image.load('GirlLeft.png').convert_alpha()
sprite_left_rect = sprite_left.get_rect(midbottom=(40, 500))
sprite_right = pygame.image.load('GirlRight.png').convert_alpha()
sprite_right_rect= sprite_right.get_rect(midbottom=(40, 500))
sprite_reactive = pygame.image.load('GirlFightReactive.png').convert_alpha()
sprite_reactive_rect = sprite_reactive.get_rect(midbottom=(40, 500))
sprite_fight = pygame.image.load('GirlFight.png').convert_alpha()
sprite_fight_rect = sprite_fight.get_rect(center=(200, 650))


mixer.music.load('MedievalMusic.wav')  # music
mixer.music.set_volume(2)
mixer.music.play(-1)

screen.blit(start, (0, 0))
screen.blit(start_text, start_text_rect)

wipe = wipe1
wipe_rect = wipe1_rect

text = mission_text
rect = mission_text_rect

text1 = mission_text1
rect1 = mission_text_rect1

x = 0
while True:
    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # stop game is Esc is pressed
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE and x == 0:
                    x = x + 1
                    mixer.music.set_volume(0.2)
                    screen.blit(path1, (0, 0))
                    screen.blit(control_text, control_text_rect)
                    start_time = int(pygame.time.get_ticks() / 1000)  # restart score
                    screen.blit(sprite_right, sprite_right_rect)
                elif event.key == pygame.K_w:  # move up when w is pressed
                    update_path1()
                    move_up()
                    screen.blit(sprite_back, sprite_back_rect)
                elif event.key == pygame.K_a:  # move left when a is pressed
                    move_left()
                    update_path1()
                    screen.blit(sprite_left, sprite_left_rect)
                elif event.key == pygame.K_s:  # move down when s is pressed
                    move_down()
                    update_path1()
                    screen.blit(sprite_front, sprite_front_rect)
                elif event.key == pygame.K_d:  # move right when d is pressed
                    move_right()
                    update_path1()
                    screen.blit(sprite_right, sprite_right_rect)

            if background == path2:
                screen.blit(house, house_rect)
                if sprite_right_rect.colliderect(house_rect):
                    background = bar
                    screen.blit(background, (0, 0))
                    in_bar()
                    bar_cords()
                elif sprite_right_rect.x <= 10:
                    background = path1
                    screen.blit(background, (0, 0))
                    back_to_path1()
            if background == bar:
                screen.blit(wipe, wipe_rect)
                if sprite_right_rect.y <= 420:
                    screen.blit(text, rect)
                    screen.blit(text1, rect1)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y and x >= 1:
                            text = mission_text2
                            rect = mission_text_rect2
                            screen.blit(background, (0, 0))
                            screen.blit(wipe, wipe_rect)
                            x = x + 1
                            if event.key == pygame.K_y and x > 2:
                                background = battle
                                screen.blit(background, (0, 0))
                                screen.blit(dice1, dice1_rect)
                            elif event.key == pygame.K_n:
                                exit()
                                pygame.quit()
                        elif event.key == pygame.K_n:
                            exit()
                            pygame.quit()
            if background == battle:
                screen.blit(dragon, dragon_rect)
                screen.blit(sprite_fight, sprite_fight_rect)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        background = final_screen
                        dice()

    pygame.display.update()  # keep window open and update
    clock.tick(60)  # frame rate
