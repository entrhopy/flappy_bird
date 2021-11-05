import pygame
import random

from pygame.time import Clock

pygame.init()


#definizione variabili immagini
sfondo = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/sfondo.png')
uccello = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/uccello.png')
base = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/base.png')
gameover = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/gameover.png')
tubo_giu = pygame.image.load('/home/denis/Scrivania/VMShare/immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)


#disegno schermo
SCHERMO = pygame.display.set_mode((288,512))
#imposto fps
FPS = 50


#funzioni di gioco
def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(uccello, (uccellox, uccelloy))

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    

def inizializza():
    global uccellox, uccelloy, uccello_vely
    uccellox, uccelloy = 60, 150
    uccello_vely = 0

#inizializzo variabili globali: posizione uccello e velocità caduta
inizializza()

#ciclo principale
while True:
    #gravità
    uccello_vely += 1
    uccelloy += uccello_vely
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP ):
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()

    #aggiornamento schermo
    disegna_oggetti()
    aggiorna()

