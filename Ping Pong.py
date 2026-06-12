import pygame
#---------------------#
#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window = pygame.display.set_mode((1300, 700))

pygame.display.set_caption("Ping Pong")
FPS = 120
class Game_Object:
    def __init__(self, x, y, w, h, color):
        self.hitbox = pygame.Rect(x, y, w, h)
        self.color = color
    def control(self):
        button_list = pygame.key.get_pressed()
        if button_list[pygame.K_w] == True:
            self.hitbox.y -= 9
        if button_list[pygame.K_s] == True:
            self.hitbox.y += 9
        if button_list[pygame.K_UP] == True:
            self.hitbox.y -= 9
        if button_list[pygame.K_DOWN] == True:
            self.hitbox.y += 9
        print("W-",button_list[pygame.K_w], "  ", "S-",button_list[pygame.K_s], "  ", "DOWN-",button_list[pygame.K_DOWN], "  ", "UP-",button_list[pygame.K_UP], "   ", "FPS-", FPS)

player = Game_Object(25, 8, 100, 100, (250, 0, 0))

class Ball:
    def __init__(self, x, y, w, h, color):
        self.hitbox = pygame.Rect(x, y, w, h)
        self.color = color
        self.speedx = 5
        self.speedy = 5
    def control(self):
        self.hitbox.x += self.speedx
        self.hitbox.y += self.speedy
        if self.hitbox.bottom > 700:
            self.speedy = -5
        if self.hitbox.right > 1300:
            self.speedx = -5
        if self.hitbox.top < 0:
            self.speedy = 5
        if self.hitbox.left < 0:
            self.speedx = 5
        if self.hitbox.colliderect(player.hitbox):
            self.speedx = 5
ball = Ball(5, 8, 50, 50, (0, 250, 0))

while True:
    window.fill((0, 0, 0))
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                pass
            if event.key == pygame.K_ESCAPE:  # Если нажат Esc
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_z):
                    pass
    player.control()
    ball.control()
    pygame.draw.rect(window, player.color, player.hitbox)
    pygame.draw.rect(window, ball.color, ball.hitbox)
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
