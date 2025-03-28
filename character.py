import pygame
class Character():
    def __init__(self,x,y,flip,data,sprite_sheet,animation_steps):
        self.size=data[0]
        self.image_scale=data[1]
        self.offset=data[2]
        self.animation_list=self.load_images(sprite_sheet,animation_steps)
        self.action_list={"idle":0,"moving":1,"jumping":2,"attack1":3,"attack2":4,"hit":5,"death":6}
        self.action=0
        self.frame_index=0
        self.image=self.animation_list[self.action][self.frame_index]
        self.rect=pygame.Rect((x,y,80,180))
        self.velocity_y=0
        self.jumping=False
        self.running=False
        self.attack_type=0
        self.attacking=False
        self.health=100
        self.flip=flip
        self.update_time=pygame.time.get_ticks()


    def load_images(self,sprite_sheet,animation_steps):
        animation_list=[]
        for y,animation in enumerate(animation_steps):
            temp_img_list=[]
            for x in range(animation):
                temp_img=sprite_sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size*self.image_scale,self.size*self.image_scale)))
            animation_list.append(temp_img_list)
        
        return animation_list    
    def draw(self,surface):
        rotating_img=pygame.transform.flip(self.image,self.flip,False)
        pygame.draw.rect(surface,(0,255,0),self.rect)
        surface.blit(rotating_img,(self.rect.x-(self.offset[0]*self.image_scale),self.rect.y-(self.offset[1]*self.image_scale)))

    def move(self,screen_width,screen_height,surface,target):
        CHARACTER_SPEED=10
        CHARACTER_GRAVITY=2
        move_x=0
        move_y=0
        self.running=False
        key=pygame.key.get_pressed()

        if self.attacking==False:
            if key[pygame.K_a]:
                self.running=True
                #self.action=self.action_list["moving"]
                move_x= -CHARACTER_SPEED
            if key[pygame.K_d]:
                self.running=True
                #self.action=self.action_list["moving"] 
                move_x= +CHARACTER_SPEED

            if key[pygame.K_w] and self.jumping == False:
                self.velocity_y=-30
                self.jumping=True
            self.velocity_y+=CHARACTER_GRAVITY
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface,target)
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
        if target.rect.centerx>self.rect.centerx:
            self.flip=False
        else:
            self.flip=True
        self.rect.x+=move_x
        self.rect.y+=move_y


    def update_character(self):
        animation_cooldown=50 #milliseconds
        self.image=self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks()-self.update_time>animation_cooldown:
            self.frame_index+=1
            self.update_time=pygame.time.get_ticks()
            if self.frame_index>=len(self.animation_list[self.action]):
                self.frame_index=0

    def attack(self,surface,target):
        self.attacking=True
        attacking_rectangle=pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip),self.rect.y,2*self.rect.width,self.rect.height)
        if attacking_rectangle.colliderect(target.rect):
            target.health-=10
        pygame.draw.rect(surface,(255,0,0),attacking_rectangle)

