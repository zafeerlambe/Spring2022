import pygame, random
blue = (0,64,255)
x = 325
y = 600
x_alien = random.randint(0,600)
y_alien = random.randint(0,500)

y_bullet = y - 40
x_bullet = x

hitX = False
hitY = False
score = 0
count = 0

x_alien_list = []
y_alien_list = []
alien_count = 0

running = True
movingRight = True
movingLeft = False
needMoreAliens = True
bulletState = False


pygame.init()

display = pygame.display.set_mode((700,700))
pygame.display.set_caption('Space Invaders')


while running:

    display.fill(blue)

    image = pygame.image.load(r'C:/Users/irain/OneDrive/Desktop/pyagem/spaceship.png')
    image = pygame.transform.scale(image,(50,50))

    alien = pygame.image.load(r'C:/Users/irain/OneDrive/Desktop/pyagem/ufo.png')
    alien = pygame.transform.scale(alien,(50,50))

    rocket = pygame.image.load(r'C:/Users/irain/OneDrive/Desktop/pyagem/rocket.png')
    rocket = pygame.transform.scale(rocket,(30,30))
    
#moving continuously 
    if x <= 0:
        movingRight = True
        movingLeft = False
        x +=1
        
    elif x >= 650:
        movingRight = False
        movingLeft = True
        x -=1
    else:
        if(movingRight):
            x += 1
        else:
            x -= 1
        display.blit(image, (x, y))

    
##add aliens
    if needMoreAliens:
        x_alien_list.append(random.randint(0,600))
        y_alien_list.append(random.randint(0,500))
        needMoreAliens = False

    if alien_count < 8:
        print(alien_count)
        alien_count += 1
        needMoreAliens = True

    for i in range(alien_count):
        display.blit(alien, (x_alien_list[i], y_alien_list[i]))
        

#add rockets
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and bulletState == False:
            display.blit(rocket, (x,y_bullet))
            x_bullet = x
            bulletState = True
  
    if(y_bullet <= 0):
        bulletState = False
        y_bullet = y-40
    elif bulletState:
        y_bullet -= 1
        display.blit(rocket,(x_bullet, y_bullet))


#collision
#       for i in x_alien_list:
#            if i - abs(x_bullet) <= 25:
#               count += 1

#        if (y_bullet == y_alien_list[count]):
#            bulletState = False
#            y_bullet = y-40
#            display.blit(rocket,(x_bullet, y_bullet))
#        count = 0
            
  
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

pygame.quit()
quit()
