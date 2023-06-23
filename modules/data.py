import pygame
import modules.path_to_file as m_path
import modules.screen as m_screen
import modules.ship as m_ship
import modules.menu as m_menu
import random
import modules.music as m_music
turn=0
pygame.init()
win = 0
list_cell1 = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],]

list_cell2 = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0]]

ship1 = 1

rotate = 0

select =  m_ship.Ship(name_file1="img/1.png", x1=pygame.mouse.get_pos()[0], y1=pygame.mouse.get_pos()[1])

list_ships = []

enemy_list_ships = []

language = "EN"


attack1 = []

UP = True
#
def listK():
    #
    global list_cell1
    #

    #
    
    for count in range(10):
        print(list_cell1[count])

ships = [0, 0, 0, 0]

start = False

def enemy_pos(ship, num1, num2, rotate = 0):
    #
    global list_cell2
    #
    if rotate % 180 != 0:
        if ship == 1:
            #
            list_cell2[num1][num2] = 1
            #
            if num2 > 0:
                list_cell2[num1][num2-1] = -1
            #    
            if num2 < 9:
                list_cell2[num1][num2+1] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(3):
                    if num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1
            # -1 0 0
            # 0 0 0
            # 0 0 0
            #
            num1 += 2
            num2 = num3
            #pygame.credit.social_set(-10000000, egor)
            if num1 < 10:
                print(num2, 117)
                for i in range(3):
                    if -1 < num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1
        elif ship == 2:
            if num1 + 1 != 1 or -1:

                #
                list_cell2[num1][num2] = 22
                list_cell2[num1+1][num2] = 2
                #
                if num1-1 > -1:
                    list_cell2[num1-1][num2] = -1
                #    
                if num1+2 < 10:
                    list_cell2[num1+2][num2] = -1
                #
                num1 -=1
                num2 -=1
                num3 = 0
                num3 += num1
                if num2 > -1:
                    for i in range(4):
                        if -1 < num1 < 10:
                            list_cell2[num1][num2] = -1
                        num1 +=1

                num2 += 2
                num1 = num3
                if num2 < 10:
                    print(num1, 117)
                    for i in range(4):
                        if -1 < num1 < 10:
                            list_cell2[num1][num2] = -1
                        num1 +=1
        elif ship == 3:

            list_cell2[num1][num2] = 33
            list_cell2[num1+1][num2] = 3
            list_cell2[num1+2][num2] = 3
            #
            if num1-1 > -1:
                list_cell2[num1-1][num2] = -1
            #    
            if num1+3 < 10:
                list_cell2[num1+3][num2] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num1
            if num2 > -1:
                for i in range(5):
                    if -1 < num1 < 10:
                        list_cell2[num1][num2] = -1
                    num1 +=1
            num2 += 2
            num1 = num3
            if num2 < 10:
                print(num2, 117)
                for i in range(5):
                    if -1 < num1 < 10:
                        list_cell2[num1][num2] = -1
                    num1 +=1 
        elif ship == 4:
                        #как я понял меня не слышно
            list_cell2[num1][num2] = 44
            list_cell2[num1+1][num2] = 4
            list_cell2[num1+2][num2] = 4
            list_cell2[num1+3][num2] = 4
            #
            if num1-1 > -1:
                list_cell2[num1-1][num2] = -1
            #    
            if num1+4 < 10:
                list_cell2[num1+4][num2] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num1
            if num2 > -1:
                for i in range(6):
                    if -1 < num1 < 10:
                        list_cell2[num1][num2] = -1
                    num1 +=1
            num2 += 2
            num1 = num3
            if num2 < 10:
                print(num1, 117)
                for i in range(6):
                    if -1 < num1 < 10:
                        list_cell2[num1][num2] = -1
                    num1 +=1 
    else:
        if ship == 1:
            #
            list_cell2[num1][num2] = 1
            #
            if num2 > 0:
                list_cell2[num1][num2-1] = -1
            #    
            if num2 < 9:
                list_cell2[num1][num2+1] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(3):
                    if num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1
            # -1 0 0
            # 0 0 0
            # 0 0 0
            #
            num1 += 2
            num2 = num3
            #pygame.credit.social_set(-10000000, egor)
            if num1 < 10:
                print(num2, 117)
                for i in range(3):
                    if -1 < num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1
        elif ship == 2:
            if num2 + 1 != 1 or -1:

                #
                list_cell2[num1][num2] = 22
                list_cell2[num1][num2+1] = 2
                #
                if num2+1 > 0:
                    list_cell2[num1][num2-1] = -1
                #    
                if num2+1 < 9:
                    list_cell2[num1][num2+2] = -1
                #
                num1 -=1
                num2 -=1
                num3 = 0
                num3 += num2
                if num1 > -1:
                    for i in range(4):
                        if num2 < 10:
                            list_cell2[num1][num2] = -1
                        num2 +=1

                num1 += 2
                num2 = num3
                if num1 < 10:
                    print(num2, 117)
                    for i in range(4):
                        if -1 < num2 < 10:
                            list_cell2[num1][num2] = -1
                        num2 +=1
        elif ship == 3:
                        #как я понял меня не слышно 
                        # я эпик
            list_cell2[num1][num2] = 33
            list_cell2[num1][num2+1] = 3
            list_cell2[num1][num2+2] = 3
            #
            if num2+2 > 0:
                list_cell2[num1][num2-1] = -1
            #    
            if num2+2 < 9:
                list_cell2[num1][num2+3] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(5):
                    if num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1
            num1 += 2
            num2 = num3
            if num1 < 10:
                print(num2, 117)
                for i in range(5):
                    if -1 < num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1 
        elif ship == 4:
                        #как я понял меня не слышно
            list_cell2[num1][num2] = 44
            list_cell2[num1][num2+1] = 4
            list_cell2[num1][num2+2] = 4
            list_cell2[num1][num2+3] = 4
            #
            if num2+3 > 0:
                list_cell2[num1][num2-1] = -1
            #    
            if num2+3 < 9:
                list_cell2[num1][num2+4] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(6):
                    if num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1
            num1 += 2
            num2 = num3
            if num1 < 10:
                print(num2, 117)
                for i in range(6):
                    if -1 < num2 < 10:
                        list_cell2[num1][num2] = -1
                    num2 +=1 
