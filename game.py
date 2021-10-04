import os
import random

import pygame


class Game():

    def __init__(self):
        self.tune = ''
        self.inp = ''

    def get_tune(self):
        os.chdir('music')
        filename = random.choice(os.listdir())
        os.chdir("..")
        return filename

    def check_tune(self):
        return self.inp.lower() + '.mp3' == self.tune.lower()

    def start(self):
        self.tune = self.get_tune()
        pygame.mixer.init()
        pygame.mixer.music.load('music/' + self.tune)
        pygame.mixer.music.play()
        self.inp = input('Введите песню : ')
        print(self.inp)
        if self.check_tune():
            print('Вы угадали, это - ' + self.tune)
        else:
            print('Вы не угадали, это - ' + self.tune)
