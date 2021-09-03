#INPORTS#####################################
from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
from ursina.prefabs.health_bar \
    import HealthBar
#############################################

app = Ursina()
Sky(texture = 'assets3d/rlsky')
player = FirstPersonController(
    collider = 'box'
)

#GUN##############AND GRAPPLE##############################################
player.gun = None


gun = Button(parent=scene, model='cube', color=color.white, texture = 'assets3d/bluGUN', origin_y=-.5, position=(3,0,3), collider='box')
gun.on_click = Sequence(Func(setattr, gun, 'parent', camera), Func(setattr, player, 'gun', gun))


hookshot_target = Button(parent = scene, model ='cube', color=color.brown, position = (4,5,5))
hookshot_target1 = Button(parent = scene, model ='cube', color=color.red, position = (2,5,10))
hookshot_target2 = Button(parent = scene, model ='cube', color=color.orange, position = (10,5,2))
hookshot_target3 = Button(parent = scene, model ='cube', color=color.green, position = (15,5,2))
hookshot_target3.on_click = Func(player.animate_position, hookshot_target3.position, duration = .5, curve = curve.linear)
hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration = .5, curve = curve.linear)
hookshot_target1.on_click = Func(player.animate_position, hookshot_target1.position, duration = .5, curve = curve.linear)
hookshot_target2.on_click = Func(player.animate_position, hookshot_target2.position, duration = .5, curve = curve.linear)

def input(key):
    if key == 'left mouse down' and player.gun:
        gun.blink(color.orange)
        bullet = Entity(parent = gun, model ='cube', scale=.1, color = color.black)
        bullet.world_parent = scene
        bullet.animate_position(bullet.position+(bullet.forward*50), curve = curve.linear, duration = 1)
        destroy(bullet, delay = 1)
        

#ENVIRONMENT###############################################################

ground = Entity(model = 'plane',
                texture = 'grass',
                collider = 'mesh',
                scale = (100,1, 100))

target = Entity(model = 'cube',
                texture = 'assets3d/tgt',
                collider = 'box',
                position = (15, 1, 5))
                

trolol = Entity(model = 'plane',
               texture = 'assets3d/rltr',
               collider = 'mesh',
               scale = (100,1,100),
               position = (15, -300, 5))


app.run()
