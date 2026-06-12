import pygame
pygame.init()
#---------------------#
#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window = pygame.display.set_mode((1300, 700))

numb_printer = pygame.font.Font(None, 50)
printer_img = numb_printer.render("счётчик", True, (50, 0, 255))

gmov_printer = pygame.font.Font(None, 50)
gmov_img = gmov_printer.render("проигрыши", True, (250, 160, 5))

pygame.display.set_caption("Ping Pong")
FPS = 120
class Game_Object:
    def __init__(self, x, y, w, h, color):
        self.hitbox = pygame.Rect(x, y, w, h)
        self.color = color
        self.count = 0
        self.speed = 4
        self.gmov_count = 0
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
    def auto_bot(self):
        if ball.hitbox.y > bot.hitbox.y:
            bot.hitbox.y += self.speed
        if ball.hitbox.y < bot.hitbox.y:
            bot.hitbox.y -= self.speed

player = Game_Object(20, 250, 100, 100, (250, 0, 0))
bot = Game_Object(1200, 0, 100, 100, (0, 0, 250))
class Ball:
    def __init__(self, x, y, w, h, color):
        self.hitbox = pygame.Rect(x, y, w, h)
        self.color = color
        self.speedx = 5
        self.speedy = 5
    def control(self):
        global printer_img
        global gmov_printer
        self.hitbox.x += self.speedx
        self.hitbox.y += self.speedy
        if self.hitbox.bottom > 700:
            self.speedy = -5
        if self.hitbox.right > 1300:
            self.speedx = -5
        if self.hitbox.top < 0:
            self.speedy = 5
        if self.hitbox.left < 0:
            self.hitbox.x = 650
            self.hitbox.y = 350
            player.gmov_count +=1
        if self.hitbox.colliderect(player.hitbox):
            self.hitbox.x = player.hitbox.right + 4
            self.speedx = 5
            player.count += 1
        if self.hitbox.colliderect(bot.hitbox):
            self.speedx = -5
        printer_img = numb_printer.render("счёт:" + str(player.count), True, (50, 0, 255))
        gmov_img = gmov_printer.render("проигрыши" + str(player.gmov_count), True, (250, 160, 5))

ball = Ball(5, 8, 50, 50, (0, 250, 0))

while True:
    window.fill((0, 0, 0))
    window.blit(printer_img, (0, 0))
    window.blit(gmov_img, (0, 20))

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
    bot.auto_bot()
    pygame.draw.rect(window, player.color, player.hitbox)
    pygame.draw.rect(window, ball.color, ball.hitbox)
    pygame.draw.rect(window, bot.color, bot.hitbox)
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
