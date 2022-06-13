import random
print("SNAKE - WATER - GUN")
n = int(input("enter the number of rounds : "))
options = ['s','w','g']
round = 1
opponent_win = 0
player_win = 0
while round<=n:
    print(f"round : {round}\nSnake - 's'\nWater - 'w'\nGun - 'g'")
    try:
        player = input("choose your option : ")
    except E0FError as e:
        print(e)
    if player != 's' and player != 'w' and player != 'g':
        print("invalid input, try again\n")
        continue   
    opponent = random.choice(options)
    if(opponent == 's'):
        if(player == 'w'):
            opponent_win += 1
        elif(player == 'g'):
            player_win += 1
    elif(opponent == 'w'):
        if(player == 'g'):
            opponent_win += 1
        elif(player == 's'):
            player_win += 1
    elif(opponent == 'g'):
        if(player == 's'):
            player_win += 1
        elif(player == 'w'):
            player_win += 1
    
    if player_win>opponent_win:
        print(f"you won round {round}\n")
    elif opponent_win>player_win:
        print(f"opponent won round {round}\n")
    else:
        print("Draw\n")
    
    round += 1

    if player_win > opponent_win:
        print("congrats!! you won")
    elif opponent_win > player_win:
        print("you lose!!")
    else:
        print("match draw")