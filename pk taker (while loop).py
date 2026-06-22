import random
import time

#simulate a penalty shootout

game_over = False

def check_winner(goals_a, goals_b):
    if goals_b> goals_a:
        return 0
    else:
        return 1

def check_game_over(penalty_round, goal_a, goal_b):
    if penalty_round>= 4:
        if goal_a > goal_b or goal_b > goal_a:
            return True
        else:
            return False 

    else:
        return False

def who_won(a,b,c):
    if a >0:
        print(f'Congratulations Player{b} you won the penalty shoot-out!')
    else:
        print(f'Congratulations Player{c} you won the penalty shoot-out!')
'''    
a = 4
b = int(input('How many goals did player 1 score?'))
c = int(input('How many goals did player 1 score?'))

cc = check_winner(a,b)

ans =(check_game_over(a,b,c))
who_won(cc,b,c)
print(str(ans))
         
game_over = ans
print(str(game_over))
'''

goal_1 = 0
def take_penalty(a,b,):
    goalkeeper_dive = random.randint(1,10)*b
    shot = random.randint(1,10)* a
    if goalkeeper_dive < shot:
        return 1
    else:
        return 0
    

def final_winner(goal_1,goal_2):
    if goal_1 > goal_2:
        print(f"{player_1} has won todays penalty shootout  by {goal_1-goal_2} goals.")
    elif goal_2 > goal_1:
        print(f"{player_2} has won todays penalty shootout  by {goal_2-goal_1} goals.")
    else:
        print(f'It was a Tie!')
'''
print(goal_1)

print ( player_ability, goalie_ability)
for i in range(10):
   
    
print (goal_1)
'''


'''penalty_shots = 10
goals = 0
'''

player_1 = input('Hello player 1 what is your name? : ')
player_2 = input('Hello player 2 what is your name? : ')
goalie_name= input('What is the name of the goal keeper you both be will be going against? :')
player_1 = player_1.upper()
player_2 = player_2.upper()
goalie_name= goalie_name.upper()
player1_ability = float(input(f"Out of a 100 what is {player_1}'s Penalty kick abilty? :"))/100
player2_ability = float(input("Out of a 100 what is {player_2}'s Penalty kick abilty? :"))/100
goalie_ability = float(input(f"Out of a 100 what is the  abilty of {goalie_name.upper()}? :"))/100

goal_2 = 0
p_round = 1
cc = True
print('And so we begin!') 
while game_over != True:

     
     print('')
     print(f'Round:{p_round}')
     b =take_penalty(player1_ability,goalie_ability)
     if b != 1:
        print(f"{goalie_name} saved the Penalty kick no score !!!")
     else:
         print(f"It's a GOOOOAAAAAAALLLLLL {player_1} scored the penalty!!!")
         print('Add 1 to the tally!!!')
     goal_1 +=b
     print(f'current goal for {player_1} = {goal_1}')
     time.sleep(1)
     print('')

     
     print(f"Now it is {player_2}'s turn.")
     s =take_penalty(player2_ability,goalie_ability)
     if s != 1:
        print(f"{goalie_name} saved the Penalty kick no score !!!")
     else:
         print(f"It's a GOOOOAAAAAAALLLLLL {player_2} scored the penalty!!!")
         print('Add 1 to the tally!!!')
     goal_2 +=s
     print(f'current goal for {player_2} = {goal_2}')
     print('----------------------------------------')
     time.sleep(1)
     
     cc = (check_game_over(p_round,goal_1,goal_2))
     print(cc)
     game_over = cc
     print(game_over)
     p_round+=1
     
print(f'\n{player_1} ended the day with {goal_1} number of penalties scored')

print(f'\n{player_2} ended the day with {goal_2} number of penalties scored')
print('\n')
final_winner(goal_1,goal_2)
   
