import itertools

# PART ONE

def get_all_points(frequency, map):
    # Returns a list of tuples
    # Each tuple is a point (row_index, col_index) for each occurence of that frequency
    occurences = []

    for row_index in range(len(map)):
        for col_index in range(len(map[row_index])):
            point = map[row_index][col_index]
            if point == frequency:
                occurences.append((row_index, col_index))

    return occurences


def get_antinodes(input_map):
    # Use a string to keep track of nodes which have been looked at
    different_freq = ""
    grid = input_map.split("\n")
    # Create an antinode grid to keep track of where antinodes are - as need to know UNIQUE locations
    antinode_grid = ["." * len(row) for row in grid]

    # Run through grid and get any different frequencies
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            point = grid[row_index][col_index]
            if (point.isalpha() or point.isdigit()) and point not in different_freq:
                frequency = point
                # Approach to find different antinodes is to add or subtract the change in y and change in x between the two antenna
                antenna_points = get_all_points(frequency, grid)
                # Get all possible pairs of antenna points for this frequency
                frequency_pairs = [p for p in itertools.product(antenna_points, repeat=2)]
                # For each pair - (if pair not equal) - get line between this pair
                # Plot a # where the node would be
                for pair in frequency_pairs:
                    if pair[0] != pair[1]:
                        # Each pair appears twice in frequency pairs list but in reverse order
                        # So simply add the difference between the two antenna in the pair
                        difference = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
                        # Add difference to first point that appears in pair (doesn't really matter as pair appears twice)
                        antinode_row_index = pair[0][0] + difference[0]
                        antinode_col_index = pair[0][1] + difference[1]
                        # Check if new pos to add in grid -if is add it
                        if 0 <= antinode_row_index < len(grid) and 0 <= antinode_col_index < len(grid[0]):
                            # To make more readable insert into string in seperate parts
                            before = antinode_grid[antinode_row_index][:antinode_col_index]
                            after = antinode_grid[antinode_row_index][antinode_col_index+1:]
                            antinode_grid[antinode_row_index] = before + "#" + after

    # Get total
    total = 0
    for row in antinode_grid:
        for point in row:
            if point == "#":
                total += 1

    return total


puzzle_input = """"""

print(get_antinodes(puzzle_input))
