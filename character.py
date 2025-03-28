import pygame
class Character():
    def __init__(self,x,y):
        self.rect=pygame.Rect((x,y,80,180))
        self.velocity_y=0
        self.jumping=False
        self.attack_type=0
    def draw(self,surface):
        pygame.draw.rect(surface,(0,255,0),self.rect)

    def move(self,screen_width,screen_height,surface):
        CHARACTER_SPEED=10
        CHARACTER_GRAVITY=2
        move_x=0
        move_y=0
         
        key=pygame.key.get_pressed()
        if key[pygame.K_a]:
            move_x= -CHARACTER_SPEED
        if key[pygame.K_d]:
            move_x= +CHARACTER_SPEED

        if key[pygame.K_w] and self.jumping == False:
            self.velocity_y=-30
            self.jumping=True
        self.velocity_y+=CHARACTER_GRAVITY
        if key[pygame.K_r] or key[pygame.K_t]:
            self.attack(surface)
            if key[pygame.K_r]:
                self.attack_type=1
            if key[pygame.K_r]:
                self.attack_type=2           
        move_y+=self.velocity_y
        if self.rect.left+move_x<0:
            move_x=-self.rect.left
        if self.rect.right+move_x>screen_width:
            move_x=screen_width-self.rect.right 

        if self.rect.bottom+move_y>screen_height-220:
            self.velocity_y=0
            self.jumping=False
            move_y=screen_height-220-self.rect.bottom           


        self.rect.x+=move_x
        self.rect.y+=move_y
    def attack(self,surface):
        attacking_rectangle=pygame.Rect(self.rect.centerx,self.rect.y,2*self.rect.width,self.rect.height)
        if attacking_rectangle.colliderect()
        pygame.draw.rect(surface,(255,0,0),attacking_rectangle)