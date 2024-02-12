import pygame as pg
import os
from random import randint
pg.init()


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
        if len(self.images_pathes) != 2:
            raise RuntimeError
        self.img1 = pg.image.load(self.images_pathes[0])
        self.img1 = pg.transform.scale(self.img1, (self.width, self.height))
        self.img1.set_colorkey((255, 255, 255))
        self.img1_rect = self.img1.get_rect(topleft=(self.x,self.y))

        self.img2 = pg.image.load(self.images_pathes[1])
        self.img2 = pg.transform.scale(self.img2, (self.width, self.height))
        self.img2.set_colorkey((255, 255, 255))
        
    def show(self, scr):
        self.curret_img = self.img2 if self.isPressed else self.img1
        scr.blit(self.curret_img, self.img1_rect.topleft)

    def changing(self, mouse_pos):
        self.isPressed = self.img1_rect.collidepoint(mouse_pos)

    def do_func(self,event):
        if self.function != None and self.isPressed and event.type==pg.MOUSEBUTTONDOWN and event.button==1:
            self.function()


class Player:

    def __init__(self) -> None:
        self.path = "./src/music"
        self.songs = []
        self.get_sound()
        self.n_sound = 0
        self.snd = pg.mixer.Sound(
                f"{self.path}/{self.songs[self.n_sound]}")
        self.playing = False
    
    def plad(self):
        if not self.playing:
            self.playing = True
            self.snd = pg.mixer.Sound(
                f"{self.path}/{self.songs[self.n_sound]}")
            self.snd.play()
        else:
            self.playing = False
            self.snd.stop()
    
    def next(self):
        self.n_sound += 1
        self.playing = False
        if self.n_sound > len(self.songs)-1:
            self.n_sound = 0
        self.snd.stop()
        self.plad()
        
    
    def next_minus(self):
        self.n_sound += -1
        self.playing = False
        if self.n_sound<0:
            self.n_sound=len(self.songs)-1
        self.snd.stop()
        self.plad()
        
        
    def load_music(self, path, name="song.mp3"):
        if ''.join(name[-4:]) != ".mp3":
            return 0

        with open(path, "rb") as f:
            data = f.read()

        with open(f"./src/music/{name}", "wb") as f:
            f.write(data)
        self.get_sound()

    def get_sound(self):
        sng = os.listdir(self.path)
        self.songs = []
        for i in sng:
            if i[-4:] == ".mp3":
                self.songs.append(i)
            else:
                continue

    def mixing(self):
        self.songs = [self.songs[randint(0, len(self.songs)-1)]
                      for _ in self.songs]
        self.snd.stop()
        self.playing = False
        self.plad()


class Window:

    def __init__(self) -> None:
        self.screen = pg.display.set_mode((400, 400))
        self.player = Player()
        self.clock = pg.time.Clock()
        self.button_start = Button(
            10, 10, 70, 60, ("./src/img/img1.png", "./src/img/img2.png"), function=self.player.plad)
        self.button_next = Button(
            80, 80, 80, 80, ("./src/img/img3.png", "./src/img/img4.png"), function=self.player.next)
        self.button_next_minus = Button(
            160, 160, 80, 80, ("./src/img/img5.png", "./src/img/img6.png"), function=self.player.next_minus)
        self.button_mix = Button(
            300, 160, 80, 80, ("./src/img/img7.png", "./src/img/img8.png"), function=self.player.mixing)

    def run(self):
        while True:
            self.screen.fill((230, 245, 27))
            self.button_start.show(self.screen)
            self.button_next.show(self.screen)
            self.button_next_minus.show(self.screen)
            self.button_mix.show(self.screen)
            for event in pg.event.get():
                self.button_start.changing(pg.mouse.get_pos())
                self.button_next.changing(pg.mouse.get_pos())
                self.button_mix.changing(pg.mouse.get_pos())
                self.button_next_minus.changing(pg.mouse.get_pos())
                self.button_start.do_func(event)
                self.button_next_minus.do_func(event)
                self.button_next.do_func(event)
                self.button_mix.do_func(event)
                if event.type == pg.QUIT:
                    exit()
            pg.display.flip()
            self.clock.tick(60)


app = Window()

app.run()
