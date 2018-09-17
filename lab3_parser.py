# (A); (B); (C)
# (A, C); X; X

stacks = []
output_stack = []

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
            aux = aux + c + ";"

        print('Stack: ' + self.name + " Containers: " + aux)


def initialize_containers(raw_string, destiny):
    parsed_stacks = raw_string.split(';')
    for x in range(0, len(parsed_stacks)):
        parsed_containers = parsed_stacks[x].strip().strip('(').strip(')')
        parsed_elements = parsed_containers.split(',')
        stack_constructor = Stack(str(x),[])

        for e in range(0, len(parsed_elements)):
            stack_constructor.add_container(parsed_elements[e].strip(" "))

        destiny.append(stack_constructor)

def are_equal():
    for x in range(0,len(stacks)):
        for y in range(0,len(stacks[x].containers)):
            if stacks[x].containers[y] != output_stack[x].containers[y]: return False
        return True

no_stacks = int(input('Enter the maximum number of containers: '))
unparsed_stacks = input('Enter the input stacks: ')
uparsed_output = input('Enter the output stacks: ')

initialize_containers(unparsed_stacks, stacks)
initialize_containers(uparsed_output, output_stack)

print("\nInitial state: ")
for e in stacks:
    e.to_string()

print("Goal state: ")
for g in output_stack:
    g.to_string()

print(are_equal())