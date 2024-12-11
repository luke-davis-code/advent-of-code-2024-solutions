# PART ONE

def get_hiking_trails(topographic_map):
    map = [row for row in topographic_map.split("\n")]

    trailhead_coords = []

    # Run through map and find trailheads
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "0":
                trailhead_coords.append((i, j))

    return trailhead_coords

def traverse_path(topographic_map, start_pos, visited=None):
    # Use visited to keep track of 9s we have been too
    if visited is None:
        visited = []

    map = [row for row in topographic_map.split("\n")]
    # Recursive function
    i = start_pos[0]
    j = start_pos[1]

    # Base case - have already visited this position
    if (i, j) in visited:
        return 0

    # If not mark position as visited
    visited.append((i, j))

    # If hit a not visited 9 then add one to total
    if map[i][j] == "9":
        return 1

    height = map[i][j]
    # Could use a dictionary for this but going to use an array as more universal
    moves = [(-1, 0), (1,0), (0, -1), (0, 1)]
    # up, down, left, right = 0, 1, 2, 3

    # Use total to keep track of score for this path
    total = 0

    for move in moves:
        # Ensure move is valid
        new_i = i + move[0]
        new_j = j + move[1]
        if 0 <= new_i < len(map) and 0 <= new_j < len(map[0]):
            if map[new_i][new_j] == str(int(height) + 1):
                total += traverse_path(topographic_map, (new_i, new_j), visited)

    return total


puzzle_input = """"""

total = 0
for pos in get_hiking_trails(puzzle_input):
    total += traverse_path(puzzle_input, pos)
print(total)