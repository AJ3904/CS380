import game

class HumanPlayer(game.Player):

    def __init__(self, character):
        super().__init__(character)

    def choose_action(self, state):
        actions = state.get_actions(self.character)
        for i in range(len(actions)):
            print(i, actions[i], sep = ": ")
        action_index = int(input("Please choose an action: "))
        state = state.execute(actions[action_index])
        return state