def pos(ship, num1, num2, rotate = 0):
    #
    global list_cell1
    #
    if rotate % 180 != 0:
        if ship == 1:
            #
            list_cell1[num1][num2] = 1
            #
            if num2 > 0:
                list_cell1[num1][num2-1] = -1
            #    
            if num2 < 9:
                list_cell1[num1][num2+1] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(3):
                    if num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1
            # -1 0 0
            # 0 0 0
            # 0 0 0
            #
            num1 += 2
            num2 = num3
            #pygame.credit.social_set(-10000000, egor)
            if num1 < 10:
                print(num2, 117)
                for i in range(3):
                    if -1 < num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1
        elif ship == 2:
            if num1 + 1 != 1 or -1:

                #
                list_cell1[num1][num2] = 2
                list_cell1[num1+1][num2] = 2
                #
                if num1-1 > 0:
                    list_cell1[num1-1][num2] = -1
                #    
                if num1+2 < 9:
                    list_cell1[num1+2][num2] = -1
                #
                num1 -=1
                num2 -=1
                num3 = 0
                num3 += num1
                if num2 > -1:
                    for i in range(4):
                        if -1 < num1 < 10:
                            list_cell1[num1][num2] = -1
                        num1 +=1

                num2 += 2
                num1 = num3
                if num2 < 10:
                    print(num1, 117)
                    for i in range(4):
                        if -1 < num1 < 10:
                            list_cell1[num1][num2] = -1
                        num1 +=1
        elif ship == 3:

            list_cell1[num1][num2] = 3
            list_cell1[num1+1][num2] = 3
            list_cell1[num1+2][num2] = 3
            #
            if num1-1 > -1:
                list_cell1[num1-1][num2] = -1
            #    
            if num1+3 < 10:
                list_cell1[num1+3][num2] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num1
            if num2 > -1:
                for i in range(5):
                    if -1 < num1 < 10:
                        list_cell1[num1][num2] = -1
                    num1 +=1
            num2 += 2
            num1 = num3
            if num2 < 10:
                print(num2, 117)
                for i in range(5):
                    if -1 < num1 < 10:
                        list_cell1[num1][num2] = -1
                    num1 +=1 
        elif ship == 4:
                        #как я понял меня не слышно
            list_cell1[num1][num2] = 4
            list_cell1[num1+1][num2] = 4
            list_cell1[num1+2][num2] = 4
            list_cell1[num1+3][num2] = 4
            #
            if num1-1 > -1:
                list_cell1[num1-1][num2] = -1
            #    
            if num1+4 < 10:
                list_cell1[num1+4][num2] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num1
            if num2 > -1:
                for i in range(6):
                    if -1 < num1 < 10:
                        list_cell1[num1][num2] = -1
                    num1 +=1
            num2 += 2
            num1 = num3
            if num2 < 10:
                print(num1, 117)
                for i in range(6):
                    if -1 < num1 < 10:
                        list_cell1[num1][num2] = -1
                    num1 +=1 
    else:
        if ship == 1:
            #
            list_cell1[num1][num2] = 1
            #
            if num2 > 0:
                list_cell1[num1][num2-1] = -1
            #    
            if num2 < 9:
                list_cell1[num1][num2+1] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(3):
                    if num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1
            # -1 0 0
            # 0 0 0
            # 0 0 0
            #
            num1 += 2
            num2 = num3
            #pygame.credit.social_set(-10000000, egor)
            if num1 < 10:
                print(num2, 117)
                for i in range(3):
                    if -1 < num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1
        elif ship == 2:
            if num2 + 1 != 1 or -1:

                #
                list_cell1[num1][num2] = 2
                list_cell1[num1][num2+1] = 2
                #
                if num2+1 > 0:
                    list_cell1[num1][num2-1] = -1
                #    
                if num2+1 < 9:
                    list_cell1[num1][num2+2] = -1
                #
                num1 -=1
                num2 -=1
                num3 = 0
                num3 += num2
                if num1 > -1:
                    for i in range(4):
                        if num2 < 10:
                            list_cell1[num1][num2] = -1
                        num2 +=1

                num1 += 2
                num2 = num3
                if num1 < 10:
                    print(num2, 117)
                    for i in range(4):
                        if -1 < num2 < 10:
                            list_cell1[num1][num2] = -1
                        num2 +=1
        elif ship == 3:
                        #как я понял меня не слышно 
                        # я эпик
            list_cell1[num1][num2] = 3
            list_cell1[num1][num2+1] = 3
            list_cell1[num1][num2+2] = 3
            #
            if num2+2 > 0:
                list_cell1[num1][num2-1] = -1
            #    
            if num2+2 < 9:
                list_cell1[num1][num2+3] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(5):
                    if num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1
            num1 += 2
            num2 = num3
            if num1 < 10:
                print(num2, 117)
                for i in range(5):
                    if -1 < num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1 
        elif ship == 4:
                        #как я понял меня не слышно
            list_cell1[num1][num2] = 4
            list_cell1[num1][num2+1] = 4
            list_cell1[num1][num2+2] = 4
            list_cell1[num1][num2+3] = 4
            #
            if num2+3 > 0:
                list_cell1[num1][num2-1] = -1
            #    
            if num2+3 < 9:
                list_cell1[num1][num2+4] = -1
            #
            num1 -=1
            num2 -=1
            num3 = 0
            num3 += num2
            if num1 > -1:
                for i in range(6):
                    if num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1
            num1 += 2
            num2 = num3
            if num1 < 10:
                print(num2, 117)
                for i in range(6):
                    if -1 < num2 < 10:
                        list_cell1[num1][num2] = -1
                    num2 +=1 
