import pygame
import random
import time
pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
fps = 30

jump_sound = pygame.mixer.Sound("dino_Jump.wav")
fail_sound = pygame.mixer.Sound("dino_Fail.wav")

pygame.mixer.music.load("Scheming_Weasel_Faster.mp3")

dino_img = pygame.image.load("Dino.png")
obstacle_img = pygame.image.load("Cactus.png")
ground_img = pygame.image.load("Ground.jpg")

dino_img = pygame.transform.scale(dino_img, (50, 50))
ground_img = pygame.transform.scale(ground_img, (screen_width, 80))

class Dino:
    def __init__(self):
        self.x = 100
        self.width = 50
        self.height = 50
        self.y = screen_height - self.height - 50
        self.is_jumping = False
        self.jump_count = 10
        self.gravity = 1
        self.image = dino_img

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

class Obstacle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.spawn_delay = random_time()
        self.image = obstacle_img

    def draw(self, screen):
        screen.blit(obstacle_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        if running == False:
            return
        self.x -= self.speed
        if self.x < -self.width - self.spawn_delay:
            global score_debounce, obstacle_img
            self.x = screen_width
            self.spawn_delay = random_time()
            random_obst = random_obstacle()

            if random_obst == 1:
                self.y = screen_height - 110
                self.width = 40
                self.height = 60
            elif random_obst == 2:
                self.y = screen_height - 90
                self.width = 60
                self.height = 40
            elif random_obst == 3:
                self.y = screen_height - 120
                self.width = 40
                self.height = 70
            elif random_obst == 4:
                self.y = screen_height - 130
                self.width = 60
                self.height = 80
            elif random_obst == 5:
                self.y = screen_height - 100
                self.width = 70
                self.height = 50

            obstacle_img = pygame.transform.scale(obstacle_img, (obstacle.width, obstacle.height))
            score_debounce = False

class Ground:
    def __init__(self):
        self.x1 = 0
        self.x2 = screen_width
        self.y = screen_height - 80
        self.speed = 20
        self.image = ground_img

    def move(self):
        if running == False:
            return
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 <= -screen_width:
            self.x1 = 0
            self.x2 = screen_width
    
    def draw(self, screen):
        screen.blit(ground_img, (self.x1, self.y))
        screen.blit(ground_img, (self.x2, self.y))



def display_score(score, screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

def display_highscore(score, screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Highscore: {score}", True, (0, 0, 0))
    screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))

def display_jumps(jumps, screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Jumps: {jumps}", True, (0, 0, 0))
    screen.blit(score_text, (10, 40))

def display_lose(screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Game Over! Press Space to Start", True, (0, 0, 0))
    screen.blit(score_text, (screen_width * 0.5 - score_text.get_width() * 0.5, screen_height * 0.5 - score_text.get_height() * 0.5))

def display_start(screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Press Space to Start", True, (0, 0, 0))
    screen.blit(score_text, (screen_width * 0.5 - score_text.get_width() * 0.5, screen_height * 0.5 - score_text.get_height() * 0.5))

def random_obstacle(): 
    return random.randint(1, 5)

def random_time():
    return random.choice([0, 200, 600])

pygame.mixer.music.play(-1)

dino = Dino()
ground = Ground()

random_obst = random_obstacle()

if random_obst == 1:
    obstacle = Obstacle(screen_width, screen_height - 110, 40, 60, 20)
elif random_obst == 2:
    obstacle = Obstacle(screen_width, screen_height - 90, 50, 40, 20)
elif random_obst == 3:
    obstacle = Obstacle(screen_width, screen_height - 120, 40, 70, 20)
elif random_obst == 4:
    obstacle = Obstacle(screen_width, screen_height - 130, 60, 80, 20)
elif random_obst == 5:
    obstacle = Obstacle(screen_width, screen_height - 100, 70, 50, 20)

obstacle_img = pygame.transform.scale(obstacle_img, (obstacle.width, obstacle.height))
    
score = 0
highscore = 0
jumps = 0
running = True
game_over = False
score_debounce = False
start = False

while running:
    while not start:
        screen.fill((255, 255, 255))
        display_start(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    start = True
        pygame.display.update()
        clock.tick(fps)

    if score < 50:
        screen.fill((255, 255, 255))
    else:
        screen.fill((210,255,210))
    ground.draw(screen)
    dino.draw(screen)
    obstacle.draw(screen)
    obstacle.move()
    ground.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        # Проверка на столкновение

        if dino.get_rect().colliderect(obstacle.get_rect()):
            game_over = True
            fail_sound.play()

        # Обработка событий
    

        keys = pygame.key.get_pressed()
        if not dino.is_jumping:
            if keys[pygame.K_SPACE]:
                jumps += 1
                dino.is_jumping = True
                jump_sound.play()

        dino.jump()

        # Подсчет очков
        if obstacle.x + obstacle.width < dino.x and score_debounce == False:
            score += 1
            if score > highscore:
                highscore = score
                
            if obstacle.speed < 50:
                obstacle.speed += 2
                ground.speed += 2
            score_debounce = True

    if game_over:
        while game_over:
            screen.fill((255, 255, 255))
            ground.draw(screen)
            dino.draw(screen)
            obstacle.draw(screen)
            display_score(score, screen)
            display_highscore(highscore, screen)
            display_jumps(jumps, screen)
            display_lose(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        game_over = False
            pygame.display.update()
            clock.tick(fps)
        
        pygame.display.update()
        game_over = False
        score = 0
        jumps = 0
        obstacle.speed = 20
        obstacle.x = screen_width
        dino.y = screen_height - dino.height - 50
        dino.is_jumping = False
        dino.jump_count = 10
        ground.x1 = 0
        ground.x2 = screen_width
        ground.speed = 20

        random_obst = random_obstacle()

        if random_obst == 1:
            obstacle.y = screen_height - 110
            obstacle.width = 40
            obstacle.height = 60
        elif random_obst == 2:
            obstacle.y = screen_height - 90
            obstacle.width = 60
            obstacle.height = 40
        elif random_obst == 3:
            obstacle.y = screen_height - 120
            obstacle.width = 40
            obstacle.height = 70
        elif random_obst == 4:
            obstacle.y = screen_height - 130
            obstacle.width = 60
            obstacle.height = 80
        elif random_obst == 5:
            obstacle.y = screen_height - 100
            obstacle.width = 70
            obstacle.height = 50
        obstacle_img = pygame.transform.scale(obstacle_img, (obstacle.width, obstacle.height))

    display_jumps(jumps, screen)
    display_score(score, screen)
    display_highscore(highscore, screen)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()


