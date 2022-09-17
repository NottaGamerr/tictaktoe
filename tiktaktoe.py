import random

def p():

    for i in range(3):
    
        for j in range(3):
        
            print(b[i][j], end = ' ')
            
        print()
    
    print()
    print()
      
def x(r,c):
    b[r][c]='x'
    
def o(r,c):
    b[r][c]='o'

def x_turn():

    global dia_num
    global oppdia_num

    column = int(input('Enter column 1 - 3: '))

    row = int(input('Enter row 1 - 3: '))

    if (row<4) and (column<4):
        
        if (b[row-1][column-1]=='-'):
            
            x(row-1,column-1)

            row_num[row-1] += 1
            col_num[column-1] += 1

            if row == column:
                dia_num = dia_num + 1
                
            if row == 3 and column == 1:
                oppdia_num = oppdia_num + 1
            elif row == 2 and column == 2:
                oppdia_num = oppdia_num + 1
            elif row == 3 and column == 1:
                oppdia_num = oppdia_num + 1
        
            
            
        else:
            print('You must place x in an empty space.')

            x_turn()
    else:
        print('Row and column must be from 1 to 3.')

        x_turn()

def ai_turn():
    
    column = random.randint(1,3)
    row = random.randint(1,3)

    if (b[row-1][column-1]=='-'):
    
        o(row-1,column-1)

        row_num2[row-1] += 1
        col_num2[column-1] += 1
     
    else:
        ai_turn()

def win_check():

    global gamewon
    
    if 3 in row_num:
        
        print("You Win!")
        gamewon = True
        
    elif 3 in col_num:
        
        print("You Win!")
        gamewon = True

    elif 3 in row_num2:
        
        print("AI Wins!")
        gamewon = True
        
    elif 3 in col_num2:
        
        print("AI Wins!")
        gamewon = True

    elif dia_num == 3:
        
        print("You Win!")
        gamewon = True
        
    elif oppdia_num == 3:
        
        print("You Win!")
        gamewon = True

    elif dia_num2 == 3:

        print("AI Wins!")
        gamewon = True
        
    



b = [['-','-','-'],['-','-','-'],['-','-','-']]

row_num = [0,0,0]
col_num = [0,0,0]
dia_num = 0
oppdia_num = 0

row_num2 = [0,0,0]
col_num2 = [0,0,0]
dia_num2 = 0

gamewon = False

turn = "x"

p()

while gamewon == False:

    if turn == "x":
        
        x_turn()
        win_check()
        p()
        turn = "o"
        
    else:

        ai_turn()
        win_check()
        p()
        turn = "x"
        


