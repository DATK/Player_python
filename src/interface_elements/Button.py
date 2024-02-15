import pygame as pg
class Button:

    def __init__(self, x: int, y: int, width: int, height: int, images_pathes: tuple, text=None, function=None, isPressed=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.images_pathes = images_pathes
        self.function = function
        self.isPressed = isPressed
        if self.images_pathes!=():      
            self.img1 = pg.image.load(self.images_pathes[0])
            self.img1 = pg.transform.scale(self.img1, (self.width, self.height))
            self.img1.set_colorkey((255, 255, 255))
            self.img1_rect = self.img1.get_rect(topleft=(self.x,self.y))

            self.img2 = pg.image.load(self.images_pathes[1])
            self.img2 = pg.transform.scale(self.img2, (self.width, self.height))
            self.img2.set_colorkey((255, 255, 255))
        else:
            self.zone=pg.Surface((self.x,self.y))
            self.zone=pg.transform.scale(self.zone,(self.width,self.height))
            self.zone_rect=self.zone.get_rect(topleft=(self.x,self.y))
            
            
    def show(self, scr):
        self.curret_img = self.img2 if self.isPressed else self.img1
        scr.blit(self.curret_img, self.img1_rect.topleft)

    def show_rect(self,scr,size=15,font="Comic Sans MS",aligin=(0,0),color=(0,0,0),color_backgroud=(255,255,255)):
        my_font =pg.font.SysFont(font, size)
        text_rnd=my_font.render(self.text,False,color)
        scr.blit(self.zone,self.zone_rect)
        scr.blit(text_rnd,self.zone.get_rect(topleft=aligin))       
    
    def changing(self, mouse_pos):
        self.isPressed = self.img1_rect.collidepoint(mouse_pos)

    def do_func(self,event):
        if self.function != None and self.isPressed and event.type==pg.MOUSEBUTTONDOWN and event.button==1:
            self.function()

