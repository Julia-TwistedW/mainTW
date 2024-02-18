import pygame
import math
import numpy as np


class Game:
    def __init__(self):
        pygame.init()

        info = pygame.display.Info()
        self.display = pygame.display.set_mode((info.current_w - 100, info.current_h - 100), pygame.RESIZABLE)
        self.size = self.width, self.height = pygame.display.get_window_size()

        self.count_cell_in_row = 10
        self.cell_size = self.width / self.count_cell_in_row

        self.field = np.zeros((math.ceil(self.height / self.cell_size) + 1, self.count_cell_in_row + 1))

        self.colors = {"black": (0, 0, 0), "red": (255, 0, 0), "blue": (0, 0, 255), "green": (0, 255, 0),
                       "yellow": (255, 255, 0), "purple": (255, 0, 255)}

    def resize(self):
        self.size = self.width, self.height = pygame.display.get_window_size()
        self.cell_size = self.width / self.count_cell_in_row

        if self.field.size / self.count_cell_in_row < self.height / self.cell_size:
            self.field.resize((math.ceil(self.height / self.cell_size) + 1, self.count_cell_in_row + 1), refcheck=False)

    def paint_cell(self, event_click):
        if not event_click:
            return

        pos = event_click.pos
        x, y = round(pos[0] / self.cell_size), round(pos[1] / self.cell_size)

        if self.field[y][x] == 0:
            self.field[y][x] = 1
            return True
        return False

    def draw_field(self):
        self.display.fill((255, 255, 255))
        for x in range(self.count_cell_in_row):
            pygame.draw.line(self.display, (0, 0, 150), (x * self.cell_size, 0), (x * self.cell_size, self.height))

        for y in range(math.ceil(self.height / self.cell_size)):
            pygame.draw.line(self.display, (0, 0, 150), (0, y * self.cell_size), (self.width, y * self.cell_size))

    def draw_cells(self):
        first_player = np.argwhere(self.field == 1)
        second_player = np.argwhere(self.field == 2)
        players = [first_player, second_player]

        for player, color in zip(players, self.colors.values()):
            for i in player:
                y, x = i
                pygame.draw.circle(self.display, color, (x * self.cell_size, y * self.cell_size),
                                   self.cell_size // 8 - (self.cell_size // 8) % 4 + 4)

    def draw(self):
        self.draw_field()
        self.draw_cells()

    def start(self):
        while True:
            event_click = None
            for event in pygame.event.get():
                # match event.type:
                #     case pygame.QUIT: return pygame.quit()
                #     case pygame.WINDOWSIZECHANGED: self.resize()
                #     case pygame.MOUSEBUTTONUP: event_click = event
                if event.type == pygame.QUIT:
                    return pygame.quit()
                if event.type == pygame.WINDOWSIZECHANGED:
                    self.resize()
                if event.type == pygame.MOUSEBUTTONUP:
                    event_click = event

            self.paint_cell(event_click)
            self.draw()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.start()
