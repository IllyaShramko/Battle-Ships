import pygame
import modules.data as m_data
import modules.settings as m_settings
import modules.screen as m_screen
import modules.ship as m_ship
import random
list_1 = [[0,0,0,0],
           [0,0,0],
            [0,0],
             [0]
              ]
ships_1 = 0
ships_3 = 0
ships_2 = 0
ships_4 = 0

             
while ships_4 < 1:
    rotate = random.randint(0,1) * 90
    ship_4_1_1 = random.randint(0,9)
    ship_4_2_1 = random.randint(0,9)
    print(3444444444444444444444444444)
    if rotate % 180 == 0:
        if ship_4_2_1 < 7:
            if m_data.list_cell2[ship_4_1_1][ship_4_2_1] == 0:
                if m_data.list_cell2[ship_4_1_1][ship_4_2_1+1] == 0:
                    if m_data.list_cell2[ship_4_1_1][ship_4_2_1+2] == 0: 
                        if m_data.list_cell2[ship_4_1_1][ship_4_2_1+3] == 0: 
                            m_data.enemy_pos(4,ship_4_1_1,ship_4_2_1) 
                            list_1[3][0] = rotate  
                            ships_4=1
    else:
        if ship_4_1_1 < 7:
            if m_data.list_cell2[ship_4_1_1][ship_4_2_1] == 0:
                if m_data.list_cell2[ship_4_1_1+1][ship_4_2_1] == 0:
                    if m_data.list_cell2[ship_4_1_1+2][ship_4_2_1] == 0: 
                        if m_data.list_cell2[ship_4_1_1+3][ship_4_2_1] == 0: 
                            m_data.enemy_pos(4,ship_4_1_1,ship_4_2_1,rotate) 
                            list_1[3][0] = rotate  
                            ships_4=1
while ships_3 < 2:
    rotate = random.randint(0,1) * 90
    ship_3_1_1 = random.randint(0,9)
    ship_3_2_1 = random.randint(0,9)
    print(3333333333333333333333334)
    if rotate % 180 == 0:
        if ship_3_2_1 < 8:
            if m_data.list_cell2[ship_3_1_1][ship_3_2_1] == 0:
               if m_data.list_cell2[ship_3_1_1][ship_3_2_1+1] == 0:
                   if m_data.list_cell2[ship_3_1_1][ship_3_2_1+2] == 0: 
                       m_data.enemy_pos(3,ship_3_1_1,ship_3_2_1)
                       list_1[2][ships_3] = rotate   
                       ships_3 +=1
    elif rotate % 180 != 0:
        if ship_3_1_1 < 8:
            if m_data.list_cell2[ship_3_1_1][ship_3_2_1] == 0:
                if m_data.list_cell2[ship_3_1_1+1][ship_3_2_1] == 0:
                    if m_data.list_cell2[ship_3_1_1+2][ship_3_2_1] == 0: 
                        m_data.enemy_pos(3,ship_3_1_1,ship_3_2_1,rotate)
                        list_1[2][ships_3] = rotate   
                        ships_3 +=1  
while ships_2 < 3:
    print(3322222222222222222222222222222)
    rotate = random.randint(0,1) * 90
    ship_2_1_1 = random.randint(0,9)
    ship_2_2_1 = random.randint(0,9)
    if rotate % 180 == 0:
        if ship_2_2_1 < 9:
            if m_data.list_cell2[ship_2_1_1][ship_2_2_1] == 0:
                if  m_data.list_cell2[ship_2_1_1][ship_2_2_1+1] == 0: 
                    m_data.enemy_pos(2,ship_2_1_1,ship_2_2_1)
                    list_1[1][ships_2] = rotate   
                    ships_2 +=1
    else:
        if ship_2_1_1 < 9:
            if m_data.list_cell2[ship_2_1_1][ship_2_2_1] == 0:
                if m_data.list_cell2[ship_2_1_1+1][ship_2_2_1] == 0: 
                    m_data.enemy_pos(2,ship_2_1_1,ship_2_2_1,rotate)
                    list_1[1][ships_2] = rotate   
                    ships_2 +=1   
