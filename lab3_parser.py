# (A); (B); (C)
# (A, C); X; X

stacks = []


class Stack:
    name = ""
    containers = []

    def __init__(self, name, containers):
        self.name = name
        self.containers = containers

    def add_container(self, container):
        self.containers.append(container)

    def to_string(self):
        aux = ""
        for c in self.containers:
            aux = aux + c + " ;"

        print('Stack: ' + self.name + " Containers: " + aux)


def initialize_containers(raw_string):
    parsed_containers = raw_string.split(';')

    for x in range(0, len(parsed_containers)):
        parsed_containers[x] = parsed_containers[x].strip('()')
        elements = parsed_containers[x].split(',')
        for y in range(0, len(elements)):
            stacks[x].add_container(elements[y])


no_stacks = int(input('Enter the number of stacks: '))
print(no_stacks)

unparsed_stacks = input('Enter the name of the stacks: ')

parsed_stacks = unparsed_stacks.split(';')

for x in range(0, len(parsed_stacks)):
    stack_constructor = Stack(parsed_stacks[x].strip().strip('()'), [])
    stacks.append(stack_constructor)

unparsed_containers = input('Enter the container s string: ')

initialize_containers(unparsed_containers)


for x in range(0, len(stacks)):
    stacks[x].to_string()