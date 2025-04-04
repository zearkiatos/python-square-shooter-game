import random
import esper
import pygame

from src.ecs.components.c_input_command import CInputCommand
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_player import CTagPlayer


def create_square(world: esper.World, size: pygame.Vector2, position: pygame.Vector2, velocity: pygame.Vector2, color: pygame.Color) -> int:
    square_entity = world.create_entity()
    world.add_component(square_entity, CSurface(
        size, color))
    world.add_component(
        square_entity, CTransform(position))
    world.add_component(
        square_entity, CVelocity(velocity))

    return square_entity


def create_enemy_square(world: esper.World, position: pygame.Vector2, enemy_info: dict):
    width, height = tuple(enemy_info["size"].values())
    red, green, blue = tuple(enemy_info["color"].values())
    size = pygame.Vector2(width, height)
    color = pygame.Color(red, green, blue)
    velocity_max = enemy_info["velocity_max"]
    velocity_min = enemy_info["velocity_min"]
    velocity = pygame.Vector2(0, 0)
    while velocity.x == 0 and velocity.y == 0:
        velocity_range = random.randrange(velocity_min, velocity_max)
        velocity = pygame.Vector2(
            random.choice([-velocity_range, velocity_range]),
            random.choice([-velocity_range, velocity_range])
        )

    enemy_entity = create_square(world, size, position, velocity, color)
    world.add_component(enemy_entity, CTagEnemy())
    return enemy_entity


def create_enemy_spawner(world: esper.World, level_data: dict):
    spawner_entity = world.create_entity()
    world.add_component(spawner_entity, CEnemySpawner(
        level_data['enemy_spawn_events']))


def create_player_square(world: esper.World, player_info: dict, player_level_info: dict) -> int:
    size = pygame.Vector2(tuple(player_info["size"].values()))
    color = pygame.Color(tuple(player_info["color"].values()))
    x, y = tuple(player_level_info["position"].values())
    position = pygame.Vector2(x - (size.x/2), y - (size.y/2))
    velocity = pygame.Vector2(0, 0)

    player_entity = create_square(world, size, position, velocity, color)
    world.add_component(player_entity, CTagPlayer())
    return player_entity

def create_input_player(world: esper.World):
    input_left = world.create_entity()
    input_right = world.create_entity()
    input_up = world.create_entity()
    input_down = world.create_entity()
    world.add_component(input_left, CInputCommand("PLAYER_LEFT", pygame.K_LEFT))
    world.add_component(input_right, CInputCommand("PLAYER_RIGHT", pygame.K_RIGHT))
    world.add_component(input_up, CInputCommand("PLAYER_UP", pygame.K_UP))
    world.add_component(input_down, CInputCommand("PLAYER_DOWN", pygame.K_DOWN))
