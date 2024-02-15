import pygame as pg


class Label:
    
    def __init__(self,x,y,weight,height,text="Label1",img_path=None):
        self.x=x
        self.y=y
        self.weight=weight
        self.height=height
        self.text=text
        self.img_path=img_path 
        if img_path!=None:
            self.zone= pg.image.load(self.img_path)
            self.zone=pg.transform.scale(self.zone,(self.weight,self.height))
            self.zone_rect=self.zone.get_rect(topleft=(self.x,self.y))
        else:
            self.zone=pg.Surface((self.x,self.y))
            self.zone=pg.transform.scale(self.zone,(self.weight,self.height))
            self.zone_rect=self.zone.get_rect(topleft=(self.x,self.y))
        
    def show(self,scr,color_background=(0,0,0),font="Comic Sans MS",size=25,aligin=(0,0),color=(255,255,255)):
        my_font =pg.font.SysFont(font, size)
        self.zone.fill(color_background)
        text_rnd=my_font.render(self.text,False,color)
        scr.blit(self.zone,self.zone_rect)
        scr.blit(text_rnd,self.zone.get_rect(topleft=aligin))       
            