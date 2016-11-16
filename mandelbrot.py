#graph

import pygame, sys, math
pygame.init()

font1 = pygame.font.SysFont('Verdana', 16)
font2 = pygame.font.SysFont('Serif', 24)
font3 = pygame.font.SysFont('Serif', 14)
white = (255,255,255)
black = (0,0,0)
colour = (200,0,200)

width, height = 800, 800
extraW = 400
screen = pygame.display.set_mode((width+extraW, height))
pygame.display.set_caption("Peter's grapher")
screen.fill(white)

def graphSet():
    point = pygame.PixelArray(screen)
    for x0 in range(width):
        for y0 in range(height):
            x = (x0 - float(width)/2-100)/300
            y = (y0 - float(height)/2)/300

            cx, cy = x, y
            for n in range(200):
                mx = x*x-y*y+cx
                my = 2*x*y + cy
                x, y = mx, my
                a = abs(x + y)
                if a > 100:
                    break
            if a <= 2:
                point[x0,y0] = (0,0,200)
            

def graphMain():
    global k
    k = 25
    title = font2.render("The Mandelbrot Set",1,black)
    subTitle = font3.render("by Peter Halldestam", 1, black)
    text = pygame.image.load('mathtext.png')
 
        
    screen.blit(title,(width+extraW-300,20))
    screen.blit(subTitle,(width+extraW-260, 60))
    screen.blit(text, (width+extraW-380, 100))
    graphSet()
    pygame.draw.rect(screen,black, (0,0,width,height),10)
    active = True
    while active:
        pygame.display.update()

        #user input, events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    graphMain()
