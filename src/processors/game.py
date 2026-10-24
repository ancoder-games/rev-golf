from dataclasses import dataclass
from math import cos, pi, sin
from random import randrange
from assets import ARROW, FONT, TITLE_SCREEN
from src.components.ball import Arrow, Ball, InvBall
import esper
from src.components.transform import Position
import pygame as pg

def move_towards(current: float, target: float, step: float) -> float:
  if abs(target - current) <= step:
    return target
  return current + step if target > current else current - step

def bounce(velocity: pg.Vector2, normal: pg.Vector2) -> float:
    return velocity.reflect(normal).as_polar()[1]

@dataclass
class GameProcessor(esper.Processor):
    screen: pg.Surface
    game: bool = False
    button = pg.Rect(235, 323, 170, 63)
    level = 1
    shot = 0

    def main_menu(self):
        self.screen.blit(TITLE_SCREEN)
        if self.button.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0]:
                self.game = True

    def process(self, dt: float):
        if not self.game:
            self.main_menu()
            return
        
        b_pos: Position | None = None
        b: Ball | None = None
        ipos: Position | None = None

        for e, _ in esper.get_component(InvBall):
            ipos = esper.try_component(e, Position)

        for e, ball in esper.get_component(Ball):
            b = ball
            ball.velocity = pg.Vector2(cos(ball.rotation * (pi / 180)), sin(ball.rotation * (pi / 180))) * ball.speed
            if ball.speed >= 0:
                ball.speed -= ball.decceleration * dt
                ball.speed = max(0, ball.speed)
            pos = esper.try_component(e, Position)
            b_pos = pos
            
            if ipos and pos:
                if (pg.Vector2(ipos.x, ipos.y) - pg.Vector2(pos.x, pos.y)).length_squared() < 20*20:
                    ball.speed = 0
                    ball.velocity = pg.Vector2(0, 0)
                    self.level += 1
                    self.shot = 0
                    ipos.x = randrange(0, 640 - 40)
                    ipos.y = randrange(0, 480 - 40)
                    pos.x = 640/2
                    pos.y = 480/2

            keys = pg.key.get_pressed()
            
            if ball.speed == 0:
                if keys[pg.K_LEFT]:
                    ball.rotation -= dt * 160
                if keys[pg.K_RIGHT]:
                    ball.rotation += dt * 160
                if keys[pg.K_UP]:
                    ball.strength += 2 * dt
                if keys[pg.K_DOWN]:
                    ball.strength -= 2 * dt
                if keys[pg.K_SPACE]:
                    ball.speed = 200 * ball.strength
                    self.shot += 1

                ball.strength = min(max(ball.strength, 1), 3)

            if pos:
                pos.x += ball.velocity.x * dt
                pos.y += ball.velocity.y * dt
                # pos.x = pg.math.clamp(pos.x, -10, 640 - 30)
                # pos.y = pg.math.clamp(pos.x, -10, 480 - 30)
                if pos.x >= 640 - 40:
                    # ball.rotation += 90
                    ball.rotation = bounce(ball.velocity, pg.Vector2(-1, 0))
                if pos.x <= 0:
                    # ball.rotation += 90
                    ball.rotation = bounce(ball.velocity, pg.Vector2(1, 0))
                if pos.y >= 480 - 40:
                    # ball.rotation += 90
                    ball.rotation = bounce(ball.velocity, pg.Vector2(0, -1))
                if pos.y <= 0:
                    # ball.rotation += 90
                    ball.rotation = bounce(ball.velocity, pg.Vector2(0, 1))
    
        for e, arrow in esper.get_component(Arrow):
            center = pg.Vector2(324, 240)
            sp: pg.Surface
            if b:
                sp = pg.transform.scale(ARROW, (100 * b.strength, 40 * b.strength))
            else:
                sp = ARROW
            if b:
                arrow.rotation = b.rotation
            if b_pos:
                center.x = b_pos.x + 20
                center.y = b_pos.y + 20
            direction = pg.Vector2(1, 0).rotate(arrow.rotation)
            arrow_center = center + direction * 40
            if b:
                # arrow_center = center + direction * (40 * b.strength)
                arrow_center = center + direction * (40)
                

            # rotated = pg.transform.rotate(ARROW, -arrow.rotation)
            rotated = pg.transform.rotate(sp, -arrow.rotation)
            rect = rotated.get_rect(center=arrow_center)
            if b and b.speed == 0:
                self.screen.blit(rotated, rect)

    
        self.screen.blit(FONT.render("Round " + str(self.level) + " Shot " + str(self.shot), True, (0, 0, 0)), (20, 0))