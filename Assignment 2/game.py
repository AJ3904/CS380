import util
from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, character):
        self.character = character

    @abstractmethod
    def choose_action(self, state):
        pass

class Game():

    def __init__(self, player1, player2, state):
        self.__state = state
        self.__player1 = player1
        self.__player2 = player2
        self.__states = [state]
    
    def play(self):
        while self.__state.is_game_over() == False:
            self.__state = self.__player1.choose_action(self.__state)
            self.__states.append(self.__state)
            util.pprint(self.__state)
            if self.__state.is_game_over() == False:
                self.__state = self.__player2.choose_action(self.__state)
                self.__states.append(self.__state)
                util.pprint(self.__state)
        
        if self.__state.get_winner() is None:
            print("It was a draw")
        else:
            print(self.__state.get_winner(), "wins")
            
        util.pprint(self.__states)