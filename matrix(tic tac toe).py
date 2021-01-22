print()

l=[['*','*','*'],['x','x','x'],['.','.','.']]

def prnt() :
    print(' ',1,2,3,sep='\t')
    print()
    c=1
    for i in l :
        print(c,end='\t')
        c+=1
        for k in i :
            print(k,end='\t')
        print()
        print()

play=True
while play :
    prnt()
    print('Tic Tac Toe')
    print('Do You Want To Play?')
    choice=input('Yes or No ?:')
    if choice not in 'Nono' :
        l=[['.','.','.'],['.','.','.'],['.','.','.']]
        pointr=input('Do you want to be the Star(*) or the Cross(x) [Type the symbol :')
        print('You Go First!\n')
        row=int(input('Enter the Row no. :'))
        column=int(input('Enter the Column no. :'))
        
        l[row-1][column-1]=pointr


        prnt()
    else :
        play=False
