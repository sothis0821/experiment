import pygame
from pygame.locals import *
import sys
import time
from chess_board import chess_board


class GUI(object):
    def __init__(self, cboard):
        pygame.init()
        pygame.display.set_caption("Cell Game(Remerber to press space key)")
        self.faint_yellow = (255, 238, 147)
        self.salmon_pink = (255, 192, 159)
        self.white = (255, 255, 255)
        self.font_one = pygame.font.Font(None, 100)
        self.font_two = pygame.font.Font(None, 40)
        self.font_three = pygame.font.Font(None, 60)
        self.game_name = self.font_one.render("Cell Game", True, self.white)
        self.operation_instruction = self.font_three.render("Press Space Key to Start and Update",
                                                              True, self.white)
        self.author = self.font_two.render("Created by Ruan Bin, Cheng Tong, Li Chenglong", True, self.white)
        self.lx = 5
        self.ly = 5
        self.xlen = 800 / cboard.length
        self.ylen = 800 / cboard.length
        self.cboard = cboard
        self.screen = pygame.display.set_mode([2 * self.lx + 800, 2 * self.ly + 800])

    def display(self):
        """display on screen for 20 times"""
        self.screen.blit(self.game_name, (220, 100))
        self.screen.blit(self.operation_instruction, (40, 600))
        self.screen.blit(self.author, (90, 200))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        self.draw_once()
                        self.cboard.update_chess_board()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

    def draw_once(self):
        """draw on the screen once"""
        for i in range(self.cboard.length):
            for j in range(self.cboard.length):
                if self.cboard.cells[i][j].status:
                    pygame.draw.rect(self.screen, self.salmon_pink,
                                     [i * self.xlen + self.lx, j * self.ylen + self.ly, self.xlen, self.ylen])
                else:
                    pygame.draw.rect(self.screen, self.faint_yellow,
                                     [i * self.xlen + self.lx, j * self.ylen + self.ly, self.xlen, self.ylen])
            pygame.display.update()
