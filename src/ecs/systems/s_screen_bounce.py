import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_enemy import CTagEnemy

def system_screen_bounce(world:esper.World, screen:pygame.Surface):
    screen_reactangle = screen.get_rect()
    components = world.get_components(CTransform, CVelocity, CSurface, CTagEnemy)

    c_transform: CTransform
    c_velocity: CVelocity
    c_surface: CSurface
    c_tag_enemy: CTagEnemy
    for _, (c_transform, c_velocity, c_surface, c_tag_enemy) in components:
        square_rectangle = c_surface.surface.get_rect(topleft=c_transform.position)
        if square_rectangle.left < 0 or square_rectangle.right > screen_reactangle.width:
            c_velocity.velocity.x *= -1
            square_rectangle.clamp_ip(screen_reactangle)
            c_transform.position.x = square_rectangle.left

        if square_rectangle.top < 0 or square_rectangle.bottom > screen_reactangle.height:
            c_velocity.velocity.y *= -1
            square_rectangle.clamp_ip(screen_reactangle)
            c_transform.position.y = square_rectangle.y