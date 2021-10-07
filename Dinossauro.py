import pygame, os, random

#Cores e Dimensões
black = (0, 0, 0)
white = (255, 255, 255)
largura_janela = 640
altura_janela = 480

pygame.init()

#Fonte
fonte = pygame.font.SysFont("Impact", 40)

#Imagens
path_1 = os.path.join(os.path.dirname(__file__), "left_leg.png") 
path_2 = os.path.join(os.path.dirname(__file__), "right_leg.png")
path_3 = os.path.join(os.path.dirname(__file__), "jump.png")
path_4 = os.path.join(os.path.dirname(__file__), "sun.png") # Sol
path_5 = os.path.join(os.path.dirname(__file__), "cloud_1.png") # Nuvem 1
path_6 = os.path.join(os.path.dirname(__file__), "cloud_2.png") # Nuvem 2
path_7 = os.path.join(os.path.dirname(__file__), "cloud_3.png") # Nuvem 3
path_8 = os.path.join(os.path.dirname(__file__), "cloud_4.png") # Nuvem 4
path_9 = os.path.join(os.path.dirname(__file__), "cacto.png") # Cacto

class make_sprite(pygame.sprite.Sprite):
    def __init__(self, img, pos_y, pos_x = 30):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

#Janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Google's Dinosaur")

#Velocidades
vel_y = 3
vel_x_cacto = 1.5
vel_x_nuvem = 0.3

#Posições
x = 30
y = 430
x_cacto1 = random.randint(200, 300)
x_cacto2 = random.randint(500, 600)
x_cacto3 = random.randint(800, 900)
x_nuvem1 = 140
x_nuvem2 = 270
x_nuvem3 = 430
x_nuvem4 = 580

#Sprites
sun = make_sprite(path_4, 80, 530)
cenário_group = pygame.sprite.Group()
cenário_group.add(sun)

press = ""
cont = 0
score_n = 0

pare = False

game_over_text = fonte.render("Game Over", True, black)
game_over = game_over_text.get_rect()
game_over.center = (largura_janela / 2, altura_janela / 2)

while True:
    if pare == False:
        score_n += 1

    score_text = fonte.render(f"Score: {score_n}", True, black)
    score = score_text.get_rect()
    score.center = (80, 40)

    if pare == False:
        if cont > 6:
            cont = 0
        cont += 1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
        
    if pygame.key.get_pressed()[pygame.K_UP]: #Pular
        if y >= 430:
            press = True

    if press == True:
        y -= vel_y
        dino = make_sprite(path_3, y)
    elif press == False:
        y += vel_y
        dino = make_sprite(path_3, y)

    if y <= 230:
        press = False
    elif y >= 430:
        if 0 <= cont <= 3:
            dino = make_sprite(path_1, y)
        elif 3 <= cont <= 6:
            dino = make_sprite(path_2, y)
        press = ""

    cacto1 = make_sprite(path_9, 410, x_cacto1)
    cacto2 = make_sprite(path_9, 410, x_cacto2)
    cacto3 = make_sprite(path_9, 410, x_cacto3)

    cloud_1 = make_sprite(path_5, 138, x_nuvem1)
    cloud_2 = make_sprite(path_6, 143, x_nuvem2)
    cloud_3 = make_sprite(path_7, 150, x_nuvem3)
    cloud_4 = make_sprite(path_8, 210, x_nuvem4)

    x_cacto1 -= vel_x_cacto
    x_cacto2 -= vel_x_cacto
    x_cacto3 -= vel_x_cacto

    x_nuvem1 -= vel_x_nuvem
    x_nuvem2 -= vel_x_nuvem
    x_nuvem3 -= vel_x_nuvem
    x_nuvem4 -= vel_x_nuvem

    if dino.rect.colliderect(cacto1.rect):
        if dino.rect.right - cacto1.rect.left > 28 or dino.rect.right - cacto2.rect.left > 28 or dino.rect.right - cacto3.rect.left > 28:
            vel_x_cacto = 0
            vel_y = 0
            vel_x_nuvem = 0
            dino = make_sprite(path_3, y)
            pare = True
            cont = 7

        '''if y == cacto1.rect.top:
            if dino.rect.bottom - cacto1.rect.top == 1 or dino.rect.bottom - cacto2.rect.top == 1 or dino.rect.bottom - cacto3.rect.top == 1:
                vel_x_cacto = 0
                vel_y = 0
                vel_x_nuvem = 0
                dino = make_sprite(path_3, y)
                pare = True
                cont = 7'''

    if x_cacto1 < 0:
        x_cacto1 = random.randint(600, 700)
    if x_cacto2 < 0:
        x_cacto2 = random.randint(900, 1000)
    if x_cacto3 < 0:
        x_cacto3 = random.randint(1200, 1300)

    if x_nuvem1 < -30:
        x_nuvem1 = random.randint(650, 700)
    if x_nuvem2 < -10:
        x_nuvem2 = random.randint(720, 800)
    if x_nuvem3 < -10:
        x_nuvem3 = random.randint(830, 900)
    if x_nuvem4 < -10:
        x_nuvem4 = random.randint(900, 1000)

    móveis_group = pygame.sprite.Group()
    móveis_group.add(dino)
    móveis_group.add(cacto1)
    móveis_group.add(cacto2)
    móveis_group.add(cacto3)
    móveis_group.add(cloud_1)
    móveis_group.add(cloud_2)
    móveis_group.add(cloud_3)
    móveis_group.add(cloud_4)

    janela.fill((187, 191, 189))
    if pare:
        janela.blit(game_over_text, game_over)
    janela.blit(score_text, score)
    pygame.draw.polygon(janela, (107, 110, 108), [(0, 430), (0, 480), (640, 480), (640, 430)], width = 0)
    cenário_group.draw(janela)
    móveis_group.draw(janela)
    pygame.display.flip()
