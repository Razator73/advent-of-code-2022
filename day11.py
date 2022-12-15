from math import lcm


def create_op(op, num):
    ops = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}
    if num.isdigit():
        return lambda x: ops[op](x, int(num))
    else:
        return lambda x: ops[op](x, x)


def parse_monkeys(mons):
    monkey_dict = {}
    for mon in mons:
        monkey_data = mon.split('\n')
        monkey_num = monkey_data[0].split(' ')[-1][:-1]
        monkey_dict[monkey_num] = {}
        monkey_dict[monkey_num]['starting_items'] = [int(i) for i in monkey_data[1][18:].split(', ')]
        op_line = monkey_data[2].split(' ')[3:]
        monkey_dict[monkey_num]['op'] = create_op(op_line[-2], op_line[-1])
        monkey_dict[monkey_num]['test'] = int(monkey_data[3].split(' ')[-1])
        monkey_dict[monkey_num]['test_true'] = monkey_data[4].split(' ')[-1]
        monkey_dict[monkey_num]['test_false'] = monkey_data[5].split(' ')[-1]
        monkey_dict[monkey_num]['inspected'] = 0
    return monkey_dict


def complete_round(mons, worry_cut, max_cut=1):
    for monkey in mons.values():
        while monkey['starting_items']:
            item = monkey['starting_items'].pop(0)
            item = monkey['op'](item)
            if isinstance(worry_cut, int):
                item = item // worry_cut
            else:
                item %= max_cut
            if item % monkey['test']:
                mons[monkey['test_false']]['starting_items'].append(item)
            else:
                mons[monkey['test_true']]['starting_items'].append(item)
            monkey['inspected'] += 1
    return mons


with open('input/day11.txt') as f:
    monkeys = f.read().strip().split('\n\n')


# Part 1
monkey_dict = parse_monkeys(monkeys)
for _ in range(20):
    monkey_dict = complete_round(monkey_dict, 3)
monkey_inspections = [monkey['inspected'] for monkey in monkey_dict.values()]
monkey_inspections.sort()
print(f'The level of monkey business is {monkey_inspections[-1] * monkey_inspections[-2]}')

# Part 2
monkey_dict = parse_monkeys(monkeys)
max_worry = lcm(*[monkey['test'] for monkey in monkey_dict.values()])
for k in range(10000):
    monkey_dict = complete_round(monkey_dict, 'test', max_worry)
monkey_inspections = [monkey['inspected'] for monkey in monkey_dict.values()]
monkey_inspections.sort()
print(f'The level of monkey business is {monkey_inspections[-1] * monkey_inspections[-2]}')
