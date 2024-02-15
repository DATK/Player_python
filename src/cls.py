import pygame as pg
import os
from interface_elements.Button import Button
from random import randint
from interface_elements.Label import Label
pg.init()


class Player:

    def __init__(self) -> None:
        self.path = "./src/music"
        self.songs = []
        self.get_sound()
        self.n_sound = 0
        self.snd = pg.mixer.Sound(
            f"{self.path}/{self.songs[self.n_sound]}")
        self.playing = False
        self.agn = False

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
        if self.n_sound < 0:
            self.n_sound = len(self.songs)-1
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

    def again(self):
        self.again = True

    def get_sound(self):
        sng = os.listdir(self.path)
        self.songs = []
        for i in sng:
            if i[-4:] == ".mp3":
                self.songs.append(i)
            else:
                continue

    def mixing(self):
        nmbrs = []
        songs = []
        ln = len(self.songs)-1
        i = 0
        while i <= ln:
            a = randint(0, ln)
            if a in nmbrs:
                continue
            else:
                nmbrs.append(a)
                songs.append(self.songs[a])
                i += 1
        self.songs = songs
        self.snd.stop()
        self.playing = False
        self.plad()


class Window:

    def __init__(self) -> None:
        self.screen = pg.display.set_mode((400, 400))
        self.player = Player()
        self.clock = pg.time.Clock()
        self.img_pacs = (("./src/img/img1.png", "./src/img/img2.png"), ("./src/img/img3.png",
                    "./src/img/img4.png"), ("./src/img/img5.png", "./src/img/img6.png"), ("./src/img/img7.png", "./src/img/img8.png"))
        self.button_start = Button(
            190, 65, 35, 35, self.img_pacs[0], function=self.player.plad)
        self.button_next = Button(
            280, 65, 35, 35, self.img_pacs[1], function=self.player.next)
        self.button_next_minus = Button(
            100, 65, 35, 35, self.img_pacs[2], function=self.player.next_minus)
        self.button_mix = Button(
            190, 105, 35, 35, self.img_pacs[3], function=self.player.mixing)
        self.label1 = Label(0, 0, 400, 50,text="It music python player")

    def buttons_init(self):
        self.button_start.show(self.screen)
        self.button_next.show(self.screen)
        self.button_next_minus.show(self.screen)
        self.button_mix.show(self.screen)

    def labels_init(self):
        self.label1.show(self.screen, size=15, aligin=(120, 15
                                                       ), color=(50, 120, 0), color_background=(40, 60, 80))

    def button_anim_func(self, event):
        self.button_start.changing(pg.mouse.get_pos())
        self.button_next.changing(pg.mouse.get_pos())
        self.button_mix.changing(pg.mouse.get_pos())
        self.button_next_minus.changing(pg.mouse.get_pos())
        self.button_start.do_func(event)
        self.button_next_minus.do_func(event)
        self.button_next.do_func(event)
        self.button_mix.do_func(event)

    def run(self):
        while True:
            self.screen.fill((200, 200, 200))
            self.buttons_init()
            self.labels_init()
            for event in pg.event.get():
                self.button_anim_func(event)
                if event.type == pg.QUIT:
                    exit()
            pg.display.flip()
            self.clock.tick(60)


app = Window()

app.run()
