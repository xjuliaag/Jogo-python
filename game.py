from random import randint
import pygame
from pygame import display
from pygame.image import load
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame.time import Clock
from pygame import font

pygame.init()

#Som inicio
pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('musica.wav')
pygame.mixer.music.play(-1)

acerto_vacina = pygame.mixer.Sound('musica_acerto.wav')
acerto_vacina.set_volume(0.8)
#Som fim

tamanho = 800, 600
fonte = font.SysFont('arial', 25)
fonte_perdeu = font.SysFont('arial', 80)

superficie = display.set_mode(
    size=tamanho
)
fundo = load('fundobonito.jpg')
display.set_caption(
    'Vacina VS Vírus'
)

class ZeGotinha(Sprite):
    def __init__(self, vacina):
        super().__init__()

        self.image = load('zegotinha.png')
        self.rect = self.image.get_rect()
        self.vacina = vacina
        self.velocidade = 4

    def jogar_vacina(self):
        if len(self.vacina) < 10:
            self.vacina.add(
                Vacina(*self.rect.center)
            )

    def update(self):
        keys = pygame.key.get_pressed()

        vacina_fonte = fonte.render(
            f'Vacinas : {10 - len(self.vacina)}',
            True,
            (255, 255, 255)
        )
        superficie.blit(vacina_fonte, (10, 10))

        if keys [pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys [pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys [pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
                self.rect.y += self.velocidade

class Vacina(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load('vacina.png')
        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        self.rect.x += 1

        if self.rect.x > tamanho[0]:
            self.kill()


class Virus(Sprite):
    def __init__(self):
        super().__init__()

        self.image = load('virus.png')
        self.rect = self.image.get_rect(
            center=(800, randint(60, 580))
        )

    def update(self):
        self.rect.x -= 0.1

        if self.rect.x == 0:
            self.kill()
            global perdeu
            perdeu = True


grupo_inimigos = Group()
grupo_vacina = Group()
zegotinha = ZeGotinha(grupo_vacina)
grupo_zegotinha = GroupSingle(zegotinha)

grupo_inimigos.add(Virus())

clock = Clock()
mortes = 0
round = 0
perdeu = False

while True:
    clock.tick(120)

    if round % 120 == 0:
        if mortes < 20:
            grupo_inimigos.add(Virus())
        for _ in range(int(mortes / 20)):
            grupo_inimigos.add(Virus())
    print(mortes)
    #Eventos
    for evento in event.get():
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_SPACE:
                zegotinha.jogar_vacina()
    if groupcollide(grupo_vacina, grupo_inimigos, True, True):
        mortes += 1
        acerto_vacina.play()

    #Display
    superficie.blit(fundo, (0, 0))

    fonte_mortes = fonte.render(
        f'Mortes : {mortes}',
        True,
        (255, 255, 255)
    )

    superficie.blit(fonte_mortes, (10, 35))
    grupo_zegotinha.draw(superficie)
    grupo_inimigos.draw(superficie)
    grupo_vacina.draw(superficie)

    grupo_zegotinha.update()
    grupo_inimigos.update()
    grupo_vacina.update()

    if perdeu:
        fim = fonte_perdeu.render(
            'Você perdeu!',
            True,
            (255,0,0)
        )
        superficie.blit(fim, (170, 100))
        display.update()
        pygame.time.delay(1000)

    round += 1
    display.update()
