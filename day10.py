with open('input/day10.txt') as f:
    signals = f.read().strip().split('\n')

x = 1
cycles = 1
read_cycle = 20
read_cycles = []

# Part 1
for signal in signals:
    if signal == 'noop':
        cycles += 1
        if cycles == read_cycle:
            read_cycles.append(x * cycles)
            read_cycle += 40
    else:
        cycles += 2
        if cycles == read_cycle:
            x += int(signal.split(' ')[1])
            read_cycles.append(x * cycles)
            read_cycle += 40
        elif cycles == read_cycle + 1:
            read_cycles.append(x * (cycles - 1))
            read_cycle += 40
            x += int(signal.split(' ')[1])
        else:
            x += int(signal.split(' ')[1])

print(f'The sum of the signals is {sum(read_cycles)}')


# Part 2
def print_crt(crt):
    for row in crt:
        print(' ' + ''.join(row))


def get_crt_pixel(sprite):
    return sprite // 40, sprite % 40


sprite_loc = 1
cycle = 0
crt_output = [['.' for _ in range(40)] for _ in range(6)]
for signal in signals:
    sprite_shape = (sprite_loc - 1, sprite_loc, sprite_loc + 1)
    if signal == 'noop':
        if cycle % 40 in sprite_shape:
            x, y = get_crt_pixel(cycle)
            crt_output[x][y] = '#'
        cycle += 1
    else:
        for _ in range(2):
            if cycle % 40 in sprite_shape:
                x, y = get_crt_pixel(cycle)
                crt_output[x][y] = '#'
            cycle += 1
        sprite_loc += int(signal.split(' ')[1])
print_crt(crt_output)
