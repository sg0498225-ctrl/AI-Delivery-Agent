from collections import deque
import heapq
import math

def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return []
    current = goal
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

class Instrumentation:
    def __init__(self):
        self.nodes_expanded = 0

def bfs(grid, start, goal):
    instr = Instrumentation()
    frontier = deque([start])
    came_from = {start: None}
    while frontier:
        current = frontier.popleft()
        instr.nodes_expanded += 1
        if current == goal:
            break
        for nb in grid.neighbors(current):
            if nb not in came_from:
                came_from[nb] = current
                frontier.append(nb)
    path = reconstruct_path(came_from, start, goal)
    return path, instr

def ucs(grid, start, goal):
    instr = Instrumentation()
    frontier = []
    heapq.heappush(frontier, (0, start))
    cost_so_far = {start: 0}
    came_from = {start: None}
    while frontier:
        cost, current = heapq.heappop(frontier)
        instr.nodes_expanded += 1
        if current == goal:
            break
        for nb in grid.neighbors(current):
            new_cost = cost_so_far[current] + grid.cost(nb)
            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                heapq.heappush(frontier, (new_cost, nb))
                came_from[nb] = current
    path = reconstruct_path(came_from, start, goal)
    return path, instr

def manhattan(a,b):
    return abs(a.r-b.r) + abs(a.c-b.c)

def a_star(grid, start, goal, heuristic=manhattan):
    instr = Instrumentation()
    frontier = []
    heapq.heappush(frontier, (0, start))
    cost_so_far = {start: 0}
    came_from = {start: None}
    while frontier:
        _, current = heapq.heappop(frontier)
        instr.nodes_expanded += 1
        if current == goal:
            break
        for nb in grid.neighbors(current):
            new_cost = cost_so_far[current] + grid.cost(nb)
            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                priority = new_cost + heuristic(nb,goal)
                heapq.heappush(frontier, (priority, nb))
                came_from[nb] = current
    path = reconstruct_path(came_from, start, goal)
    return path, instr
