priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
              'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
              'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
              'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
# test_input = ('vJrwpWtwJgWrhcsFMMfFFhFp\n'
#               'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
#               'PmmdzqPrVvPwwTWBwg\n'
#               'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
#               'ttgJtRGJQctTZtZT\n'
#               'CrZsJsPPZsGzwwsLwLmpwMDw')
# sacks = test_input.split('\n')
with open('input/day3.txt') as f:
    sacks = [sack for sack in f.read().split('\n') if sack]

# Part 1
sack_error_sum = 0
for sack in sacks:
    compartment_1, compartment_2 = sack[:len(sack) // 2], sack[len(sack) // 2:]
    for item in compartment_1:
        if item in compartment_2:
            sack_error_sum += priorities[item]
            break
print(sack_error_sum)

# Part 2
badge_sum = 0
for i in range(0, len(sacks), 3):
    group = sacks[i:i + 3]
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badge_sum += priorities[item]
            break
print(badge_sum)
