import util, game, agent, human, connect3

if __name__ == "__main__":
    player1 = util.get_arg(1)
    player2 = util.get_arg(2)
    stateString = util.get_arg(3)
    state = connect3.State(stateString)

    if player1 == "human":
        player1 = human.HumanPlayer("X")
    elif player1 == "random":
        player1 = agent.RandomPlayer("X")
    elif player1 == "minimax":
        player1 = agent.MinimaxPlayer("X")
    elif player1 == "minimaxalphabeta":
        player1 = agent.MinimaxAlphaBetaPlayer("X")
    else:
        print("Invalid player1")

    if player2 == "human":
        player2 = human.HumanPlayer("O")
    elif player2 == "random":
        player2 = agent.RandomPlayer("O")
    elif player2 == "minimax":
        player2 = agent.MinimaxPlayer("O")
    elif player2 == "minimaxalphabeta":
        player2 = agent.MinimaxAlphaBetaPlayer("O")
    else:
        print("Invalid player2")
    
    start_game = game.Game(player1, player2, state)
    start_game.play()