import pygame


pygame.init()

def CheckClose():
    Close = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Close = True
    return Close

def MakeAWindow(Hight, Lenth, Color):
    
    Window = pygame.display.set_mode([Hight, Lenth])
    
    Window.fill(Color)
    
    pygame.display.flip()
    #return Window
    
    
def DrawCir(y):
    #from GameChalange import y
    Window = pygame.display.get_surface()
    #def __init__(self):
    
     
        
    pygame.draw.circle(Window, (255, 165, 0), (500, y), 15)
        
    #pygame.display.flip()
    #print(self.y)
    
    
def DrawSmallEnemy(x,y,SmallEnemy1Side):
        
    Window = pygame.display.get_surface()
    
    if SmallEnemy1Side == 1:
        pygame.draw.polygon(Window, (255,255,0), [(x, y + 50), (x, y - 50), (x - 50, y)])

    else:
        pygame.draw.polygon(Window, (255,255,0), [(x, y - 50), (x, y + 50), (x + 50, y)])
    
        
    #pygame.display.update()



def ResetEnemy(SmallEnemyx, SmallEnemy1y, SmallEnemySide):
    import random as ran
    
    wait1 = ran.randint(1200, 2000)
    wait2 = ran.randint(-1000, -200)

    
    if SmallEnemyx >= wait1 or SmallEnemyx == wait2:
        #print(str(SmallEnemy1x))
        SmallEnemySide = ran.randint(1, 2)
        if SmallEnemySide == 1:
            SmallEnemyx = 1050
            #SmallEnemy1x = 500
            
        else:
            SmallEnemyx = -50
            #SmallEnemy1x = 500
        
        #print("Reset")
        
        SmallEnemy1y = ran.randint(0, 1000)
    return SmallEnemyx, SmallEnemy1y, SmallEnemySide

    
    

def CheckForColistionSmall(Playery, enemyx, enemyy):
    Hit = False
    if enemyx == 500:
        if Playery <= (enemyy + 51) and Playery >= (enemyy - 51):
            Hit = True
    return Hit

def DeclareEnemySmall():
    import random as ran
    
    SmallEnemy1Side = ran.randint(1, 2)
    if SmallEnemy1Side == 1:
        SmallEnemy1x = 1050
        #SmallEnemy1x = 500

    else:
        SmallEnemy1x = -50
        #SmallEnemy1x = 500
    
    
    #print(str(SmallEnemy1Side))
    
    SmallEnemy1y = ran.randint(0, 1000)
    
    return SmallEnemy1y, SmallEnemy1x, SmallEnemy1Side

def MoveEnemy(SmallEnemy1x, SmallEnemy1Side, speed):
    if SmallEnemy1Side == 1:
        SmallEnemy1x -= speed
    else:
        SmallEnemy1x += speed
    return SmallEnemy1x
