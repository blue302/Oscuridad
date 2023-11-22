init python:
    def inventoryUpdate(st):
        pass
    def inventoryEvents(event, x, y, at):
        pass
    def environmentEvents(event, x, y, at):
        pass
screen scene1:
    add environment_SM

label setupScene1:
    $environment_items = ["box", "door-vines", "key", "lantern"]

    python:
        for item in environment_items:
            idle_image = Image("Environment Items/{}-idle.png".format(item))   
            hover_image = Image("Environment Items/{}-hover.png".format(item)) 
            t = Transform(child=idle_image, zoom=0.5)
            environment_sprites.append(environment_SM.create(t))
            environment_sprites[-1].type = item
            environment_sprites[-1].idle_image = idle_image
            environment_sprites[-1].hover_image = hover_image

            if item == "box":
                environment_sprites[-1].width = 157/2
                environment_sprites[-1].height = 125/2
                environment_sprites[-1].x = 780
                environment_sprites[-1].y = 430
            elif item == "door-vines":
                environment_sprites[-1].width = 450/2
                environment_sprites[-1].height = 603/2
                environment_sprites[-1].x = 1200
                environment_sprites[-1].y = 355
            elif item == "key":
                environment_sprites[-1].width = 101/2
                environment_sprites[-1].height = 55/2
                environment_sprites[-1].x = 780
                environment_sprites[-1].y = 420
            elif item == "lantern":
                environment_sprites[-1].width = 123/2
                environment_sprites[-1].height = 181/2
                environment_sprites[-1].x = 345
                environment_sprites[-1].y = 160

    scene scene-1-bg at half_size:
    call screen scene1

transform half_size:
    zoom 0.5

label start:
    $config.rollback_enabled = False
    $quick_menu = False
    $environment_SM = SpriteManager(event=environmentEvents)
    $inventory_SM = SpriteManager(update=inventoryUpdate, event=environmentEvents)
    $inventory_sprites = []
    $environment_sprites = []
    $environment_items = []
    $inventory_items = []
    $environment_item_names = []
    $inventory_item_names = ["key", "Lantern", "Matches", "Sacateure"]
    $current_scene = "scene1"

    jump setupScene1
    return
