from p6_game import Simulator

ANALYSIS = {}

def analyze(design):
    global ANALYSIS
    ANALYSIS = {}
    sim = Simulator(design)
    queue = []
    visited = []
    init = sim.get_initial_state()
    queue.append((init, [init]))
    visited.append(init)
    while queue:
        (state, path) = queue.pop(0)
        for next in sim.get_moves():
            next_state = sim.get_next_state(state, next)
            if next_state is not None and next_state not in ANALYSIS:
                if next_state not in visited:
                    ANALYSIS[next_state] = path
                    queue.append((next_state, path + [next_state]))
                    visited.append(next_state)

def inspect((i,j), draw_line):
    found = False
    for next in ANALYSIS:
        if (i,j) == next[0]:
            path = ANALYSIS[next]
            for n in xrange(len(path) - 1):
                found = True
                draw_line(path[n][0], path[n+1][0], offset_obj = next[1], color_obj = path[n][1])
            # draw last segment
            draw_line(path[-1][0], next[0], offset_obj = next[1], color_obj = path[-1][1])
    # cursor over black
    if not found:
        print "No path found"
