#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        print('Setup Start')
        print('Setup End')

        print('Loop Start')
        # Criamos o menu passando a nossa janela para ele
        menu = Menu(self.window)

        while True:
            # Executa o código do menu (desenha o fundo na tela)
            menu.run()

