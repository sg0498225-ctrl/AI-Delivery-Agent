import math, random, time
from search import a_star

def path_cost(grid, path):
    if not path: return math.inf
    cost = 0
    for p in path[1:]:
        cost += grid.cost(p)
    return cost

def simulated_annealing_replan(grid, path, start, goal, time_limit=1.0):
    if not path:
        return path
    best = path[:]
    best_cost = path_cost(grid,best)
    cur = best[:]
    cur_cost = best_cost
    t0 = time.time()
    while time.time() - t0 < time_limit:
        if len(cur) < 4:
            break
        i = random.randint(0, len(cur)-3)
        j = random.randint(i+2, len(cur)-1)
        a = cur[i]
        b = cur[j]
        subpath, _ = a_star(grid, a, b)
        if not subpath:
            continue
        new_path = cur[:i] + subpath + cur[j+1:]
        new_cost = path_cost(grid, new_path)
        delta = new_cost - cur_cost
        T = max(0.001, 1.0 - (time.time()-t0)/time_limit)
        accept = False
        if delta < 0:
            accept = True
        else:
            if random.random() < math.exp(-delta / (T*10 + 1e-9)):
                accept = True
        if accept:
            cur = new_path
            cur_cost = new_cost
            if cur_cost < best_cost:
                best = cur[:]
                best_cost = cur_cost
    return best
