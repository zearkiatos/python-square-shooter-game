import esper
from src.ecs.components.c_enemy_spawner import CEnemySpawner, SpawnEventData
from src.ecs.create.prefabric_creator import create_enemy_square

def system_enemy_spawner(world: esper.World, enemies_data:dict, delta_time: float):
    components = world.get_component(CEnemySpawner)
    c_enemy_spawner:CEnemySpawner

    for _, c_enemy_spawner in components:
        c_enemy_spawner.current_time += delta_time
        c_spawner_event:SpawnEventData
        for c_spawner_event in c_enemy_spawner.spawn_event_data:
            if c_enemy_spawner.current_time >= c_spawner_event.time and not c_spawner_event.triggered:
                c_spawner_event.triggered = True
                create_enemy_square(world, c_spawner_event.position, enemies_data[c_spawner_event.enemy_type])