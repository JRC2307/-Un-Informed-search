# (A); (B); (C)
# (A, C); X; X

import itertools
import heapq
import copy

stacks = []
goal_state = []


def initialize_containers(raw_string, destiny):
    parsed_stacks = raw_string.split(';')
    for x in range(0, len(parsed_stacks)):
        parsed_containers = parsed_stacks[x].strip().strip('(').strip(')')
        parsed_elements = parsed_containers.split(',')
        stack_constructor = []

        for e in range(0, len(parsed_elements)):
            if parsed_elements[e].strip(" ") != '':
                stack_constructor.append(parsed_elements[e].strip(" "))

        destiny.append(stack_constructor)


def are_equal(actual):
    equal_numbers = 0
    for index, item in enumerate(goal_state):
        if item != ['X']:
            if actual[index] == goal_state[index]:
                equal_numbers += 1
    if equal_numbers == len(goal_state) - goal_state.count(['X']):
        return True
    return False

def heuristic(actual):
    heuristic = 0
    for index, item in enumerate(goal_state):
        if item != ['X']:
            if actual[index] != goal_state[index]:
                heuristic += 1
    return heuristic

def get_children(cost, actual_state, extensions, path, depth):
    children = []
    for move in extensions:

        p = copy.deepcopy(path)
        s = copy.deepcopy(actual_state)
        c = cost + 1 + abs(move[0] - move[1])

        if len(s[move[1]]) >= depth:
            continue
        if not s[move[0]]:
            continue

        value = (s[move[0]]).pop()
        heuristic_cost = heuristic(s)
        s[move[1]].append(value)
        c = c + heuristic_cost
        p.append(move)

        children.append((c, p, s))
    return children


def print_path(path):
    aux = 0
    for p in path:
        if aux < len(path) - 1:
            print(p, end="")
            print("; ", end="")
        else:
            print(p)
        aux = aux+1

def main():

    explored = []
    path = []

    cost = 0

    no_stacks = int(input())
    unparsed_stacks = input()
    uparsed_output = input()

    initialize_containers(unparsed_stacks, stacks)
    initialize_containers(uparsed_output, goal_state)
    actual_state = [(cost, path, stacks)]

    while actual_state:
        cost, path, state = heapq.heappop(actual_state)
        if are_equal(state):
            print(cost)
            print_path(path)
            return path
        else:
            extensions = list(itertools.permutations(range(0, len(state)), 2))
            if state not in explored:
                next_children = get_children(cost, state, extensions, path, no_stacks)
                for c in next_children:
                    heapq.heappush(actual_state, c)
                #kep
                explored.append(state)

    print("No solution found")

main()