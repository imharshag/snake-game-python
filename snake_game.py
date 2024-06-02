import pygame
import random
from enum import Enum
pygame.init()

class Direction(Enum):
    RIGHT=1
    LEFT=2
    UP=3
    DOWN=4

class SnakeGame:

    def __init__(self,w=640,h=480): #screen size in pixels
        self.w=w
        self.h=h

        #init display
        self.dispaly=pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Snake') #setting title
        self.clock=pygame.time.Clock()

        #init game state
        self.direction=""

    def play_step(self):
        pass



if __name__=='__main__':
    game= SnakeGame()
 
    while True:
        game.play_step()


    #break if game over

        pygame.quit()

