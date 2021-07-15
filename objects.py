import pygame
from typing import List
import random

clr = "#ff0000"
clrs = ["#ff0000", "#ffffff", "#4200ff", "#21813b", "#8a5c15", "#1cec6b", "#bf13d7", "#000000", "#ff0049"]


class Colliders:
    collider_objects = []
    collider_width = 40
    x_ptr = 0     # position where the first bar should be rendered
    velocity = 3

    def __init__(self, currency: str, crypto_data: List[float]) -> None:
        self.barHeights = crypto_data
        self.currency = currency
        self.clr_list = [ clrs[random.randint(0, len(clrs)-1)] for x in crypto_data ]
        self.barHeightsNormalized = crypto_data

    def normalize(self):
        """
        Function is used to normalized the bitcoin data
        for scaling it down to pixel levels
        """
        norm_value = 60 if self.currency == "btc" else 18
        self.barHeightsNormalized = [heights / norm_value for heights in self.barHeights]

    def override_width(self, w):
        self.collider_width = w

    def render(self, screen, screen_height, screen_width):
        w = 20
        offset_y = 400
        x_ptr = self.x_ptr
        for i in range(len(self.barHeights)):
            # calculate x and y co-ordinates for rendering object
            y_cor = (screen_height - self.barHeightsNormalized[i]) + offset_y if self.currency == 'btc' else 0

            x_cor = x_ptr
            x_ptr += self.collider_width  # next object should render current + width pixels away
            pygame.draw.rect(screen, self.clr_list[i], [x_cor, y_cor, self.collider_width, self.barHeightsNormalized[i]])
        self.x_ptr -= self.velocity
