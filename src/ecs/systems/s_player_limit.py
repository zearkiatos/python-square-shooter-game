import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_player import CTagPlayer

def system_player_limit(world: esper.World, screen: pygame.Surface) -> None:
    screen_reactangle = screen.get_rect()
    components = world.get_components(CTransform, CVelocity, CSurface, CTagPlayer)

    c_transform: CTransform
    c_velocity: CVelocity
    c_surface: CSurface
    c_tag_player: CTagPlayer
    for _, (c_transform, c_velocity, c_surface, c_tag_player) in components:
        square_rectangle = c_surface.surface.get_rect(topleft=c_transform.position)
        if square_rectangle.left <= 0 or square_rectangle.right >= screen_reactangle.width:
            square_rectangle.clamp_ip(screen_reactangle)
            c_transform.position.x = square_rectangle.left
            c_velocity.velocity.x = 0
        if square_rectangle.top <= 0 or square_rectangle.bottom >= screen_reactangle.height:
            square_rectangle.clamp_ip(screen_reactangle)
            c_transform.position.y = square_rectangle.top
            c_velocity.velocity.y = 0