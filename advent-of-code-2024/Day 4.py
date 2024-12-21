# PART ONE


def get_neighbour_letter_position(grid, position, direction_index):
    # Moves north, east, south, west, northeast, northwest, southeast, southwest
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
    direction = directions[direction_index]
    next_position = (position[0] + direction[0], position[1] + direction[1])
    return (next_position[0],next_position[1])

puzzle_input = """"""

word_grid = puzzle_input.split("\n")

visited = []
solution_word = "XMAS"
check_length = 4
# Run through every letter in grid
i, j = 0, 0
solution_letter = 0
counter = 0
for i in range(len(word_grid)):
    for j in range(len(word_grid[0])):
        start_position = (i, j)
        for direction_index in range(8):
            am_checking = True
            checking = start_position
            # If first letter matches first letter of word
            # There is a chance so check this word
            while am_checking:
                if solution_letter == len(solution_word):
                    am_checking = False
                    counter += 1
                # Check if position actually possible
                elif not (0 <= checking[0] < len(word_grid) and 0 <= checking[1] < len(word_grid[0])):
                    am_checking = False
                elif word_grid[checking[0]][checking[1]] == solution_word[solution_letter]:
                    solution_letter += 1
                    checking = get_neighbour_letter_position(word_grid, checking, direction_index)
                    print(checking)
                else:
                    am_checking = False
            solution_letter = 0


print(counter)