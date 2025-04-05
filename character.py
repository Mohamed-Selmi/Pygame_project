import pygame
class Character():
    def __init__(self,player,x,y,flip,name,character_data):#data,sprite_sheet,animation_steps):
        self.player=player
        self.name=name
        self.size=character_data[0][0]
        self.image_scale=character_data[0][1]
        self.offset=character_data[0][2]
        self.sprite_sheet=character_data[1]
        self.animation_steps=character_data[2]
        self.animation_list=self.load_images(self.sprite_sheet,self.animation_steps)
        self.action_list={"idle":0,"moving":1,"jumping":2,"attack1":3,"attack2":4,"hit":5,"death":6}
        self.action=0
        self.frame_index=0
        self.image=self.animation_list[self.action][self.frame_index]
        self.rect=pygame.Rect((x,y,80,180))
        self.velocity_y=0
        self.jumping=False
        self.moving=False
        self.attack_type=0
        self.attack_cooldown=0
        self.attacking=False
        self.health=100
        self.alive=True
        self.flip=flip
        self.hit=False
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

    def move(self,screen_width,screen_height,surface,target,round_over):
        CHARACTER_SPEED=10
        CHARACTER_GRAVITY=2
        move_x=0
        move_y=0
        self.moving=False
        self.attack_type=0
        key=pygame.key.get_pressed()

        if self.attacking==False and self.alive==True and round_over==False:
            if self.player==1:
                if key[pygame.K_a]:
                    self.moving=True
                    #self.action=self.action_list["moving"]
                    move_x= -CHARACTER_SPEED
                if key[pygame.K_d]:
                    self.moving=True
                    #self.action=self.action_list["moving"] 
                    move_x= +CHARACTER_SPEED

                if key[pygame.K_w] and self.jumping == False:
                    self.velocity_y=-30
                    self.jumping=True
                self.velocity_y+=CHARACTER_GRAVITY
                if key[pygame.K_r] or key[pygame.K_t] and self.jumping==False:
                    
                    self.attack(surface,target)
                    if key[pygame.K_r]:
                        self.attack_type=1
                    if key[pygame.K_t]:
                        self.attack_type=2 
            if self.player==2:
                if key[pygame.K_LEFT]:
                    self.moving=True
                    #self.action=self.action_list["moving"]
                    move_x= -CHARACTER_SPEED
                if key[pygame.K_RIGHT]:
                    self.moving=True
                    #self.action=self.action_list["moving"] 
                    move_x= +CHARACTER_SPEED

                if key[pygame.K_UP] and self.jumping == False:
                    self.velocity_y=-30
                    self.jumping=True
                self.velocity_y+=CHARACTER_GRAVITY
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(surface,target)
                    if key[pygame.K_KP1]:
                        self.attack_type=1
                    if key[pygame.K_KP2]:
                        self.attack_type=2 
                        
        move_y+=self.velocity_y
        if self.rect.left+move_x<0:
            move_x=-self.rect.left
        if self.rect.right+move_x>screen_width:
            move_x=screen_width-self.rect.right 

        if self.rect.bottom+move_y>screen_height-90:
            self.velocity_y=0
            self.jumping=False
            move_y=screen_height-90-self.rect.bottom           
        if target.rect.centerx>self.rect.centerx:
            self.flip=False
        else:
            self.flip=True
        if self.attack_cooldown>0:
            self.attack_cooldown-=1
        self.rect.x+=move_x
        self.rect.y+=move_y

    def update_action(self,new_action):
        if new_action!=self.action:
            self.action=new_action
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()

    def update_character(self):
        animation_cooldown=50 #milliseconds
        if self.health<=0:
            self.health=0
            self.alive=False
            self.update_action(self.action_list["death"])
        elif self.hit==True:
            self.update_action(self.action_list["hit"])
        elif self.attacking==True:
            if self.attack_type==1:
                self.update_action(self.action_list["attack1"])
            elif self.attack_type==2:
                self.update_action(self.action_list["attack2"])
        elif self.jumping==True:
            self.update_action(self.action_list["jumping"])
        elif self.moving==True:
            self.update_action(self.action_list["moving"])
        else:
            self.update_action(self.action_list["idle"])
        self.image=self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks()-self.update_time>animation_cooldown:
            self.frame_index+=1
            self.update_time=pygame.time.get_ticks()
        if self.frame_index>=len(self.animation_list[self.action]):
            self.frame_index=0
            if self.action==self.action_list['attack1'] or self.action==self.action_list['attack2']:
                self.attacking=False
                self.attack_cooldown=20
            if self.action==self.action_list['hit']:
                self.hit=False
                self.attacking=False
                self.attack_cooldown=20
            if self.alive==False:
                self.frame_index=len(self.animation_list[self.action])-1

    def attack(self,surface,target):
        if self.attack_cooldown==0:
            self.attacking=True
            attacking_rectangle=pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip),self.rect.y,2*self.rect.width,self.rect.height)
            if attacking_rectangle.colliderect(target.rect):
                target.health-=50
                target.hit=True
            pygame.draw.rect(surface,(255,0,0),attacking_rectangle)


