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

# Breadth first search
frontier = [start]
explored = []

next = 
