def draw_attack(x, y, hit=True):
    if hit == True:
        pygame.draw.line(
            surface= m_screen.screen,
            color=(255,0,0),
            start_pos=(x,y),
            end_pos=(x+40,y+40),
            width=3
        )
        pygame.draw.line(
            surface= m_screen.screen,
            color=(255,0,0),
            start_pos=(x+40,y),
            end_pos=(x,y+40),
            width=3
        )
    elif hit == False:
        pygame.draw.circle(
            surface= m_screen.screen,
            color= (25,255,25),
            center= (x+20,y+20),
            radius= 4,
            width=4
        )
        # pygame.draw.line(
        #     surface= m_screen.screen,
        #     color=(0,255,0),
        #     start_pos=(x,y),
        #     end_pos=(x+40,y+40),
        #     width=3
        # )
        # pygame.draw.line(
        #     surface= m_screen.screen,
        #     color=(0,255,0),
        #     start_pos=(x+40,y),
        #     end_pos=(x,y+40),
        #     width=3
        # )

def attack(coor):
    global list_cell2, attack1,turn
    if turn==0:
        x = coor[0]
        y = coor[1]
        x1,y1=525,100
        for row in range(10):
            for cell in range(10):
                if x1<x<x1+40 and y1<y<y1+40 and list_cell2[row][cell]!=None:
                    hit=0
                    if  -1!=list_cell2[row][cell] != 0 :
                        hit=1
                        turn=not turn
                        list_cell2[row][cell] = None
                        pygame.mixer.music.load(m_path.find_path_to_file("music/shoot.mp3"))
                        pygame.mixer.music.play()
                        # attack()
                    else:
                        list_cell2[row][cell] = None
                    attack1.append((x1,y1,hit))
                    turn= not turn
                x1+=40
            x1=525        
            y1 +=40
