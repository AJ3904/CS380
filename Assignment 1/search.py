import util
import iq
import agent

def heuristic(state):
    possible_moves = len(state.get_actions())
    peg_count = state.count_pegs()
    return possible_moves - peg_count

if __name__ == "__main__":

    cmd = util.get_arg(1)

    string = util.get_arg(2) or iq.DEFAULT_STATE
    state = iq.State(string)
    search_agent = agent.Agent()

    if cmd == "random":
        states = search_agent.random_walk(state)
        util.pprint(states)
    elif cmd == "bfs":
        search_agent.BFS(state)
    elif cmd == "dfs":
        search_agent.DFS(state)
    elif cmd == "a_star":
        search_agent.a_star(state, heuristic)