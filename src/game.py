import pygame as pg
import esper

from assets import BALL, INVERSE_BALL
from src.processors.game import GameProcessor
from src.components.ball import Arrow, Ball, InvBall
from src.components.rendering import Sprite
from src.components.transform import Position
from src.processors.rendering import RenderProcessor

pg.init()

screen = pg.display.set_mode((640, 480))

esper.add_processor(RenderProcessor(screen))
esper.add_processor(GameProcessor(screen))

esper.create_entity(Position(320 - 20, 240 - 20), Sprite(BALL), Ball(pg.Vector2(0, 0), -90, 0))
esper.create_entity(Position(320 - 20, 240 - 20), Arrow())
esper.create_entity(Position(100, 100), InvBall(), Sprite(INVERSE_BALL))

clock = pg.time.Clock()
dt = 0.1
running = True
while running:
    screen.fill((255, 255, 255))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    esper.process(dt)
    pg.display.flip()
    dt = clock.tick(0) / 1000
    dt = max(0.001, min(0.1, dt))

pg.quit()