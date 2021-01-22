###Rock Paper Scissors

import random

#no.of rounds to be played
rounds=int(input('\nEnter the number of rounds you want to play :'))
wins=ties=losses=0
game_count=1

#initializing dictionary of playable values
playable={1:'ROCK',2:'PAPER',3:'SCISSORS'}

#Outputs which are to be printed
win1="You've Won!"
win2='Total Wins :'

loose1='You Lost!'
loose2='Total Losses :'

tie1="It's A Tie!"
tie2='Total Ties :'

c_out='Computer played :'
msg1='Enter Your Choice Again'
nw1='\n'
ask1='Do You Want To Continue?'

err2='!Invalid Input!'
err1='ERROR'

thnx1='Thank You For Playing!!'
thnx2='Looking Forward To seeing You Again :)'

leave1='Do You Want To Restart The Game?'

sorry="Sorry You'll Have To Restart The Program Yourself ;("

#Defining the various Functions

#computers played o/p
def play() :
    rand_num=random.randint(1,3)
    return (playable[rand_num] , rand_num)

#checking for validity of user's ans
def check_valid(inp) :
    checked='no'
    for i in playable :
        if playable[i]==inp :
            checked='yes'
    return checked

#geting the key of user's i/p
def getkey(val):
    for i in playable :
        if playable[i]==val :
            return i

#user's i/p
def user_inp() :
    temp=input('Enter your played choice :')
    return temp.upper()

#checking if user lost
def check_lost() :
    global losses
    checked='tie'
    loosing_num=user_val+1
    if user_val==3 :
        loosing_num=1
    if comp_val==loosing_num :
        checked='lost'
        losses+=1
        print(nw1,loose1,nw1,loose2,losses,sep='')
    return checked

#checing if user won
def check_win() :
    checked='tie'
    winning_num=user_val-1
    if user_val==1 :
        winning_num=3
    if comp_val==winning_num :
        checked='win'
    return checked

#asking to play again
def question() :
    temp=input('Enter your Answer :')
    return temp.lower()


#start of the game

while rounds>0 :

    print(f'\nGame {game_count}')

    #inputs
    user_choice=user_inp()
    validity=check_valid(user_choice)

    #if user's i/p is invalid
    if validity != 'yes' :
        print(nw1,err1,nw1,err2,nw1,msg1,sep='')
        continue
    
    user_val=getkey(user_choice)
    comp_choice,comp_val=play()

    #printing the computer's play
    print(c_out,comp_choice)

    #checking if user lost
    checked=check_lost()

    #knowing whether user has won or gotten a tie
    if checked != 'lost' :
        #checking if user wins
        checked=check_win()
        if checked=='win' :
            wins+=1
            print(nw1,win1,nw1,win2,wins,sep='')
        else :
           ties+=1
           print(nw1,tie1,nw1,tie2,ties,sep='')

    #asking to play again
    print(nw1,ask1,sep='')
    asked=question()
    if asked == 'no' :
        rounds=0
    else :
        rounds-=1
        game_count+=1

#end of while loop

#asking if user want's to play again
else :
    #printing result
    print(f"\nYour Result : \nWins : {wins} \nLosses : {losses} \nTies : {ties}")
    #asking to restart
    print(nw1,leave1,sep='')
    asked=question()
    if asked == 'yes' :
        print(sorry)
    print(nw1,thnx1,nw1,thnx2,sep='')
