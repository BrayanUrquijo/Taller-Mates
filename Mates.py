import pygame as pg

#iniciamos pygame

pg.init()

#creamos la pantalla

pantalla = pg.display.set_mode((800, 600))

#titulo de la ventana

pg.display.set_caption("The God of Math")

#bucle principal

run = True

while run == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
pg.quit() #cerramos pygame


