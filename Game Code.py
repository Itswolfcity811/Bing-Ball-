def GameLoop():
    from Functions import MakeAWindow, DrawCir, DrawSmallEnemy,CheckClose, ResetEnemy, CheckForColistionSmall, DeclareEnemySmall, MoveEnemy
    import random as ran
    import pygame

    pygame.init()
    
    my_text = "Hi"

    
    
    #EnemyList = []
    Clock = pygame.time.Clock()
    
    Count = 0
    
    Playing = True
    
    MakeAWindow(1000, 1000, (0, 0, 0))
    
    Text = pygame.Surface((1000, 1000))
    
    Window = pygame.display.get_surface()

    
        
    SmallEnemy1y, SmallEnemy1x, SmallEnemy1Side = DeclareEnemySmall()
    SmallEnemy2y, SmallEnemy2x, SmallEnemy2Side = DeclareEnemySmall()
    SmallEnemy3y, SmallEnemy3x, SmallEnemy3Side = DeclareEnemySmall()
    SmallEnemy4y, SmallEnemy4x, SmallEnemy4Side = DeclareEnemySmall()


    

    SmallEnemySpeed = 10
    PlayerSpeed = 10
    PlayerSlowSpeed = ((PlayerSpeed % 10) + 1)
    #print(str(SmallEnemy1x))
    
    GoUp = True
    
    GoDown = False
    
    y = 500
    while Playing:
        #print(str(SmallEnemy1x))
        #print(SmallEnemy1Side)
        #print(SmallEnemy1x)
        if CheckClose():
            Playing = False
            break
        
        
        if (Count / 40) == 1:
            PlayerSpeed += 0.2
            PlayerSlowSpeed = (PlayerSpeed % 10)

        elif (Count / 5) == 1:
            SmallEnemySpeed += 1
        
        

        Window.fill((0, 0, 0))

        
        DrawCir(y)
                
        SmallEnemy1x = MoveEnemy(SmallEnemy1x, SmallEnemy1x, 10)
        SmallEnemy2x = MoveEnemy(SmallEnemy2x, SmallEnemy2x, 10)
        SmallEnemy3x = MoveEnemy(SmallEnemy3x, SmallEnemy3x, 10)
        SmallEnemy4x = MoveEnemy(SmallEnemy4x, SmallEnemy4x, 10)

        
        
        
        DrawSmallEnemy(SmallEnemy1x, SmallEnemy1y, SmallEnemy1Side)
        DrawSmallEnemy(SmallEnemy2x, SmallEnemy2y, SmallEnemy2Side)
        DrawSmallEnemy(SmallEnemy3x, SmallEnemy3y, SmallEnemy3Side)
        DrawSmallEnemy(SmallEnemy4x, SmallEnemy4y, SmallEnemy4Side)


        
        if CheckForColistionSmall(y, SmallEnemy1x, SmallEnemy1y) or CheckForColistionSmall(y, SmallEnemy2x, SmallEnemy2y) or CheckForColistionSmall(y, SmallEnemy3x, SmallEnemy3y) or CheckForColistionSmall(y, SmallEnemy4x, SmallEnemy4y):
            Playing = False
        
        SmallEnemy1x, SmallEnemy1y, SmallEnemy1Side = ResetEnemy(SmallEnemy1x, SmallEnemy1y, SmallEnemy1Side)
        SmallEnemy2x, SmallEnemy2y, SmallEnemy2Side = ResetEnemy(SmallEnemy2x, SmallEnemy2y, SmallEnemy2Side)
        SmallEnemy3x, SmallEnemy3y, SmallEnemy3Side = ResetEnemy(SmallEnemy3x, SmallEnemy3y, SmallEnemy3Side)
        SmallEnemy4x, SmallEnemy4y, SmallEnemy4Side = ResetEnemy(SmallEnemy4x, SmallEnemy4y, SmallEnemy4Side)

            

        if pygame.mouse.get_pressed() == (1, 0, 0) and GoUp:
            #while pygame.mouse.get_pressed() == (1, 0, 0) and GoUp:
            y -= PlayerSlowSpeed
            
        elif not pygame.mouse.get_pressed() == (1, 0, 0) and GoUp:
            y -= PlayerSpeed
            
        elif pygame.mouse.get_pressed() == (1, 0, 0) and GoDown:
            #while pygame.mouse.get_pressed() == (1, 0, 0) and GoDown:
            y += PlayerSlowSpeed
            
        elif not pygame.mouse.get_pressed() == (1, 0, 0) and GoDown:
            y += PlayerSpeed
            
        if y <= 0 and GoUp:
            GoUp = False
            GoDown = True
            Count += 1
            
        elif y >= 1000 and GoDown:
            GoUp = True
            GoDown = False
            Count += 1

        #print("1")
        pygame.display.flip()
        #Clock.tick(60)
    print("You got", str(Count))

GameLoop()
