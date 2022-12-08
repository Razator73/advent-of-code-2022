import copy
import re

with open('input/day5.txt') as f:
    data = [line for line in f.read().split('\n') if line]

movements = []
raw_stacks = []
for line in data:
    if move := re.search(r'move (\d+) from (\d+) to (\d+)', line):
        movements.append(tuple(int(i) for i in move.groups()))
    else:
        raw_stacks.append(line)

stacks = {}
for stack_num in raw_stacks[-1].split(' '):
    if stack_num:
        stack_num = int(stack_num)
        new_stack = []
        for row in raw_stacks[-2::-1]:
            if len(row) < 4 * stack_num - 3:
                continue
            if (crate := row[4 * stack_num - 3]) != ' ':
                new_stack.append(crate)
        stacks[stack_num] = new_stack

original_stacks = copy.deepcopy(stacks)

# Part 1
for move in movements:
    quantity, from_stack, to_stack = move
    for i in range(quantity):
        stacks[to_stack].append(stacks[from_stack].pop())
print(''.join(stack[-1] for stack in stacks.values()))

# Part 2
stacks = copy.deepcopy(original_stacks)
for move in movements:
    quantity, from_stack, to_stack = move
    stacks[to_stack] += stacks[from_stack][-quantity:]
    stacks[from_stack] = stacks[from_stack][:-quantity]
print(''.join(stack[-1] for stack in stacks.values()))
