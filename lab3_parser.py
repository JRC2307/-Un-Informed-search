class Stack:
  def __init__(self, name, containers):
    self.name = name
    self.containers = containers

stacks = []

no_stacks = int(input('Enter the number of stacks: '))
print(no_stacks)

unparsed_stacks = input('Enter the name of the stacks: ')

parsed_stacks = unparsed_stacks.split(';')

if len(parsed_stacks) != no_stacks:
	print('The number of stacks and the given string of stacks doesnt match')

for x in range(0, no_stacks):
	stack_constructor = Stack(parsed_stacks[x], [])
	stacks.append(stack_constructor)

print(stacks)
	