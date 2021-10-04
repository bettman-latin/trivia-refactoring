#!/usr/bin/env python3
#test
#correct V
#self.players[currenty_player].whatever


class Player:
    def __init__(self, n):
        self.name = n
        self.places = 0
        self.purses = 0
        self.in_penalty_box = 0

class Questions:
    def __init__(self):
        
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)
            
    def _current_category(self, current):
        if current.places % 4 == 0: 
            return 'Pop'
        elif current.places % 4 == 1:
            return 'Science'
        elif current.places % 4 == 2: 
            return 'Sports'
        else:
            return 'Rock'

    def _ask_question(self, current):
        if self._current_category(current) == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category(current) == 'Science': print(self.science_questions.pop(0))
        if self._current_category(current) == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category(current) == 'Rock': print(self.rock_questions.pop(0))

#link Player Class to game class
#current-category is messed up

class Game:
    def __init__(self):

        self.players = []
        self.questions = Questions()

        # self.current_questions = 0
        self.current_player = 0
        self.is_getting_out_of_penalty_box = False


#removed create_rock question function

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        newPlayer = Player(player_name)
        self.players.append(newPlayer)
 
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    # def addQ(self, question):
    #     newQuestion = Questions(question)
    #     self.questions.append(newQuestion)


    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.current_player)
        print("They have rolled a %s" % roll)

        if self.players[self.current_player].in_penalty_box: #if player is in penalty box
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.current_player)
                self.continue_roll(roll)
            else:
                print("%s is not getting out of the penalty box" % self.current_player)
                self.is_getting_out_of_penalty_box = False
        else:
            self.continue_roll(roll)


    def continue_roll(self, roll):
        current = self.players[self.current_player]

        current.places = current.places + roll
        if  current.places > 11:
            current.places = current.places - 12

        print(current.name + \
                    '\'s new location is ' + \
                    str(current.places))
        print("The category is %s" % self.questions._current_category(current))
        self.questions._ask_question(current)

    def was_correctly_answered(self):
        if self.players[self.current_player].in_penalty_box:
            if self.is_getting_out_of_penalty_box:
                self.answer_was_correct_()
            else:
                self.advace_current_player()
                return True
        else:
            self.answer_was_correct_()

    def answer_was_correct_(self):
        current = self.players[self.current_player]
        print('Answer was correct!!!!')
        current.purses += 1
        print(current.name + \
            ' now has ' + \
            str(current.purses) + \
            ' Gold Coins.')

        winner = self._did_player_win()
        self.advace_current_player()

        return winner

    def wrong_answer(self):
        current = self.players[self.current_player]
        print('Question was incorrectly answered')
        print(current.name + " was sent to the penalty box")
        current.in_penalty_box = True
        
        self.advace_current_player()
        return True

    def _did_player_win(self):
        return not (self.players[self.current_player].purses == 6)


    def advace_current_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

from random import randrange

if __name__ == '__main__':
    not_a_winner = False
    
    game = Game()
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break


#player object (name, purse, penalty)
#game (list of players from player class, roll,  )


#work on more refactoring
#duplication
#if 2 lines or more, and if they appear more than once 

#take game class, and slit into game and question
