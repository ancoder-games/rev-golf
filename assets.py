import pygame as pg

pg.font.init()

FONT = pg.font.SysFont("segoeuisymbol", 48) 

BALL = pg.Surface((40, 40), pg.SRCALPHA)
# BALL.fill((255, 255, 255))
# BALL.set_colorkey((255, 255, 255))
pg.draw.aacircle(BALL, (0, 0, 0), (20, 20), 19)

INVERSE_BALL = pg.Surface((30, 30), pg.SRCALPHA)
# BALL.fill((255, 255, 255))
# BALL.set_colorkey((255, 255, 255))
pg.draw.aacircle(INVERSE_BALL, (255, 255, 255), (15, 15), 14)

ARROW = pg.Surface((100, 40), pg.SRCALPHA)
# ARROW.fill((255, 0, 0, 0))
# ARROW.fill((255, 255, 255))
# ARROW.set_colorkey((255, 255, 255))
ARROW.blit(FONT.render("➜", True, (0, 0, 0)), (50, -15))

bg = pg.image.load("assets/background.png")
BACKGROUND = pg.Surface(bg.get_size(), pg.SRCALPHA)
BACKGROUND.fill((50, 168, 82))
BACKGROUND.blit(bg, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

TITLE_SCREEN = pg.image.load("assets/title_screen.png")