# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:26:49 2019

@author: julien porcher
"""


class TennisGame():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score = [0,0]
        self.dict_score = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.morethan3 = False


    def Point(self, player):

        if player == self.player_1:
            self.score[0] = self.score[0] + 1
        else:
            self.score[1] = self.score[1] + 1


    def Isdeuce(self):

        if self.score[0] == self.score[1] and self.score[0] >= 3:
            print('Deuce')
        else:
            pass


    def Asadvantage(self):

        if self.score[0] >= 4 and self.score[0]-self.score[1] == 1:
            self.morethan3 = True
            print("Advantage " + self.player_1)

        elif self.score[1] >= 4 and self.score[1]-self.score[0] == 1:
            self.morethan3 = True
            print("Advantage " + self.player_2)
        else:
            pass


    def Game(self):

        if self.score[0] >= 4 and self.score[0]-self.score[1] >= 2:
            self.morethan3 = True
            self.score = [0,0]
            print("Game " + self.player_1)
            

        elif self.score[1] >= 4 and self.score[1]-self.score[0] >= 2:
            self.morethan3 = True
            self.score = [0,0]
            print("Game " + self.player_2)
            

    def Score(self):

        self.Isdeuce()

        self.Asadvantage()

        self.Game()

        if self.morethan3 == False:
            score_p1 = self.dict_score[self.score[0]]
            score_p2 = self.dict_score[self.score[1]]
            print(score_p1 + " - " + score_p2)