import re

with open('input/day4.txt') as f:
    assignments = [assignment for assignment in f.read().split('\n') if assignment]
assignments = [re.search(r'(\d+)-(\d+),(\d+)-(\d+)', assignment).groups() for assignment in assignments]

# Part 1
contains = 0
for assignment in assignments:
    x1, x2, y1, y2 = [int(i) for i in assignment]
    if (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2):
        contains += 1
print(contains)

# Part 2
overlaps = 0
for assignment in assignments:
    x1, x2, y1, y2 = [int(i) for i in assignment]
    if (y1 <= x1 <= y2) or (y1 <= x2 <= y2) or (x1 <= y1 <= x2) or (x1 <= y2 <= x2):
        overlaps += 1
print(overlaps)
