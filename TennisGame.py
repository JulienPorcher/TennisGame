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
        self.l_score = [0,0]     # Number of point for each player in the game
        self.game = [0,0]        # Number of game for each player in the set
        self.dict_score = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.morethan3 = False   # If one player scores more than 3 points
        self.win = False         # If one player won the game
        self.deuce = False       # If there is a deuce
        self.advantage = False   # If there is an advantage
        
    def new_game(self):
        '''
        Initialise Bool if a new game start
        '''
        if self.l_score == [0,0]:
            self.morethan3 = False

    def point(self, player):
        '''
        Parameters
        ----------
        player : str()
            The player who won the point

        Increment the score
        '''

        # Test player name
        self.test(player)
        # Test if it's a new game
        self.new_game()

        if player == self.player_1:
            self.l_score[0] = self.l_score[0] + 1
        else:
            self.l_score[1] = self.l_score[1] + 1

    def is_deuce(self):
        '''
        If at least three points have been scored by each player, and the
        scores are equal, the score is "Deuce".
        '''
        if self.l_score[0] == self.l_score[1] and self.l_score[0] >= 3:
            self.deuce = True
            return 'Deuce'
        else:
            pass

    def as_advantage(self):
        '''
        If at least three points have been scored by each side and a player
        has one more point than his opponent, the score of the game is
        "Advantage" for the player in the lead.
        '''
        if self.l_score[0] >= 4 and self.l_score[0]-self.l_score[1] == 1:
            self.morethan3 = True
            self.advantage = True
            return str("Advantage " + self.player_1)

        elif self.l_score[1] >= 4 and self.l_score[1]-self.l_score[0] == 1:
            self.morethan3 = True
            self.advantage = True
            return str("Advantage " + self.player_2)
        else:
            pass

    def win_game(self):
        '''
        A game is won by the first player to have won at least four points in
        total and at least two points more than the opponent.
        '''
        if self.l_score[0] >= 4 and self.l_score[0]-self.l_score[1] >= 2:
            self.morethan3 = True
            self.win = True
            self.l_score = [0,0]
            self.game[0] = self.game[0] + 1
            return str("Game " + self.player_1)

        elif self.l_score[1] >= 4 and self.l_score[1]-self.l_score[0] >= 2:
            self.morethan3 = True
            self.win = True
            self.l_score = [0,0]
            self.game[1] = self.game[1] + 1
            return str("Game " + self.player_2)

        else:
            pass

    def game_score(self):
        '''
        Returns the number of games won in the set
        '''
        return str(self.player_1 + " : " + self.game[0] + ":" + self.game[1] +
                   " : " + self.player_2)

    def test(self, player):
        # Test the player name
        if player == self.player_1 or player == self.player_2:
            pass
        else:
            raise ValueError("Incorrect player name, should be " +
                             self.player_1 + " or " + self.player_2)

    def score(self):
        '''
        Return the score
        '''

        # Test if the game is won
        str_score = self.win_game()
        # Test if there is an advantage
        if self.win is False:
            str_score = self.as_advantage()
            if self.advantage is False:
                # Test if there is a Deuce
                str_score = self.is_deuce()
                # If none of the cases before, return the score
                if self.deuce is False:
                    score_p1 = self.dict_score[self.l_score[0]]
                    score_p2 = self.dict_score[self.l_score[1]]
                    str_score = str(score_p1 + " - " + score_p2)
        # Initialize Bool
        self.win = False
        self.advantage = False
        self.deuce = False

        return str(str_score)
