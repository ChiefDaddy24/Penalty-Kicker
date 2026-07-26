from pk_class import *

import random
import time


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


def take_penalty(a,b,):
    goalkeeper_dive = random.randint(1,10)*b
    shot = random.randint(1,10)* a
    if goalkeeper_dive < shot:
        return 1
    else:
        return 0


def final_winner(goal_1,goal_2,name1,name2):
    if goal_1 > goal_2:
        print(f"{name1} has won todays penalty shootout  by {goal_1-goal_2} goals.")
    elif goal_2 > goal_1:
        print(f"{name2} has won todays penalty shootout  by {goal_2-goal_1} goals.")
    else:
        print(f'It was a Tie!')

def getP_info():
    name = input("Hello What is the name of this player? :")
    name = name.upper()
    ability = float(input(f"Out of 100 what is {name}'s ability?:  "))
    return name,ability

def getG_info():
        name = input("Hello What is the name of this Goalie? :")
        name = name.upper()
        ability = float(input(f"Out of 100 what is {name}'s ability?:  "))
        return name,ability

player1 = Player(*getP_info())
player2 = Player(*getP_info())
goalie = Goalie(*getG_info())

#print(player1.player_name)

p_round =1

print('And so we begin!') 
while game_over != True:

     
     print('')
     print(f'Round:{p_round}')
     b =take_penalty(player1.ability,goalie.goalie_ability)
     if b != 1:
        print(f"{goalie.goalie_name} saved the Penalty kick no score !!!")
        player1.update(0,1)
        goalie.updateG(1)
     else:
         print(f"It's a GOOOOAAAAAAALLLLLL {player1.player_name} scored the penalty!!!")
         print('Add 1 to the tally!!!')
         player1.update(1,1)
         goalie.updateG(0)
     print(f'current goal for {player1.player_name} = {player1.goals}')
     time.sleep(1)
     print('')

     
     print(f"Now it is {player2.player_name}'s turn.")
     s =take_penalty(player2.ability,goalie.goalie_ability)
     if s != 1:
        print(f"{goalie.goalie_name} saved the Penalty kick no score !!!")
        player2.update(0,1)
        goalie.updateG(1)
     else:
         print(f"It's a GOOOOAAAAAAALLLLLL {player2.player_name} scored the penalty!!!")
         print('Add 1 to the tally!!!')
         player2.update(1,1)
         goalie.updateG(0)

     print(f'current goal for {player2.player_name} = {player2.goals}')
     print('----------------------------------------')
     time.sleep(1)
     
     cc = (check_game_over(p_round,player1.goals,player2.goals))
     print(cc)
     game_over = cc
     print(game_over)
     p_round+=1
     
print(f'\n{player1.player_name} ended the day with {player1.goals} number of penalties scored on {player1.shots} penalties taken.')

print(f'\n{player2.player_name} ended the day with {player2.goals} number of penalties scored on {player2.shots} penalties taken.')
print('\n')
final_winner(player1.goals,player2.goals,player1.player_name,player2.player_name)
print(f"{goalie.goalie_name} ended the day with {goalie.saves} made")