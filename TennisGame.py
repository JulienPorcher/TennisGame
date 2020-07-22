# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:26:49 2019

@author: julien porcher
"""


class TennisGame():
    # Return the score between player_1 and player_2

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score = [0,0]
        self.game = [0,0]
        self.dict_score = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.morethan3 = False
        self.win = False
        self.deuce = False
        self.advantage = False


    def Newgame(self):
        '''
        Initialise Bool if a new game start
        '''
        if self.score == [0,0]:
            self.morethan3 = False


    def Point(self, player):
        '''
        Parameters
        ----------
        player : str()
            The player who won the point

        Increment the score
        '''

        if player == self.player_1:
            self.score[0] = self.score[0] + 1
        else:
            self.score[1] = self.score[1] + 1


    def Isdeuce(self):
        '''
        If at least three points have been scored by each player, and the
        scores are equal, the score is "Deuce".
        '''
        if self.score[0] == self.score[1] and self.score[0] >= 3:
            self.deuce = True
            return 'Deuce'
        else:
            pass


    def Asadvantage(self):
        '''
        If at least three points have been scored by each side and a player
        has one more point than his opponent, the score of the game is
        "Advantage" for the player in the lead.
        '''
        if self.score[0] >= 4 and self.score[0]-self.score[1] == 1:
            self.morethan3 = True
            self.advantage = True
            return str("Advantage " + self.player_1)

        elif self.score[1] >= 4 and self.score[1]-self.score[0] == 1:
            self.morethan3 = True
            self.advantage = True
            return str("Advantage " + self.player_2)
        else:
            pass


    def Game(self):
        '''
        A game is won by the first player to have won at least four points in
        total and at least two points more than the opponent.
        '''
        if self.score[0] >= 4 and self.score[0]-self.score[1] >= 2:
            self.morethan3 = True
            self.win = True
            self.score = [0,0]
            self.game[0] = self.game[0] + 1
            return str("Game " + self.player_1)
            

        elif self.score[1] >= 4 and self.score[1]-self.score[0] >= 2:
            self.morethan3 = True
            self.win = True
            self.score = [0,0]
            self.game[0] = self.game[0] + 1
            return str("Game " + self.player_2)

        else:
            pass


    def Gamescore(self):
        '''
        Returns the number of games won in the set
        '''
        return str(self.player_1 + " : " + self.game[0] + ":" + self.game[1] +
                   " : " + self.player_2)


    def Score(self,player):
        '''
        Return the score
        '''
        # Test if it's a new game
        self.Newgame()
        # Increment the score
        self.Point(player)
        # Test if the game is won
        str_score = self.Game()
        print(str_score)
        # Test if there is an advantage
        if self.win is False:
            str_score = self.Asadvantage()
            print(str_score)
            if self.advantage is False:
                # Test if there is a Deuce
                str_score = self.Isdeuce()
                print(str_score)
                # If none of the cases before, return the score
                if self.deuce is False:
                    score_p1 = self.dict_score[self.score[0]]
                    score_p2 = self.dict_score[self.score[1]]
                    str_score = str(score_p1 + " - " + score_p2)
        # Initialize Bool
        self.win = False
        self.advantage = False
        self.deuce = False

        return str(str_score)