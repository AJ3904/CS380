from cmath import inf
import game, random, copy

class RandomPlayer(game.Player):

    def __init__(self, character):
        super().__init__(character)

    def choose_action(self, state):
        actions = state.get_actions(self.character)
        action = random.choice(actions)
        state = state.execute(action)
        return state

class MinimaxPlayer(game.Player):

    def __init__(self, character):
        super().__init__(character)
        self.opp_character = "O" if character == "X" else "X"

    def choose_action(self, state):
        actions = state.get_actions(self.character)
        scores = []
        for action in actions:
            copy_state = copy.deepcopy(state)
            copy_state = copy_state.execute(action)
            scores.append(self.min_value(copy_state, 1))
        best_action = actions[scores.index(max(scores))]
        state = state.execute(best_action)
        return state

    def max_value(self, state, depth):
        if state.is_game_over() != False:
            return self.utility(state, depth)
        v = float(-inf)
        actions = state.get_actions(self.character)
        for action in actions:
            copy_state = copy.deepcopy(state)
            copy_state = copy_state.execute(action)
            v = max(v, self.min_value(copy_state, depth + 1))
        return v
    
    def min_value(self, state, depth):
        if state.is_game_over() != False:
            return self.utility(state, depth)
        v = float(inf)
        actions = state.get_actions(self.opp_character)
        for action in actions:
            copy_state = copy.deepcopy(state)
            copy_state = copy_state.execute(action)
            v = min(v, self.max_value(copy_state, depth + 1))
        return v

    def utility(self, state, depth):
        if state.get_winner() == self.character:
            return 1/depth
        elif state.get_winner() == self.opp_character:
            return -1/depth
        else:
            return 0

class MinimaxAlphaBetaPlayer(game.Player):
    def __init__(self, character):
        super().__init__(character)
        self.opp_character = "O" if character == "X" else "X"

    def choose_action(self, state):
        actions = state.get_actions(self.character)
        scores = []
        for action in actions:
            copy_state = copy.deepcopy(state)
            copy_state = copy_state.execute(action)
            scores.append(self.min_value(copy_state, 1))
        best_action = actions[scores.index(max(scores))]
        state = state.execute(best_action)
        return state

    def max_value(self, state, depth, alpha = float(-inf), beta = float(inf)):
        if state.is_game_over() != False:
            return self.utility(state, depth)
        v = float(-inf)
        actions = state.get_actions(self.character)
        for action in actions:
            copy_state = copy.deepcopy(state)
            copy_state = copy_state.execute(action)
            v = max(v, self.min_value(copy_state, depth + 1, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, depth, alpha = float(-inf), beta = float(inf)):
        if state.is_game_over() != False:
            return self.utility(state, depth)
        v = float(inf)
        actions = state.get_actions(self.opp_character)
        for action in actions:
            copy_state = copy.deepcopy(state)
            copy_state = copy_state.execute(action)
            v = min(v, self.max_value(copy_state, depth + 1, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def utility(self, state, depth):
        if state.get_winner() == self.character:
            return 1/depth
        elif state.get_winner() == self.opp_character:
            return -1/depth
        else:
            return 0