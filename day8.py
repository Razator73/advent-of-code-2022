with open('input/day8.txt') as f:
    data = [[c for c in row] for row in f.read().strip().split('\n')]

# Part 1 and 2
exterior_trees = len(data) * 2 + len(data[0]) * 2 - 4
interior_trees = 0
scenic_scores = []
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        tree_height = data[i][j]
        # look left
        for k in range(j - 1, -1, -1):
            if data[i][k] >= tree_height:
                visible_from_left = False
                left_score = abs(k - j)
                break
        else:
            visible_from_left = True
            left_score = j
        # look right
        for k in range(j + 1, len(data[i])):
            if data[i][k] >= tree_height:
                visible_from_right = False
                right_score = abs(k - j)
                break
        else:
            right_score = abs(j - (len(data[i]) - 1))
            visible_from_right = True
        # look up
        for n in range(i - 1, -1, -1):
            if data[n][j] >= tree_height:
                visible_from_up = False
                up_score = abs(n - i)
                break
        else:
            up_score = i
            visible_from_up = True
        # look down
        for n in range(i + 1, len(data)):
            if data[n][j] >= tree_height:
                visible_from_down = False
                down_score = abs(n - i)
                break
        else:
            down_score = abs(i - (len(data) - 1))
            visible_from_down = True
        interior_trees += 1 if visible_from_down or visible_from_up or visible_from_left or visible_from_right else 0
        scenic_scores.append(left_score * right_score * up_score * down_score)

print(f'Visible trees {exterior_trees + interior_trees}')
print(f'Best scenic score is {max(scenic_scores)}')
