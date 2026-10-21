from dataclasses import dataclass
from assets import BACKGROUND
from src.components.transform import  Scale
import esper
import pygame as pg
from src.components.rendering import Sprite
from src.components.transform import Position

@dataclass
class RenderProcessor(esper.Processor):
    screen: pg.Surface

    def process(self, dt: float):
        self.screen.blit(BACKGROUND)
        
        for e, sprite in esper.get_component(Sprite):
            target: tuple[float, float, float, float] = (0, 0, *sprite.image.size)
            
            pos = esper.try_component(e, Position)
            if pos:
                target = (pos.x, pos.y, *sprite.image.size)
            
            scale = esper.try_component(e, Scale)
            if scale:
                target = (target[0], target[1], sprite.image.size[0] * scale.x, sprite.image.size[1] * scale.y)
            
            self.screen.blit(sprite.image, target)