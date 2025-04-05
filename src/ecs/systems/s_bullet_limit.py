import esper

from src.ecs.components.tags.c_tag_bullet import CTagBullet

def system_bullet_limit(world: esper.World, levels_config: dict):
    components = world.get_components(CTagBullet)
    
    return len(components) >= levels_config["max_bullets"]