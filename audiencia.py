import pygame
from pygame.locals import *
from engine import Game, Scene
from people import *
import random
import varitaje
import motor
peoplex,peopley = (55, 119)
filasx, filasy = (800/peoplex,600/peopley)

wardrobes = getAllWardrobes()
def buildIndividual():
    wd=random.choice(wardrobes)
    i= Individual(wd)
    i.random()
    return i

class Fila:
    sillas=None
    def __init__(self):
        if Fila.sillas is None:
            Fila.sillas = self.construirSillas()
        self.personas = [ buildIndividual().render() for x in range(filasx) ]

    def construirSillas(self):
        img = pygame.image.load('escenario/butaca.png')
        img.convert_alpha()
        base = pygame.Surface((800, peopley), 0, img)
        for x in range(filasx):
            base.blit(img, (peoplex * x, 0) )
        return base

    def render(self, surface, (dx,dy), porcentaje ):
        surface.blit(Fila.sillas, (dx,dy))
        print porcentaje
        for x, persona in enumerate(self.personas):
            if random.randint(0,1000)<porcentaje:
                gx = random.choice([-1,0,1])
                gy = random.choice([-1,-2,0])
            else:
                gx, gy = 0,0
            surface.blit(persona, ((x*peoplex)+dx+gx, dy+gy))


class Audiencia:
    def __init__(self):
        self.filas = [ Fila() for y in range(filasy) ]
        self.fg = pygame.image.load("escenario/foreground.png")
        self.fg.convert()
        self.mano = pygame.image.load("escenario/manos/mano1.png")
        self.mano.convert()
        self.varitaje = varitaje.Varitaje()

    def render(self, surface, porcentaje):
        for y,fila in enumerate(self.filas):
            dx = (y%2) * peoplex/2 - peoplex/2 + 6
            dy = peopley/2 * y
            fila.render(surface, (dx,dy), porcentaje)
        surface.blit(self.fg, (0,0))
        surface2 = surface.subsurface(pygame.Rect(0,0,800,525))
        surface2.blit(self.mano, self.mano.get_rect(center=self.varitaje.nextpos()))

class AudienciaScene(Scene):
    def init(self):
        import sounds
        self.sounds = sounds
        self.finalizar = False
        self.audiencia = Audiencia()
        self.calor = 0

    def event(self, evt):
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE:
                self.end()
            elif evt.key == K_RETURN:
                self.finalizar = True
                
    def gameEvent(self, evt):
        if evt == motor.Eventos.PALOK:
            self.sounds.bravo.play()
        elif evt == motor.Eventos.PALMAL:
            self.sounds.abucheo.play()
        elif evt == motor.Eventos.OK_DEUNA:
            self.sounds.bravo2.play()
        elif evt == motor.Eventos.MAL:
            self.sounds.abucheo2.play()
        
    def setCalor(self, calor):
        self.calor = calor
    
    def loop(self):
        # aca updateamos el mundo cada paso
        
        
        if self.finalizar:
            self.end( )
                    
    def update(self):
        global iLayers
        self.game.screen.fill((0,0,0))
        self.audiencia.render(self.game.screen, abs(self.calor)*100)

    def setVoluntario(self, voluntario, hacerPuff):
        """cambia el voluntario. Si hacerPuff es true, entonces baja la varita y hace aparecer el humito"""
        self.voluntario = voluntario

    def tomateame(self):
        pass
        
if __name__ == "__main__":
    g = Game(800, 600, framerate = 200)
    g.run( AudienciaScene(g) )
