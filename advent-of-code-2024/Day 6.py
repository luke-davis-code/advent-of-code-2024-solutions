def distinct_positions(input):
    total = 0

    # Parse input so it is an array as easier to then access as a grid
    grid = [row.strip("\n") for row in input.split('\n')]

    # Get guard start coordinate
    # There is always a guard so don't need to worry about exception
    for row in grid:
        if "^" in row:
            # Coordinate (row, column)
            guard_coord = [grid.index(row), row.index("^")]

    # Create an array of moves with directions associated with them
    # Could use a dictionary for this but going to use an array as more universal
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # up, down, left, right = 0, 1, 2, 3

    # Use number to keep track of current direction
    # Start up (so 0)
    # Adding one turns guard right
    current_direction = 0

    # Now implement guard logic
    # Guard keeps moving unless next move is off the grid
    while 0 <= guard_coord[0] + moves[current_direction][0] < len(grid) and 0 <= guard_coord[1] + moves[current_direction][1] < len(grid[0]):
        row_index = guard_coord[0]
        col_index = guard_coord[1]

        # Check if there is an item in front of the guard
        if grid[row_index + moves[current_direction][0]][col_index + moves[current_direction][1]] == "#":
            # Turn to right
            # Mod to ensure index is in the moves list
            current_direction = (current_direction + 1) % 4
        else:
            # Mark square as visited and add one to total
            # If not visited previously
            if grid[row_index][col_index] != "X":
                total += 1
                grid[row_index] = grid[row_index][:col_index] + "X" + grid[row_index][col_index+1:]

            # Move in current direction
            guard_coord = [guard_coord[0] + moves[current_direction][0], guard_coord[1] + moves[current_direction][1]]

    # Add one to total for start position
    total += 1

    return total


puzzle_input = """"""

print(distinct_positions(puzzle_input))
