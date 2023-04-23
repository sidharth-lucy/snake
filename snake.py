import pygame 
import random
import sys


pygame.init()

clock = pygame.time.Clock
white= (255,255,255)
red = (255, 0,0)
black = (0,0,0)
green = (90, 245, 66)


screen_w = 900
screen_h = 600 

game_window = pygame.display.set_mode((screen_w,screen_h))

pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)


def text_screen(text ,color ,x,y):
    game_window.fill(black)
    screen_text = font.render(text ,True ,color)
    text_react = screen_text.get_rect()

    game_window.blit(screen_text, [x,y])
    pygame.display.update()






snake_head= [60,60]
snake_list=[[60,60] ,[40,60] ,[20,60]]
snake_list_set= set([(60,60),(40,60),(20,60)])

food_exist = True 
food_location = [(random.randint(1,(screen_w-20)//20))*20 , (random.randint(3,(screen_h-20)//20))*20 , 20 ,20] 

score =  0
dirs = 'right'
n_dirs= dirs
 

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP and dirs not in ['up' , 'donw']:
                snake_head[1]= snake_head[1]-20
                n_dirs = 'up'
            elif event.key == pygame.K_DOWN and dirs not in ['up' , 'donw']:
                snake_head[1]= snake_head[1]+20
                n_dirs = 'down'
            elif event.key == pygame.K_LEFT and dirs not in ['left' , 'right']:
                snake_head[0]= snake_head[0]-20
                n_dirs = 'left'
            elif event.key == pygame.K_RIGHT and dirs not in ['left' , 'right']:
                snake_head[0]= snake_head[0]+20
                n_dirs = 'right'
            
        
        

    if n_dirs==dirs:
        if dirs=='right':
            snake_head[0]= snake_head[0]+20
        elif dirs=='left':
            snake_head[0]= snake_head[0]-20
        elif dirs=='up':
            snake_head[1]= snake_head[1]-20
        elif dirs=='down':
            snake_head[1]= snake_head[1]+20

    else:
        dirs= n_dirs

    # Game over 
    if tuple(snake_head) in snake_list_set or snake_head[0]<0 or snake_head[0]>900 or snake_head[1]<0 or snake_head[1]>600 :
        
        mess = "Game Over , Your Score is :" + str(score)
        text_screen(mess , green , 20 ,250)
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()



    snake_list.insert(0, snake_head[:])
    snake_list_set.add(tuple(snake_head))

    if snake_head[0]!= food_location[0] or snake_head[1]!=food_location[1]:
        snake_list_set.remove(tuple(snake_list.pop()))
    else:
        score+=1
        food_exist= False
    
    if not food_exist:
        food_location = [(random.randint(1,(screen_w-20)//20))*20 , (random.randint(3,(screen_h-20)//20))*20 , 20 ,20] 
        food_exist = True


    # print(snake_head, food_location)
    print(snake_list)

    game_window.fill(white)
    for x,y in snake_list:
        pygame.draw.rect(game_window , black ,pygame.Rect(x, y, 20 ,20))

    pygame.draw.rect(game_window , green , food_location)

    pygame.display.update()
    clock.tick(10)























