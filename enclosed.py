import math as m

bulletlist = []

class objct():
    def __init__(self, x = 0, y = 0, height = 2, width = 2 ):
        self.position = [x,y]
        self.height = height
        self.width = width
        self.orientation = 0

class bullet():
    def __init__(self, origin, speedX, speedY, damagemod = 0, damage = 1, unvokedistance = 10):
        self.speedX = speedX
        self.speedY = speedY
        self.damage = damage + damagemod
        self.position = origin
        self.deltaTime = 0
        self.unvokedistance = unvokedistance

    def change_bullet_position_per_tick(self):
        self.deltaTime += 1
        self.position = (self.position[0] + self.deltaTime*self.speedX, self.position[1] + self.deltaTime*self.speedY)
        if self.deltaTime > self.unvokedistance:
            bulletlist.remove(self)



class gun():
    def __init__(self):
        self.speed = 10

    def shoot(self, position, orientation):
        #Calcular a velocidade da bala no x e no y
        bala = bullet(position, m.sin(orientation*(m.pi/180))*self.speed, m.cos(orientation*(m.pi/180))*self.speed) 
        bulletlist.append(bala)

class player_box(objct):
    def rotate(self, value): 
        self.orientation += value
    def shoot(self, gun):
        gun.shoot(self.position, self.orientation)


def impactado(bulletlist, field):
    for bullets in bulletlist:
        for object in field:
            if bullets.position[0]>object.position[0]-object.width/2 and bullets.position[0]<object.position[0]+object.width/2 and bullets.position[1]>object.position[1]-object.height/2 and bullets.position[1]<object.position[1]+object.height/2:
                return True

def atualizar_position(bulletlist):
    for bullet in bulletlist:
        bullet.change_bullet_position_per_tick()

def calculate_pixelpos_by_angle(angle):
    pass

def detect_things(player_pos, field, alcance = 10):
    detected = []
    for objct in field:
        if objct.position[0]>player_pos[0]-alcance and objct.position[0]<player_pos[0]+alcance and objct.position[1]>player_pos[1]-alcance and objct.position[1]<player_pos[1]+alcance:
            detected.append(objct)
    return detected

player = player_box()
gunplayer = gun()

alvo = objct(11, -4)

bala = bullet([0,0], m.sin(110*(m.pi/180))*2, m.cos(110*(m.pi/180))*2) 

bulletlist.append(bala)
field = []
field.append(alvo)
