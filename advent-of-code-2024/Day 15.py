# PART ONE

def move_robot(warehouse, move):
    # Get position of robot after a move
    # Return the map after
    new_warehouse = warehouse.copy()

    robot_position = (0,0)
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[i])):
            if warehouse_map[i][j] == "@":
                robot_position = (i, j)

    # Use a dictionary to keep track of moves
    moves_list = {"<" : (0, -1),
            ">" : (0, 1),
            "v" : (1, 0),
            "^" : (-1, 0)}

    # Move robot according to move
    move_vec = moves_list[move]
    new_pos = (robot_position[0] + move_vec[0], robot_position[1] + move_vec[1])

    # If moving into a wall don't move
    if warehouse[new_pos[0]][new_pos[1]] == "#":
        return new_warehouse


    # Move boxes in the way
    # Boxes aim position variable
    boxes_aim = new_pos
    while warehouse[boxes_aim[0]][boxes_aim[1]] == "O":
        boxes_aim = (boxes_aim[0] + move_vec[0], boxes_aim[1]+move_vec[1])

    # If boxes being pushed into wall robot doesnt move
    if warehouse[boxes_aim[0]][boxes_aim[1]] == "#":
        return new_warehouse

    # Now move robot and boxes
    # Use a pointer that goes backwards from the boxes in front of robot and moves them forwards
    current_mover = boxes_aim
    # If no boxes to move only move robot
    if boxes_aim == new_pos:
        new_warehouse[boxes_aim[0]][boxes_aim[1]] = "@"
        new_warehouse[robot_position[0]][robot_position[1]] = "."
        return new_warehouse

    # If at this point there are boxes so move them then robot
    while current_mover != robot_position:
        previous = (current_mover[0] - move_vec[0], current_mover[1] - move_vec[1])
        new_warehouse[current_mover[0]][current_mover[1]] = new_warehouse[previous[0]][previous[1]]
        new_warehouse[previous[0]][previous[1]] = "."
        current_mover = previous

    return new_warehouse


puzzle_input = """"""

# Parse puzzle input
for line_index in range(len(puzzle_input.split("\n"))):
    if puzzle_input.split("\n")[line_index] == "":
        warehouse_map = [[item for item in line] for line in puzzle_input.split("\n")[:line_index]]
        moves = puzzle_input.split("\n")[line_index+1:]

moves = "".join(moves)
for move in moves:
    warehouse_map = move_robot(warehouse_map, move)

# Get sum of all GPS coordinates
sum = 0
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[i])):
        if warehouse_map[i][j] == 'O':
            sum += (100 * i) + j
print(sum)


