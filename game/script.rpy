init python:
    # created functions that was defined at lbl start
    def inventoryUpdate(st):
        pass
    def inventoryEvents(event, x, y, at):
        pass
    def environmentEvents(event, x, y, at):
        pass
    def inventoryArrows(button):
        pass
screen UI:
    zorder 1
    image "UI/inventory-icon-bg.png" xpos 0 ypos 0.8 at half_size
    imagebutton auto "UI/inventory-icon-%s.png" action If(renpy.get_screen("inventory") == None, true= Show("inventory"), false= Hide("inventory")) xpos 0.03 ypos 0.825 at half_size
    #the condition above decides wether to show or hide inventory 
screen inventory:
    # inventory background img
    image "UI/inventory-bg.png" xpos 0.17 ypos 0.8 at half_size
    # image of the actual slots within the inventory
    image "UI/inventory-slots.png" xpos 0.274 ypos 0.845 at half_size

    imagebutton idle If(inventory_rb_enabled == True, true= "UI/inventory-arrow-right-enabled-idle.png", false= "UI/inventory-arrow-right-disabled.png") hover If(inventory_rb_enabled == True, true= "UI/inventory-arrow-right-enabled-hover.png", false= "UI/inventory-arrow-right-disabled.png") action Function(inventoryArrows, button = "right") xpos 0.921 ypos 0.86 at half_size
    imagebutton idle If(inventory_lb_enabled == True, true= "UI/inventory-arrow-left-enabled-idle.png", false= "UI/inventory-arrow-left-disabled.png") hover If(inventory_lb_enabled == True, true= "UI/inventory-arrow-left-enabled-hover.png", false= "UI/inventory-arrow-left-disabled.png") action Function(inventoryArrows, button = "left") xpos 0.202 ypos 0.86 at half_size


screen scene1:
    add environment_SM

label setupScene1:
    # items within inventory 
    $environment_items = ["box", "door-vines", "key", "lantern"]#use file name in order to work

    # for in loop that runs code for every item within environment items 
    python:
        for item in environment_items:
            #created 2 images that the sprites will use
            idle_image = Image("Environment Items/{}-idle.png".format(item))   
            hover_image = Image("Environment Items/{}-hover.png".format(item)) 
            # creted a transform to edit size
            t = Transform(child=idle_image, zoom=0.5)
            # sprite object appended a reference to the environment sprite list
            environment_sprites.append(environment_SM.create(t))
            # bellow are custom attribute for environment
            environment_sprites[-1].type = item
            environment_sprites[-1].idle_image = idle_image
            environment_sprites[-1].hover_image = hover_image
            # bellow are properties for each item 
            if item == "box":
                environment_sprites[-1].width = 157 / 2
                environment_sprites[-1].height = 115 / 2
                environment_sprites[-1].x = 780
                environment_sprites[-1].y = 420
            elif item == "door-vines":
                environment_sprites[-1].width = 450 / 2
                environment_sprites[-1].height = 603 / 2
                environment_sprites[-1].x = 345
                environment_sprites[-1].y = 160
            elif item == "key":
                environment_sprites[-1].width = 101 / 2
                environment_sprites[-1].height = 55 / 2
                environment_sprites[-1].x = 1020
                environment_sprites[-1].y = 430
            elif item == "lantern":
                environment_sprites[-1].width = 123 / 2
                environment_sprites[-1].height = 181 / 2
                environment_sprites[-1].x = 1200
                environment_sprites[-1].y = 355

    scene scene-1-bg at half_size
    call screen scene1
# scales bckgrnd image 2 half
transform half_size:
    zoom 0.5

label start:
    # not entirely sure what all of these are but rollback is dissabled for some reason
    $config.rollback_enabled = False
    $quick_menu = False #dissabled because its interfiring with ui within tutorial
    $environment_SM = SpriteManager(event = environmentEvents)#this sprite handles the environment event mouse cklck 
    $inventory_SM = SpriteManager(update= inventoryUpdate, event= inventoryEvents)#this sprite handles inventory
    $inventory_sprites = []#this list are reference to SM
    $environment_sprites = []#this list are reference to SM

    #the following 2 will list contain actual file names for each images that were going to be putting onto the  sprites?
    $environment_items = []
    $inventory_items = []

    # the following list contain readable names for items so that we dont have to use file names
    $environment_item_names = []
    $inventory_item_names = ["key", "Lantern", "Matches", "Sacateure"]

    
    $current_scene = "scene1" #keeps track of the current scene supposedly this will help later to better manage this for our project 

    # helps determine if we want to use the enable or disabled version of images
    $inventory_rb_enabled = False
    $inventory_lb_enabled = False

    show screen UI
    jump setupScene1
    return
