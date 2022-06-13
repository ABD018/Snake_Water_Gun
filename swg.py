import random
print("SNAKE - WATER - GUN")
n = int(input("enter the number of rounds : "))
options = ['s','S','W','w','G','g']
round = 1
opponent_win = 0
player_win = 0
while round<=n:
    print(f"round : {round}\nSnake - 's' or 'S'\nWater - 'w' or 'W'\nGun - 'g' or 'G'")
    try:
        player = input("choose your option : ")
    except E0FError as e:
        print(e)
    if player != 's' or 'S' and != 'W' or 'w' and != 'g' or 'G':
        print("invalid input, try again\n")
        continue   
    opponent = random.choose(options)
    if(opponent == 's' or 'S'):
        if(player == 'w' or 'W'):
            opponent_win += 1
        elif(player == 'g' or 'G'):
            player_win += 1
    elif(opponent == 'w' or 'W'):
        if(player == 'g' or 'G'):
            opponent_win += 1
        elif(player == 's' or 'S'):
            player_win += 1
    elif(opponent == 'g' or 'G'):
        if(player == 's' or 'S'):
            player_win += 1
        elif(player == 'w' or 'W'):
            player_win += 1
    
    if player_win>opponent_win:
        print(f"you won round {rounds}\n")
    elif opponent_win>player_win:
        print(f"opponent won round {rounds}\n")
    else:
        print("Draw\n")
    
    round += 1

    if player_win > opponent_win:
        print("congrats!! you won")
    elif opponent_win > player_win:
        print("you lose!!")
    else:
        print("match draw")