import pygame
pygame.init()

screen_width = 1200
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
        if player1_score >= 3 or player2_score >= 3:
            return
        elif self.number == 1:
            if keys[pygame.K_w]:
                if self.y > 0:
                    self.y -= self.speed
            if keys[pygame.K_s]:
                if self.y + self.height < screen_height:
                    self.y += self.speed
        if self.number == 2:
            if keys[pygame.K_UP]:
                if self.y > 0:
                    self.y -= self.speed
            if keys[pygame.K_DOWN]:
                if self.y + self.height < screen_height:
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
        if player1_score < 3 and player2_score < 3:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def fly(self):
        if player1_score < 3 and player2_score < 3:
            self.x += self.Xspeed
            self.y += self.Yspeed
        
def text(screen, score1, score2):
    font = pygame.font.Font(None, 30)
    score1_text = font.render(f"Score:{score1}", True, white)
    score2_text = font.render(f"Score:{score2}", True, white)
    screen.blit(score1_text, (20, 10))
    screen.blit(score2_text, (screen_width - 100, 10))

def win(screen, text):
    font = pygame.font.Font(None, 60)
    score1_text = font.render(text, True, white)
    screen.blit(score1_text, (screen_width // 2 - 200, screen_height // 2 - 15))

running = True
player1 = Player(50, 250, 30, 100, white, 10, 1)
player2 = Player(screen_width - 80, 250, 30, 100, white, 10, 2)
ball = Ball(screen_width // 2 - 25, screen_height // 2 - 25, 50, 50, white, 8, 8)

player1_score = 0
player2_score = 0

def check_collision(player1, player2, ball):
    global player1_score, player2_score

    if player1_score >= 3 or player2_score >= 3:
        return
    
    if player1.x < ball.x + ball.width and \
        player1.x + player1.width > ball.x and \
        player1.y < ball.y + ball.height and \
        player1.y + player1.height > ball.y:
        ball.Xspeed = max(min(ball.Xspeed * -1 * 1.2, 25), -25)
        ball.Yspeed = max(min(ball.Yspeed * 1.2, 25), -25)  
        ball.x = player1.x + player1.width
    
    elif player2.x < ball.x + ball.width and \
        player2.x + player2.width > ball.x and \
        player2.y < ball.y + ball.height and \
        player2.y + player2.height > ball.y:
        ball.Xspeed = max(min(ball.Xspeed * -1 * 1.2, 25), -25)
        ball.Yspeed = max(min(ball.Yspeed * 1.2, 25), -25)

        ball.x = player2.x - ball.width

    if ball.y < 0:
        ball.y == 0
        ball.Yspeed *= -1

    if ball.y + ball.height > screen_height:
        ball.y = screen_height - ball.height
        ball.Yspeed *= -1

    if ball.x + ball.width > screen_width:
        if player1_score < 3 and player2_score < 3:
            player1_score += 1          
            ball.x = (screen_width // 2) - (ball.width // 2)
            ball.y = (screen_height // 2) - (ball.height // 2)
            ball.Xspeed = 8
            ball.Yspeed = 8

    if ball.x < 0:
        if player1_score < 3 and player2_score < 3:
            player2_score += 1               
            ball.x = (screen_width // 2) - (ball.width // 2)
            ball.y = (screen_height // 2) - (ball.height // 2)
            ball.Xspeed = -8
            ball.Yspeed = -8
        

while running:
    screen.fill((0, 100, 100))
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)
    text(screen, player1_score, player2_score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player2.move(keys)
    player1.move(keys)
    ball.fly()

    if player1_score == 3:
        win(screen, "Player 1 Wins!")
    
    if player2_score == 3:
        win(screen, "Player 2 Wins!")

    check_collision(player1, player2, ball)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()


