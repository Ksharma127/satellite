import pgzrun
import random

WIDTH = 750
HEIGHT = 650

WHITE = (255,255,255)
BLUE = (0,0,255)
#create shape

ship=Actor("shooter")

bug=Actor("bug")
ship.pos=(WIDTH//2,HEIGHT-60)
bullets=[]
enemies= []
enemies.append(Actor("bug"))
enemies[-1].x=100
enemies[-1].y=-100
score=0
def displayscore():
    screen.draw.text(str(score),(100,30))


def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x =ship.x
        bullets[-1].y = ship.y-50

def update():
    global score
    if keyboard.left:
        ship.x=ship.x-5
        if ship.x<=0:
            ship.x=0
    elif keyboard.right:
        ship.x=ship.x+5
        if ship.x>=WIDTH:
            ship.x=WIDTH
    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y-=10
    
    for enemy in enemies:
        enemy.y+=2
        if enemy.y>=HEIGHT:
           enemy.y=-100
           enemy.x=random.randint(50,WIDTH-50)
        for bullet in bullets:
            if enemy.colliderect(bullet):
               score+=100
               bullets.remove(bullet)
               enemies.remove(enemy)



    

def draw():
    screen.clear()
    screen.fill((0,0,255))
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    displayscore()



pgzrun.go()