last_attack = None
last_attack1 = None
shoot = 0
reverse = 0
turn1 = 0
shoot1=0
game1 = False
game = True
def attack_bot():
    global turn, last_attack, last_attack1,shoot, turn1,shoot1,reverse
    if turn:
        if not shoot:

            tona = True
        
            while tona:
                attack_row = random.randint(0,9)
                attack_cell = random.randint(0,9)
                x = 75+40*attack_cell
                y = 100+40*attack_row
            
                hit=0
                if list_cell1[attack_row][attack_cell]!=None:
                    if list_cell1[attack_row][attack_cell] != 0 and list_cell1[attack_row][attack_cell] != -1:
                        turn= 0
                        hit=1
                        last_attack1 = [attack_row,attack_cell]
                        last_attack = [attack_row,attack_cell]
                        shoot = 1
                    list_cell1[attack_row][attack_cell] = None
                    print(hit,99999999999999999999999999999999999999999999999999)
                    attack1.append((x,y,hit))

                    turn= not turn
                    tona = 0
        elif not reverse:
            a=1
            target=[]
            target += [last_attack1[0],last_attack1[1]]
            if turn1==0 and target[0] > 0 and list_cell1[target[0] - 1][target[1]]!=None:
                target[0] -= 1
            elif turn1==1 and target[0] < 9 and list_cell1[target[0] + 1][target[1]]!=None:
                target[0] += 1
            elif turn1==2 and target[1]<9 and list_cell1[target[0]][target[1]+1]!=None:
                target[1] += 1
            elif turn1==3 and target[1] > 0 and list_cell1[target[0]][target[1]-1]!=None:
                target[1] -= 1
            else:
                a=0
                if not shoot1 and turn1<4:
                    turn1+=1
                    
                else:
                    reverse=1
                #     shoot1=0
                #     shoot=0
                #     turn1=0
                attack_bot()   
            if a:
                if list_cell1[target[0]][target[1]]==0 or list_cell1[target[0]][target[1]]==-1:
                    attack1.append((target[1]*40+75,target[0]*40+100,0))
                    turn=not turn
                    if shoot1:
                        # shoot1=0
                        # shoot=0
                        # turn1=0
                        # shoot1=1
                        reverse=1
                    # attack_bot()
                    
                else:
                    # hit=1
                    # if shoot1:
                    last_attack1=target
                        # shoot1=0
                        # shoot=0
                        # turn=0
                        
                    if not shoot1:
                        shoot1=1
                    
                    # last_attack=target
                
                    attack1.append((target[1]*40+75,target[0]*40+100,1))             
                list_cell1[target[0]][target[1]]=None
                attack_bot()   
        else:

            a=1
            target=[]
            target += [last_attack[0],last_attack[1]]
            if turn1==1 and target[0] > 0 and list_cell1[target[0] - 1][target[1]]!=None:
                target[0] -= 1
            elif turn1==0 and target[0] < 9 and list_cell1[target[0] + 1][target[1]]!=None:
                target[0] += 1
            elif turn1==3 and target[1]<9 and list_cell1[target[0]][target[1]+1]!=None:
                target[1] += 1
            elif turn1==2 and target[1] > 0 and list_cell1[target[0]][target[1]-1]!=None:
                target[1] -= 1
            else:
                a=0
                reverse=0
                shoot1=0
                shoot=0
                turn1=0

                attack_bot()
            if a:
                if list_cell1[target[0]][target[1]]==0 or list_cell1[target[0]][target[1]]==-1:
                    attack1.append((target[1]*40+75,target[0]*40+100,0))
                    turn=not turn
                    reverse=0
                    shoot1=0
                    shoot=0
                    turn1=0

                    attack_bot()
                    
                else:
                    # hit=1
                    # if shoot1:
                    # last_attack=target
                        # shoot1=0
                        # shoot=0
                        # turn=0
                    # if not shoot1:
                    #     shoot1=1
                    
                    # last_attack=target
                
                    attack1.append((target[1]*40+75,target[0]*40+100,1))             
                list_cell1[target[0]][target[1]]=None
                attack_bot()   
