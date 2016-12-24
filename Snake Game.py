import pygame
import random

class Snake(pygame.sprite.Sprite):
    '''A class to create the snake object, this will let it be manipulated throughout program'''
    def __init__(self, Colour, Width, Height):

        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(Colour)

        pygame.draw.rect(self.image, Colour, (x, y, Width, Height))

        self.rect = self.image.get_rect()

    '''Functions to allow movement'''
    def Up(self, speed):
        self.rect.y += speed

    def Down(self, speed):
        self.rect.y += speed

    def Right(self, speed):
        self.rect.x += speed

    def Left(self, speed):
        self.rect.x += speed



class Food(pygame.sprite.Sprite):
    '''A class to create a food object, this will be able to be manipulated throughout the program'''
    def __init__(self, Colour, Width, Height):

        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(Colour)

        pygame.draw.rect(self.image, Colour, (0, 0, 10, 10))

        self.rect = self.image.get_rect()



def Scoreboard():
    '''Function to show player their score'''
    Text = pygame.font.Font('freesansbold.ttf', 20)
    TextSurface = Text.render('Score: ' + str(SnakeLength), True, white)
    Screen.blit(TextSurface, (0,0))

    pygame.display.update()

#Define all variables that will be used throughout prorgam
ScreenWidth = 500
ScreenHeight = 500
xSpeed = 0
ySpeed = 0
x = 0
y = 0
Foodx = random.randrange(0, ScreenWidth, 10)
Foody = random.randrange(0, ScreenHeight, 10)
SnakeLength = 0
SnakeTailx = []
SnakeTaily = []


#assign colours
black = (32, 32, 32)
white = (255, 255, 255)
red = (245, 0, 0)

#initialise pygame
pygame.init()
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

#Lists used for sprites
SpriteList = pygame.sprite.Group()
SnakeList = pygame.sprite.Group()

#Create Food
FoodPart = Food(red, ScreenWidth, ScreenHeight)
FoodPart.rect.x = Foodx
FoodPart.rect.y = Foody
#Add food to the sprite list
SpriteList.add(FoodPart)

#Create snake
SnakeBody = Snake(white, ScreenWidth, ScreenHeight)
SnakeBody.rect.x = ScreenWidth/2
SnakeBody.rect.y = ScreenHeight/2
#Add snake to the sprite list
SpriteList.add(SnakeBody)



Collide = False

#forever loop
while not Collide:



    #Check if snake hit the food
    if FoodPart.rect.x == SnakeBody.rect.x and FoodPart.rect.y == SnakeBody.rect.y:
        FoodPart.rect.x = random.randrange(0, ScreenWidth, 10)
        FoodPart.rect.y = random.randrange(0, ScreenWidth, 10)
        SnakeLength += 1
        print(SnakeLength)
        print("Food Found")


    #if snake collides with boundaries end game
    if SnakeBody.rect.x < 0 or SnakeBody.rect.x >= ScreenWidth:
        print("Hit x axis")
        Collide = True
    elif SnakeBody.rect.y < 0 or SnakeBody.rect.y >= ScreenHeight:
        print("Hit y axis")
        Collide = True

    #if snake collides with itself end game
    CheckSnakeCollision = pygame.sprite.spritecollide(SnakeBody, SnakeList, False)
    for i in CheckSnakeCollision:
        print("Hit itself")
        Collide = True


    #Handle inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Collide = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                xSpeed = -10
                ySpeed = 0
                SnakeBody.Left(xSpeed)
            elif event.key == pygame.K_RIGHT:
                xSpeed = 10
                ySpeed = 0
                SnakeBody.Right(xSpeed)
            elif event.key == pygame.K_UP:
                ySpeed = -10
                xSpeed = 0
                SnakeBody.Up(ySpeed)
            elif event.key == pygame.K_DOWN:
                ySpeed = 10
                xSpeed = 0
                SnakeBody.Down(ySpeed)

    # Make the snake longer for every food eaten
    SnakeTailx.append(SnakeBody.rect.left)
    SnakeTaily.append(SnakeBody.rect.top)

    if len(SnakeTailx) > SnakeLength:
        SnakeTailx.remove(SnakeTailx[0])

    if len(SnakeTaily) > SnakeLength:
        SnakeTaily.remove(SnakeTaily[0])

    SnakeList.empty()

    for i in range(0, SnakeLength):
        tail = Snake(white, ScreenWidth, ScreenHeight)
        tail.rect.x = SnakeTailx[i]
        tail.rect.y = SnakeTaily[i]
        SnakeList.add(tail)


    #update all the sprites
    SpriteList.update()
    SnakeList.update()

    #create the background
    Screen.fill((black))


    #draw sprites onto the screen so they can be seen
    SpriteList.draw(Screen)
    SnakeList.draw(Screen)


    SnakeBody.rect.x += xSpeed      # keep incrementing by the speed so snake is still moving
    SnakeBody.rect.y += ySpeed
    Scoreboard()
    pygame.display.update()
    clock.tick(10)  #frames per second
pygame.quit()
quit()


