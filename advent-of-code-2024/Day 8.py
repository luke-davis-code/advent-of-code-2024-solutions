import itertools

def get_line(point_a, point_b):
    # Points in form (x,y)
    # Given two points get a line that both points lie on
    # y = mx +c
    # return form this the gradient, m
    # return m as tuple (change in y, change in x)

    m = (point_b[1]-point_a[1],point_b[0]-point_a[0])
    # c = point_a[1] - (m * point_a[0])

    return m

def get_all(frequency, map):
    # Returns a list of tuples
    # Each tuple is a point (row_index, col_index) for each occurence of that frequency
    occurences = []

    for row_index in range(len(map)):
        for col_index in range(len(map[row_index])):
            point = map[row_index][col_index]
            if point == frequency:
                print(row_index)
                occurences.append((row_index, col_index))

    return occurences


def get_antinodes(input_map):
    # Use a string to keep track of nodes which have been looked at
    different_freq = ""
    grid = input_map.split("\n")

    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            point = grid[row_index][col_index]
            if (point.isalpha() or point.isdigit()) and point not in different_freq:
                different_freq += point

    print(different_freq)
    for frequency in different_freq:
        antenna_points = get_all(frequency, grid)
        # Get all possible pairs of antenna points for this frequency
        frequency_pairs = [p for p in itertools.product(antenna_points,repeat=2)]
        # For each pair - (if pair not equal) - get line between this pair
        # Plot a # where the node would be
        for pair in frequency_pairs:
            if pair[0] != pair[1]:
                # Row index is y
                m = get_line(pair[0], pair[1])
                # Node is two m (the gradient) away from each pair
                # - gradient for lower pair
                # + gradient for higher pair
                # Must check if node index exists
                # Need to do element wise tuple addition
                node0_pos = tuple(map(lambda i, j: i - j, pair[0], 2*m))
                node1_pos = tuple(map(lambda i, j: i + j, pair[1], 2 * m))

                print(pair)
                print(m)
                print(node0_pos)












puzzle_input = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""

get_antinodes(puzzle_input)