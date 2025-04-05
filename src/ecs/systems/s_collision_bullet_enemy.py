import esper

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy

def system_collision_bullet_enemy(world: esper.World) -> None:
    enemy_components = world.get_components(CSurface, CTransform, CTagEnemy)
    bullet_components = world.get_components(CSurface, CTransform, CTagBullet)

    for bullet_entity, (c_bullet_surface, c_bullet_transform, _) in bullet_components:
        bullet_rectangle = c_bullet_surface.surface.get_rect(topleft = c_bullet_transform.position)
        for enemy_entity, (c_enemy_surface, c_enemy_transform, _) in enemy_components:
            enemy_rectangle = c_enemy_surface.surface.get_rect(topleft = c_enemy_transform.position)
            if bullet_rectangle.colliderect(enemy_rectangle):
                world.delete_entity(bullet_entity)
                world.delete_entity(enemy_entity)
                break