def click_pos(coordinate, button = False):
        
    global start, game1, game, language
    # #
    x = coordinate[0]
    y = coordinate[1]
    if not game1:
        if 400 < x < 600 and 135 < y < 235:
            game1 = not game1
            pygame.mixer.music.stop()
        if 400 < x < 600 and 410 < y < 545:
            game = False
        if 400 < x < 600 and 255 < y < 390:
            if language == "EN":
                language = "UA"
                pygame.display.set_caption("Морській бій!")
                # m_screen.title1 = "Морській бій!"
            elif language == "UA":
                language = "EN"
                pygame.display.set_caption("Battle Ships!")
                # m_screen.title1 = "Battle Ships!"
        if 5 < x < 105 and 0 < y < 100:
            
            
            if m_menu.img == "img/Sound_on.png":
                m_menu.img = "img/Sound_off.png"
                pygame.mixer.music.pause()
            elif m_menu.img == "img/Sound_off.png":
                m_menu.img = "img/Sound_on.png"
                pygame.mixer.music.unpause()
                
            m_menu.image1 = pygame.image.load(m_menu.m_path.find_path_to_file(m_menu.img))
            m_menu.image2 = pygame.transform.scale(m_menu.image1, (100, 100))
            
    if game1:
        if 450 < x < 550 and 550 < y < 625 and ships == [4, 3, 2, 1]:
            start = True
