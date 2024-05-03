import pygame
from Block import Block
from hráč import Player
import random
import time

pygame.init()
screen = pygame.display.set_mode([800, 600], pygame.RESIZABLE)
clock = pygame.time.Clock()
blockSize = 30
player = Player(400, 550, blockSize)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
blocks = []
last_block_time = 0
last_block_spawn_time = pygame.time.get_ticks()
font = pygame.font.Font(None, 36)
čas = 1000
pygame.display.set_caption("Uhýbání")

def create_block():
    x = random.randrange(0, 800)
    y = random.randrange(30, 100)
    block = Block(x, y, "", blockSize)
    blocks.append(block)
    all_sprites_list.add(block)

def create_blocks():
    global last_block_spawn_time
    if pygame.time.get_ticks() - last_block_spawn_time > čas:
        create_block()
        last_block_spawn_time = pygame.time.get_ticks()

def collision_detection():
    global hit
    for block in blocks:
        if pygame.sprite.collide_rect(player, block):
            blocks.remove(block)
            all_sprites_list.remove(block)
            hit += 1
            return True
    return False

def draw_time_options(selected_option):
    options = ["10s", "20s", "30s", "40s", "50s", "60s"]
    text_color = (255, 255, 255)
    selected_color = (255, 0, 0)
    x_start = 300
    y_start = 300
    spacing = 50
    for i, option in enumerate(options):
        text = font.render(option, True, selected_color if i == selected_option else text_color)
        screen.blit(text, (x_start + i * spacing, y_start))

def select_time():
    global options
    selected_option = options.index("30s")
    while True:
        screen.fill((0, 0, 0))
        draw_time_options(selected_option)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_option = max(0, selected_option - 1)
                elif event.key == pygame.K_RIGHT:
                    selected_option = min(len(options) - 1, selected_option + 1)
                elif event.key == pygame.K_RETURN:
                    return (selected_option + 1) * 10 * 1000

options = ["10s", "20s", "30s", "40s", "50s", "60s"]
čas = select_time()

diff = "Lehká"
k = 0
i = 0
hit = 0
m = 0
casy = []
jes = 0
konec = False
running = True
Konec_cas = čas
e1 = time.time()
while running:
    e2 = time.time()
    ticks = round(e2 - e1) * 1000
    if (Konec_cas // 6) > ticks:
        čas = 500
        diff = "1/5"
    elif (Konec_cas // 6) <= ticks and (Konec_cas // 6) * 2 > ticks:
        player.vybarvi(1)
        čas = 200
        diff = "2/5"
    elif (Konec_cas // 6) * 2 <= ticks and (Konec_cas // 6) * 3 > ticks:
        player.vybarvi(2)
        čas = 100
        diff = "3/5"
    elif (Konec_cas // 6) * 3 <= ticks and (Konec_cas // 6) * 4 > ticks:
        player.vybarvi(3)
        čas = 50
        diff = "4/5"
    elif (Konec_cas // 6) * 4 <= ticks:
        čas = 10
        player.vybarvi(4)
        diff = "BONUS"
    clock.tick(60)
    okay = ticks
    create_blocks()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if okay >= Konec_cas - 1:
        konec = True
    keys = pygame.key.get_pressed()
    direction = None
    if keys[pygame.K_LEFT]:
        direction = "left"
    elif keys[pygame.K_RIGHT]:
        direction = "right"
    obtiznost = font.render(f"Část: {diff}", True, (255, 255, 255))
    screen.blit(obtiznost, (350, 20))
    player.update(direction)
    score = font.render(f"Skóre: {hit}", True, (255, 255, 255))
    screen.blit(score, (20, 570))
    okays = round(okay / 1000, 1)
    cas = font.render(f"čas: {ticks // 1000} / {Konec_cas // 1000} s", True, (255, 255, 255))
    screen.blit(cas, (550, 570))

    for block in blocks[:]:
        block.update()
        if block.rect.y > 550:
            blocks.remove(block)
            all_sprites_list.remove(block)

    all_sprites_list.update() 
    all_sprites_list.draw(screen)
    if collision_detection():
        if m == 0:
            m += 1
            jeden = time.time()
        elif m >= 1:
            dva = time.time()
            finito = round(dva - jeden, 3)
            if finito >= 1:
                pass
            elif finito < 1:
                if k == 0:
                    jes = okay
    else:
        pygame.display.flip()
    if konec:
        screen.fill((0, 0, 0))
        text = font.render("Konec", True, (255, 255, 255))
        text1 = font.render(f"Konečné Skóre: {hit}", True, (255, 255, 255))
        screen.blit(text1, (330, 280))
        screen.blit(text, (350, 240))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        running = False

pygame.quit()
