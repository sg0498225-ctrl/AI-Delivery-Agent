import argparse, math
from grid import Grid, Node
from search import bfs, ucs, a_star
from local_search import simulated_annealing_replan, path_cost

SMALL_MAP = open('maps/small_map.txt').read()
MEDIUM_MAP = open('maps/medium_map.txt').read()
LARGE_MAP = open('maps/large_map.txt').read()
DYNAMIC_MAP = open('maps/dynamic_map.txt').read()

def run_planner(grid, start, goal, algorithm='astar', replanner=None):
    if algorithm == 'bfs':
        planner = bfs
    elif algorithm == 'ucs':
        planner = ucs
    else:
        planner = a_star
    path, instr = planner(grid, start, goal)
    total_expanded = instr.nodes_expanded
    total_cost = path_cost(grid, path)
    return {'path':path, 'cost':total_cost, 'expanded':total_expanded}

def sample_experiments():
    examples = [ ('small', SMALL_MAP, Node(0,0), Node(4,4)),
                 ('medium', MEDIUM_MAP, Node(0,0), Node(4,6)),
                 ('large', LARGE_MAP, Node(0,0), Node(6,8)) ]
    for name, text, s,g in examples:
        grid = Grid.from_text(text)
        for alg in ['bfs','ucs','astar']:
            r = run_planner(grid, s, g, algorithm=alg)
            print(name,alg,r['cost'],r['expanded'],len(r['path']))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()
    if args.example:
        sample_experiments()

if __name__=='__main__':
    main()