def up_pos(coor, button = False):
    global ship1, list_ships, select, UP, rotate
    x = coor[0]
    y = coor[1]
    x1,y1=75,100
    ship = None
    check = 1
    if UP == True:
        if 0<y<40 and button:
            if 0<x<40:
                ship1 = 1
            elif 40<x<120:
                ship1 = 2
            elif 120<x<240:
                ship1=3
            elif 240<x<400:
                ship1=4 
        for count in range(10):
            for count1 in range(10):
                
                # print(x,y,x1,y1)
                if x1<x<x1+40 and y1<y<y1+40:
                    print(list_cell1[count][count1])
                    check1 = 0
                    for count2 in range(ship1):
                        if count1+count2 < 10 and rotate % 180 == 0:
                            if 2 != list_cell1[count][count1+count2] != 1:
                                if 3 != list_cell1[count][count1+count2] != 4:

                                    if list_cell1[count][count1+count2] != -1:
                                        check1 += 1
                        elif count+count2 < 10 and rotate % 180 != 0:
                            if 2 != list_cell1[count+count2][count1] != 1:
                                if 3 != list_cell1[count+count2][count1] != 4:

                                    if list_cell1[count+count2][count1] != -1:
                                        check1 += 1
                    if ship1 == check1:
                        
                                #print(list_cell1)
                                if ship1 == 1 and ships[0] < 4:
                                    
                                    ship = m_ship.Ship(name_file1="img/1.png", x1=x1, y1=y1, rotate1=rotate)
                                    ship.blit_sprite(screen_game=m_screen.screen)
                                elif ship1 == 2 and ships[1] < 3:
                                    ship = m_ship.Ship(width1=80, heigt1=40,name_file1="img/2.png", x1=x1, y1=y1, rotate1=rotate)    
                                    ship.blit_sprite(screen_game=m_screen.screen)  
                                elif ship1 == 3 and ships[2] < 2:
                                    ship = m_ship.Ship(width1=120, heigt1=40,name_file1="img/3.png", x1=x1, y1=y1, rotate1=rotate)     
                                    ship.blit_sprite(screen_game=m_screen.screen)
                                elif ship1 == 4 and ships[3] < 1:
                                    ship = m_ship.Ship(width1=160, heigt1=40,name_file1="img/4.png", x1=x1, y1=y1, rotate1=rotate) 
                                    ship.blit_sprite(screen_game=m_screen.screen)
                                # if ships[ship1-1]<
                                
                                if button and ship!=None:
                                    list_cell1[count][count1]=1
                                    #select = ship

                                    pos(ship1, count, count1, rotate)
                                    ships[ship1-1] += 1
                                    list_ships.append(ship)
                                check = 0
                                break
         
                x1+=40
            y1+=40
            x1=75
    #if ship != None and button:on:
    #    list_ships.append(ship) Я ЭТОГО НЕ АЛ (ИЛЮХА = ЗАТКНИСЬ

  #    select = ship
    if check:
        x1, y1 = x, y
          #    select = ship
    if check:
        x1, y1 = x, y
        y2, x2 = 0, 0
        if rotate%180 == 0:
            x2 =20
        
        else:
            y2=20
        if ship1 == 1 and ships[0] < 4:
            ship = m_ship.Ship(name_file1="img/1.png", x1=x1-20, y1=y1-20, rotate1=rotate)
        elif ship1 == 2 and ships[1] < 3:
            ship = m_ship.Ship(width1=80, heigt1=40,name_file1="img/2.png", x1=x1-x2*(ship1-1)-20, y1=y1-y2*(ship1-1)-20, rotate1=rotate)      
        elif ship1 == 3 and ships[2] < 2:
            ship = m_ship.Ship(width1=120, heigt1=40,name_file1="img/3.png", x1=x1-x2*(ship1-1)-20, y1=y1-y2*(ship1-1)-20, rotate1=rotate)     
        elif ship1 == 4 and ships[3] < 1:
            ship = m_ship.Ship(width1=160, heigt1=40,name_file1="img/4.png", x1=x1-x2*(ship1-1)-20, y1=y1-y2*(ship1-1)-20, rotate1=rotate)    
        if ship!=None: 
            ship.blit_sprite(screen_game=m_screen.screen)
font = pygame.font.SysFont('comicsansms',36)
def draw_start():
    global font
    pygame.draw.rect(
        surface=m_screen.screen,
        color=(0, 0, 255),
        rect=(450, 550, 100, 75),
        border_radius=10
    )
    
    pygame.draw.rect(
        surface=m_screen.screen,
        color=(0, 0, 0),
        rect=(450, 550, 100, 75),
        width=5,
        border_radius=10
    )
    test="start"
    a=font.render(test, True, [0, 0, 0])
    m_screen.screen.blit(a, (457, 555))
