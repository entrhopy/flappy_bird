import pygame
import random

pygame.init()


# definizione variabili immagini
sfondo = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/sfondo.png')
uccello = pygame.image.load(
    '/home/denis/Scrivania/VMShare/immagini/uccello.png')
base = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/base.png')
gameover = pygame.image.load(
    '/home/denis/Scrivania/VMShare/immagini/gameover.png')
tubo_giu = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)


# disegno schermo
SCHERMO = pygame.display.set_mode((288, 512))
# imposto fps
FPS = 50
# vel di avanz
VEL_AVANZ = 3


# classe tubi
class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75, 150)

    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x,self.y+210))
        SCHERMO.blit(tubo_su, (self.x,self.y-210))



# funzioni di gioco

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0, 0))
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox, uccelloy))
    SCHERMO.blit(base, (basex, 400))


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi

    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())


def hai_perso():
    SCHERMO.blit(gameover, (50, 180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()


# inizializzo variabili globali: posizione uccello e velocità caduta
inizializza()

# ciclo principale
while True:
    basex -= VEL_AVANZ
    if basex < -45:
        basex = 0
    # gravità
    uccello_vely += 1
    uccelloy += uccello_vely

    # comandi
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_UP):
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()
    if tubi[-1].x < 150: tubi.append(tubi_classe())
    #collisione con base
    if uccelloy > 380:
        hai_perso()
    # aggiornamento schermo
    disegna_oggetti()
    aggiorna()
