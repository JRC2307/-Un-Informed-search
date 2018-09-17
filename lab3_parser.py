# (A); (B); (C)
# (A, C); X; X

import itertools
import heapq

stacks = []
goal_state = []


def initialize_containers(raw_string, destiny):
    parsed_stacks = raw_string.split(';')
    for x in range(0, len(parsed_stacks)):
        parsed_containers = parsed_stacks[x].strip().strip('(').strip(')')
        parsed_elements = parsed_containers.split(',')
        stack_constructor = []

        for e in range(0, len(parsed_elements)):
            stack_constructor.append(parsed_elements[e].strip(" "))

        destiny.append(stack_constructor)


def are_equal():
    for x in range(0,len(stacks)):
        for y in range(0,len(stacks[x])):
            if stacks[x][y] != goal_state[x][y]: return False
    return True

def main():

    explored = []
    path = []

    cost = 0

    no_stacks = int(input('Enter the maximum number of containers: '))
    unparsed_stacks = input('Enter the input stacks: ')
    uparsed_output = input('Enter the output stacks: ')

    initialize_containers(unparsed_stacks, stacks)
    initialize_containers(uparsed_output, goal_state)

    actual_state = [(cost, path, stacks)]
    cost, path, state = heapq.heappop(actual_state)

    while True:
        if are_equal():
            print(cost)
            print(path)
        else:
            extensions = list(itertools.permutations(range(0, len(state)), 2))
            print(extensions)

main()