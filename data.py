import pygame
#import modules.path_to_file as m_path
import modules.screen as m_screen
import modules.ship as m_ship
import random
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
        
    global start 
    # #
    x = coordinate[0]
    y = coordinate[1]


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
                        
                                print(list_cell1)
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
                            #ludi i gitler i vernulsa vam vsem tututututututututu
                            # pri stalene takogo NE BULO!!
                            # pomni angely ne spat oni smotrat na teba
                            # gde proshla tu tam upala zvezda tam svetila luna i igrala volna
                            # lorax uxodit
                            # skibidi toilet
                            #                   
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
    global list_cell1, list_cell2, font_win, win
    text= None
    if check_win(list_cell1):
        text = "Поразка!"
        color = (255,25,25)
    elif check_win(list_cell2):
        text = "Перемога!"
        color = (25,255,25)
    if text != None:
        win = 1
        m_screen.screen.blit(font_win.render(text,0,color), (300, 25))