while ships_1 < 4:
    print(311111111111111111111111111111111111111111111111)
    rotate = random.randint(1,9) * 90
    ship_1_1_1 = random.randint(0,9)
    ship_1_2_1 = random.randint(0,9)
    if m_data.list_cell2[ship_1_1_1][ship_1_2_1] == 0: 
        m_data.enemy_pos(1,ship_1_1_1,ship_1_2_1, rotate)
        list_1[0][ships_1] = rotate
        ships_1 +=1







for count in range(10):
    print(m_data.list_cell2[count])
print()
for count in range(10):
    print(m_data.list_cell1[count])


# 2 2 0
def check(row, cell):
    
    if cell<9 and  m_data.list_cell2[row][cell+1] ==m_data.list_cell2[row][cell]//10:
        return 0
    else:
        return 90

# pygame.transform.rotate()
class Bot(m_settings.Settings):
    def __init__(self,width1=40,height1=40, x1 = 0, y1=0, name_file1= None, rotate1=False, rotate2= False):
        global list_1
        m_settings.Settings.__init__(self,width=width1, height=height1, x=x1, y=y1, name_file=name_file1, rotate=rotate1, T_F_rotate=rotate2)
        
        self.X2, self.Y2 = x1, y1
        self.load_image()
        self.X3 = self.X
        self.ROTATE1 =list_1
    def place(self):
        # count3 = [0,0,0,0]
        #3 0 3
        #n 0 n
        #3 0 n
        for count in range(10):
            for count1 in range(10):
                if m_data.list_cell2[count][count1] == 1:
                    ship = m_ship.Ship(x1=self.X2, y1=self.Y2, name_file1="img/1.png", rotate1=self.ROTATE1[0][0])
                    del self.ROTATE1[0][0]
                    ship.load_image()
                    ship.CELLS=[[count, count1]]#
                    m_data.enemy_list_ships.append(ship)
                if m_data.list_cell2[count][count1] == 22:
                    ship = m_ship.Ship(width1=80, x1=self.X2, y1=self.Y2, name_file1="img/2.png", rotate1=check(count, count1))
                    del self.ROTATE1[1][0]
                    ship.load_image()
                    if check(count, count1):
                        ship.CELLS=[[count, count1],[count+1, count1]]#
                    else:
                        ship.CELLS=[[count, count1],[count, 1+count1]]#
                    m_data.enemy_list_ships.append(ship)
                if m_data.list_cell2[count][count1] == 33:
                    ship = m_ship.Ship(width1=120,x1=self.X2, y1=self.Y2, name_file1="img/3.png", rotate1=check(count, count1))
                    del self.ROTATE1[2][0]
                    ship.load_image()
                    if check(count, count1):
                        ship.CELLS=[[count, count1],[count+1, count1],[count+2, count1]]#
                    else:
                        ship.CELLS=[[count, count1],[count, count1+1],[count, count1+2]]#
                    # ship.CELLS.append([count, count1])#
                    m_data.enemy_list_ships.append(ship)
                if m_data.list_cell2[count][count1] == 44:
                    ship = m_ship.Ship(width1=160, x1=self.X2, y1=self.Y2, name_file1="img/4.png", rotate1=check(count, count1))
                    del self.ROTATE1[3][0]
                    ship.load_image()
                    if check(count, count1):
                        ship.CELLS=[[count, count1],[count+1, count1],[count+2, count1],[count+3, count1]]#
                    else:
                        ship.CELLS=[[count, count1],[count, count1+1],[count, count1+2],[count, count1+3]]#
                    # ship.CELLS.append([count, count1])#
                    m_data.enemy_list_ships.append(ship)
                self.X2 += 40
            self.Y2 += 40
            self.X2 = self.X3
        #self.X2 = self.X
        #self.Y2 = self.Y

            
 

ship_1_1 = Bot(x1 = 525, y1 = 100,name_file1 = "img/1.png")
#m_data.enemy_list_ships.append(ship_1_1)
ship_1_1.place()

