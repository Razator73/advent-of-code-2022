from math import inf

with open('input/day12.txt') as f:
    height_map = [[c for c in row] for row in f.read().strip().split('\n')]


def get_reverse_neighbors(heights, x, y):
    neighbors = []
    rows = len(heights)
    cols = len(heights[0])
    if x > 0 and heights[x][y] - heights[x - 1][y] < 2:
        neighbors.append((x - 1, y))
    if x < rows - 1 and heights[x][y] - heights[x + 1][y] < 2:
        neighbors.append((x + 1, y))
    if y > 0 and heights[x][y] - heights[x][y - 1] < 2:
        neighbors.append((x, y - 1))
    if y < cols - 1 and heights[x][y] - heights[x][y + 1] < 2:
        neighbors.append((x, y + 1))
    return neighbors


def get_distance(graph, start, end=None):
    unvisited = graph.copy()
    dist = {v: float(inf) for v in graph}
    dist[start] = 0
    cur_pos = start
    while unvisited and cur_pos != end:
        cur_pos = unvisited.pop(unvisited.index(min(unvisited, key=lambda v: dist[v])))
        cur_neighbors = get_reverse_neighbors(height_map, *cur_pos)
        for v in [_ for _ in cur_neighbors if _ in unvisited]:
            alt = dist[cur_pos] + 1
            if alt < dist[v]:
                dist[v] = alt
            if v == end_pos:
                break
    return dist


height_str = 'abcdefghijklmnopqrstuvwxyz'
vertices = []
start_pos = end_pos = (0, 0)
for i in range(len(height_map)):
    for j in range(len(height_map[i])):
        vertices.append((i, j))
        if height_map[i][j] == 'S':
            start_pos = (i, j)
            height_map[i][j] = 0
        elif height_map[i][j] == 'E':
            end_pos = (i, j)
            height_map[i][j] = 25
        else:
            height_map[i][j] = height_str.find(height_map[i][j])

distances = get_distance(vertices, end_pos)
# Part 1
print(distances[start_pos])

# Part 2
starting_positions = [(i, j) for i in range(len(height_map)) for j in range(len(height_map[i]))
                      if height_map[i][j] == 0]
print(min([distances[start] for start in starting_positions]))
