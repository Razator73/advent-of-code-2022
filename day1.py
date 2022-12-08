with open('input/day1.txt') as f:
    data = f.read()
    elves_data = [[int(food) for food in elf.split('\n') if food] for elf in data.split('\n\n')]

elf_totals = [sum(elf) for elf in elves_data]
# Part 1
print(max(elf_totals))

# Part 2
elf_totals.sort()
print(elf_totals[-3:])
print(sum(elf_totals[-3:]))