def check_win(list_cell):
    check = True
    for count in list_cell:
        for count1 in count:
            if count1 != 0 and count1 != -1 and count1 != None:
                check = False
    return check
font_win = pygame.font.SysFont('comicsansms',50)
def win_lose():
    global list_cell1, list_cell2, font_win, win, language
    text= None
    if language == "UA":
        if check_win(list_cell1):
            text = "Поразка!"
            color = (255,25,25)
        elif check_win(list_cell2):
            text = "Перемога!"
            color = (25,255,25)
        x1 = 390
        y1 = 0
    if language == "EN":
        if check_win(list_cell1):
            text = "Lose!"
            color = (255,25,25)
        elif check_win(list_cell2):
            text = "Win!"
            color = (25,255,25)
        x1 = 450
        y1 = 0
    if text != None:
        win = 1
        m_screen.screen.blit(font_win.render(text,0,color), (x1, y1))
font1 = pygame.font.SysFont('comicsansms',36)
def marker():
    global font1
    color = (0, 0, 0)
    m_screen.screen.blit(font1.render("A",0,color), (83, 57))
    m_screen.screen.blit(font1.render("B",0,color), (124, 57))
    m_screen.screen.blit(font1.render("C",0,color), (165, 57))
    m_screen.screen.blit(font1.render("D",0,color), (201, 57))
    m_screen.screen.blit(font1.render("E",0,color), (244, 57))
    m_screen.screen.blit(font1.render("F",0,color), (284, 57))
    m_screen.screen.blit(font1.render("G",0,color), (323, 57))
    m_screen.screen.blit(font1.render("H",0,color), (361, 57))
    m_screen.screen.blit(font1.render("I",0,color), (405, 57))
    m_screen.screen.blit(font1.render("J",0,color), (443, 57))

    m_screen.screen.blit(font1.render("1",0,color), (45, 94))
    m_screen.screen.blit(font1.render("2",0,color), (45, 132))
    m_screen.screen.blit(font1.render("3",0,color), (45, 174)) 
    m_screen.screen.blit(font1.render("4",0,color), (45, 213))
    m_screen.screen.blit(font1.render("5",0,color), (45, 252))
    m_screen.screen.blit(font1.render("6",0,color), (45, 292))
    m_screen.screen.blit(font1.render("7",0,color), (42, 333))
    m_screen.screen.blit(font1.render("8",0,color), (40, 373))
    m_screen.screen.blit(font1.render("9",0,color), (45, 414))
    m_screen.screen.blit(font1.render("10",0,color), (35, 452))
#
    m_screen.screen.blit(font1.render("A",0,color), (533, 57))
    m_screen.screen.blit(font1.render("B",0,color), (574, 57))
    m_screen.screen.blit(font1.render("C",0,color), (612, 57))
    m_screen.screen.blit(font1.render("D",0,color), (651, 57))
    m_screen.screen.blit(font1.render("E",0,color), (693, 57))
    m_screen.screen.blit(font1.render("F",0,color), (735, 57))
    m_screen.screen.blit(font1.render("G",0,color), (774, 57))
    m_screen.screen.blit(font1.render("H",0,color), (811, 57))
    m_screen.screen.blit(font1.render("I",0,color), (854, 57))
    m_screen.screen.blit(font1.render("J",0,color),(894, 56))

    m_screen.screen.blit(font1.render("1",0,color), (935, 94))
    m_screen.screen.blit(font1.render("2",0,color), (935, 132))
    m_screen.screen.blit(font1.render("3",0,color), (935, 174)) 
    m_screen.screen.blit(font1.render("4",0,color), (935, 213))
    m_screen.screen.blit(font1.render("5",0,color), (935, 252))
    m_screen.screen.blit(font1.render("6",0,color), (935, 292))
    m_screen.screen.blit(font1.render("7",0,color), (935, 333))
    m_screen.screen.blit(font1.render("8",0,color), (935, 373))
    m_screen.screen.blit(font1.render("9",0,color), (935, 414))
    m_screen.screen.blit(font1.render("10",0,color), (935, 452))
#   

