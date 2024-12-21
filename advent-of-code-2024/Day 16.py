# PART ONE

puzzle_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

maze = [[col for col in row] for row in puzzle_input.split("\n")]
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start = (i, j)
        if maze[i][j] == "E":
            end = (i, j)

for row in maze:
    print(row)

# Perform a depth first search to get maze solutions
# Using wikipedia as basis of implementation
def depth_first_search(maze, start, end, visited):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        # For all directions can travel in cehck that node
        # If not visited then call dfs
        forward = 























