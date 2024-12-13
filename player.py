
import pygame

class Player:
    def __init__(self, x: int, y:int, momentum: str) -> None:
        self.x = x
        self.y = y
        self.momentum = momentum 
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y

    def set_momentum(self, key: pygame.event, cur_momentum: str) -> None:
        if (key == pygame.K_UP or key == pygame.K_w) and cur_momentum != 'down':
            self.momentum = 'up'
            
        elif (key == pygame.K_DOWN or key == pygame.K_s) and cur_momentum != 'up':
            self.momentum = 'down'
            
        elif (key == pygame.K_LEFT or key == pygame.K_a) and cur_momentum != 'right':
            self.momentum = 'left'
            
        if (key == pygame.K_RIGHT or key == pygame.K_d) and cur_momentum != 'left':
            self.momentum = 'right'
            

    def move(self) -> None:
        if self.momentum == 'left':
            self.x -= 1 
        elif self.momentum == 'right':
            self.x += 1 
        elif self.momentum == 'up':
            self.y -= 1 
        elif self.momentum == 'down':
            self.y += 1 


