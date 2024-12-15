# PART ONE
from tenacity import retry_unless_exception_type

GRID_X_SIZE = 101
GRID_Y_SIZE = 103

def get_positions(intitial_positions, velocities, seconds):
    # Given intitial positions, velocites of robots as lists with pos[i] and vel[i] for the same robot i
    # Return a grid with their positions after seconds

    # Keep track of current position of each robot
    positions = intitial_positions.copy()

    # Bathroom size is 101 by 103
    grid = [[0 for i in range(GRID_X_SIZE)] for j in range(GRID_Y_SIZE)]

    # Go through each initial position and add one to the count of robots in that position
    for position in positions:
        x = position[0]
        y = position[1]
        grid[y][x] += 1

    # Now for each second
    # Move robots by their velocity
    for i in range(seconds):
        # Run through each robot
        for pos_ind in range(len(positions)):
            cur_pos = positions[pos_ind]
            x = cur_pos[0]
            y = cur_pos[1]
            new_x = positions[pos_ind][0] + velocities[pos_ind][0]
            new_y = positions[pos_ind][1] + velocities[pos_ind][1]

            # Deal with wrapping around cases
            if new_x < 0:
                new_x = GRID_X_SIZE + new_x
            elif new_x >= GRID_X_SIZE:
                new_x = new_x - GRID_X_SIZE

            if new_y < 0:
                new_y = GRID_Y_SIZE + new_y
            elif new_y >= GRID_Y_SIZE:
                new_y = new_y - GRID_Y_SIZE

            new_pos = (new_x, new_y)

            # Now add robot to new pos and take away one from old pos
            grid[new_y][new_x] += 1
            grid[y][x] -= 1
            # Change position to reflect where robot is now
            positions[pos_ind] = new_pos

    return grid

def get_safety_factor(robot_grid):
    quadrants = [0,0,0,0]
    # Run through indexes in grid
    # Check if there is a robot in pos
    # If there is check what quadrant using the index and add one to the quadrant count

    centre_x_ind = GRID_X_SIZE//2
    centre_y_ind = GRID_Y_SIZE//2

    for y in range(GRID_Y_SIZE):
        for x in range(GRID_X_SIZE):
            robot_count = robot_grid[y][x]
            if robot_count > 0:
                if x < centre_x_ind and y < centre_y_ind:
                    quadrants[0] += robot_count
                elif x > centre_x_ind and y < centre_y_ind:
                    quadrants[1] += robot_count
                elif x < centre_x_ind and y > centre_y_ind:
                    quadrants[2] += robot_count
                elif x > centre_x_ind and y > centre_y_ind:
                    quadrants[3] += robot_count

    safety_factor = 1
    for n in quadrants:
        safety_factor = safety_factor * n

    return safety_factor


puzzle_input = """"""

# Parse input
robots = puzzle_input.split("\n")
initial_positions = [robot.split(" ")[0] for robot in robots]
velocities = [robot.split(" ")[1] for robot in robots]

for ind in range(len(initial_positions)):
    pos = initial_positions[ind]
    x_pos = pos[pos.index("=")+1:pos.index(",")]
    y_pos = pos[pos.index(",")+1:]
    initial_positions[ind] = (int(x_pos), int(y_pos))
    vel = velocities[ind]
    x_vel = vel[vel.index("=") + 1:vel.index(",")]
    y_vel = vel[vel.index(",") + 1:]
    velocities[ind] = (int(x_vel), int(y_vel))

print(get_safety_factor(get_positions(initial_positions, velocities, 100)))
