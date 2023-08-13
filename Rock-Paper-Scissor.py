# import random packages
from random import randint

# define game rule function
def gameRule(uOpt):
    # declare global variable
    global userPoint, compPoint, count

    # choose option for computer
    cOpt= randint(1,3)

    # option name for computer
    if cOpt== 1:
        cmpoptionName= 'Rock'
    if cOpt== 2:
        cmpoptionName= 'Paper'
    if cOpt== 3:
        cmpoptionName= 'Seissor'
    
    # option name for user
    if uOpt== 1:
        useroptionName= 'Rock'
    if uOpt== 2:
        useroptionName= 'Paper'
    if uOpt== 3:
        useroptionName= 'Seissor'

    # print both choice
    print(f'\nUser Choose: {useroptionName} & Computer Choose: {cmpoptionName}')

    # design game rule
    if uOpt== cOpt:
        print('It\'s Draw')
        count+=1
    if uOpt==1 and cOpt==2:
        print('Computer Win')
        compPoint+=1
        count+=1
    if uOpt==1 and cOpt==3:
        print('User Win')
        userPoint+=1
        count+=1
    if uOpt==2 and cOpt==1:
        print('User Win')
        userPoint+=1
        count+=1
    if uOpt==2 and cOpt==3:
        print('Computer Win')
        compPoint+=1
        count+=1
    if uOpt==3 and cOpt==1:
        print('Computer Win')
        compPoint+=1
        count+=1
    if uOpt==3 and cOpt==2:
        print('User Win')
        userPoint+=1
        count+=1

# define game result funcion
def gameResult():
    global userPoint, compPoint, count
    print(f'\nTotal Round: {count}\nDraw Round:{count-(userPoint+compPoint)}\nUser Won: {userPoint}\nComputer Won: {compPoint}')

# define main function
if __name__=="__main__":
    userPoint= 0
    compPoint= 0
    count= 0

# not-ending loop until user decide
    while True:
        print('\n\nPress 1 for Rock\nPress 2 for Paper\nPress 3 for Scissor\nPress Q for Quit and display Result')
        userOption= input('\nEnter Your Option: ')

        if userOption== '1':
            gameRule(uOpt= 1)
        elif userOption== '2':
            gameRule(uOpt= 2)
        elif userOption== '3':
            gameRule(uOpt= 3)
        elif userOption.upper()== 'Q':
            gameResult()
            break
        else:
            print('Choose Correct Option')