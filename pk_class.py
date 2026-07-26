class Player :
    def __init__(self,name,ability,):
         self.player_name = name
         self.ability = ability
         self.goals = 0
         self.shots = 0

    def update(self,goal,shot):
         self.goals+= goal
         self.shots+= shot


class Goalie:
    def __init__(self,name,ability):
         self.goalie_name = name 
         self.goalie_ability = ability
         self.saves = 0

    def updateG(self,save):
         self.saves+= save
