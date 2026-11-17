###Main Game file
import pygame
import os
import numpy as np
from pygame import gfxdraw

### Init pygame
pygame.init()

### Define the color library (if you wish)

### Define the window
class game1:
    def __init__(self):
        self.setDefaultConfig()

    def setDefaultConfig(self):
        ### Set the general default configurations for the canvas
        self.width=750
        self.height=750
        self.bg_color = (145,145,145) ###Use RGB Codes

        ### Set the fps, zoom level, and offset
        self.fps=120
        self.zoom=5
        self.offset=(0,0)

        ### This sets the default mouse position; make random position
        self.mouseLast=(0,0)
        
        ### This sets the mouse down state; is the mouse pressed or not?
        self.mouseDown = False

    ### Set the background color thru codes.  
    def background(self, rC, gC, bC):
        self.screen.fill((rC,gC,bC))

    def drawStatus(self):
        textFPS=self.text_font.render(f't={20.0:.5}', False, (0,0,0))
        textFRC=self.text_font.render(f'n={1000}', False, (0, 0, 0))
        self.screen.blit(textFPS, (0, 0))
        self.screen.blit(textFRC, (100, 0))

    def draw(self):
        ###Fill the background
        self.background(self.bg_color[0], self.bg_color[1], self.bg_color[2])
        #self.drawStatus()

    def gameLoop(self, loop=None):
        self.screen=pygame.display.set_mode((self.width, self.height))
        ###set bounding box for movement
        screenRect=self.screen.get_rect()

        flags=pygame.SCALED
        pygame.display.flip()
        clock = pygame.time.Clock()
        pygame.font.init()
        self.text_font = pygame.font.SysFont('Console', 16)

        ### Define player obj
        box=pygame.Rect(150,150,35,35)
        held=False
        boxOffsetX=0
        boxOffsetY=0

        running = True
        while running:
            self.draw()
            
            for event in pygame.event.get():
                #### Quit program if window is closed
                if event.type == pygame.QUIT:
                    running = False 
                    
                # Handle mouse events
                
                elif event.type == pygame.MOUSEBUTTONDOWN: ###If any mouse buttons are clicked/pressed.
                    ### If mouse button down
                    if event.button == 1:
                        #### Left click
                        x, y = pygame.mouse.get_pos()
                        x0, y0 = self.offset
                        self.mouseLast = (x-x0*self.zoom, y-y0*self.zoom)
                        self.mouseDown = True

                        ###Checks if player char is in line with everybody else
                        if box.collidepoint(event.pos):
                            held=True
                            mouseX,mouseY=event.pos
                            boxOffsetX=box.x-mouseX
                            boxOffsetY=box.y-mouseY
                        
                    if event.button == 4:
                        #### Mouse wheel up
                        self.zoom *=  (self.zoom**2+self.zoom/4+1) / (self.zoom**2+1)
                        
                    if event.button == 5:
                        ### Mouse wheel down
                        self.zoom *= (self.zoom**2+1) / (self.zoom**2+self.zoom/4+1)
                        
                elif event.type == pygame.MOUSEMOTION and held is not False:
                    #### Drag the box with the miuse
                    if self.mouseDown and held==True:
                        mouseX,mouseY=pygame.mouse.get_pos()
                        box.x=mouseX+boxOffsetX
                        box.y=mouseY+boxOffsetY
                        box.clamp_ip(screenRect)
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False
                    held=False
            
            ###redraw the rectangle in its new position frame by frame and updat time and speeds, etc. 
            pygame.draw.rect(self.screen,(255, 0, 0),box)
            pygame.display.flip()
            clock.tick(self.fps)



if __name__=='__main__':
    g=game1()
    g.gameLoop()
