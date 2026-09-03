import pygame
pygame.init()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()
fps = 30

class Player:
    def __init__(self, x, y, width, height, color, speed, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.number = number
 
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        if self.number == 1:
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed 

        elif self.number == 2:
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
        
class Ball:
    def __init__(self, x, y, width, height, color, Xspeed, Yspeed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.Xspeed = Xspeed
        self.Yspeed = Yspeed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def fly(self):
        self.x += self.Xspeed
        self.y += self.Yspeed

running = True
player1 = Player(50, 250, 30, 100, white, 10, 1)
player2 = Player(800, 250, 30, 100, white, 10, 2)
ball = Ball(400, 250, 50, 50, white, 5, 3)

Debounce = False

def check_collision(player1, player2, ball):
    if player1.x < ball.x + ball.width and \
        player1.x + player1.width > ball.x and \
        player1.y < ball.y + ball.height and \
        player1.y + player1.height > ball.y and \
        Debounce == False:
        ball.Xspeed /= -1

    elif player2.x < ball.x + ball.width and \
        player2.x + player2.width > ball.x and \
        player2.y < ball.y + ball.height and \
        player2.y + player2.height > ball.y and \
        Debounce == False:
        ball.Xspeed /= -1
    
    elif ball.y < 0 or \
        ball.y + ball.height > screen_height:
        ball.Yspeed /= -1

while running:
    screen.fill((0, 100, 100))
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player2.move(keys)
    player1.move(keys)
    ball.fly()

    check_collision(player1, player2, ball)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()


