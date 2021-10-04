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


class Game:
    def __init__(self):

        self.players = []        

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

#removed create_rock question function

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        newPlayer = Player(player_name)
        self.players.append(newPlayer)
 
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

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
        print("The category is %s" % self._current_category)
        self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        current = self.players[self.current_player]
        if current.places % 4 == 0: 
            return 'Pop'
        elif current.places % 4 == 1:
            return 'Science'
        elif current.places % 4 == 2: 
            return 'Sports'
        else:
            return 'Rock'

    def was_correctly_answered(self):
        if self.players[self.current_player].in_penalty_box:
            if self.is_getting_out_of_penalty_box:
                self.answer_was_correct_()
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
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
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

        return winner

    def wrong_answer(self):
        current = self.players[self.current_player]
        print('Question was incorrectly answered')
        print(current.name + " was sent to the penalty box")
        current.in_penalty_box = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.players[self.current_player].purses == 6)




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
