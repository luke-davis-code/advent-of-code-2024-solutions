# PART ONE

# Represent grid as a list of lists

def get_regions(garden):
    # Regions is a list of lists of points in the same region
    regions = []

    # Keep a track of points visited
    visited = []

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for row_index in range(len(garden)):
        for col_index in range(len(garden[row_index])):
            point = (row_index, col_index)

            # If not already visited point
            if point not in visited:
                plant = garden[point[0]][point[1]]
                region = [point]
                visited.append(point)

                # To visit keeps track of next points in region to visit
                to_visit = [point]

                while len(to_visit) > 0:
                    current_point = to_visit.pop()

                    for move in moves:
                        adjacent_point = (current_point[0] + move[0], current_point[1] + move[1],)
                        # Check if adjacent point exists
                        if 0 <= adjacent_point[0] < len(garden) and 0 <= adjacent_point[1] < len(garden[0]):
                                # It exists so check if its been visited
                                if adjacent_point not in visited:
                                    adjacent_plant = garden[adjacent_point[0]][adjacent_point[1]]
                                    # If not then check if this is in same region i.e., has same plant in it
                                    if plant == adjacent_plant:
                                        # Now this is region so need to check adjacent point again
                                        to_visit.append(adjacent_point)
                                        region.append(adjacent_point)
                                        visited.append(adjacent_point)
                regions.append(region)
    return regions

def get_fence_prices(regions):
    # Takes in a list of regions
    # Gets the perimeter of each region, area of each region
    # Fence price is area * perimeter
    # Returns sum of fence prices
    sum = 0

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # up, down, left, right = 0, 1, 2, 3

    for region in regions:
        # Area is number of plots in region (easy)
        area = len(region)

        # Perimeter is number of sides of garden plot that do not touch another garden plot in same region
        # Run through points add one to perimiter if not touching another point in same region
        # Don't need to worry about overadding to perimeter as the points of duplication are ignored
        perimeter = 0
        for point in region:
            for move in moves:
                adjacent_point = (point[0] + move[0], point[1] + move[1])
                # Check if adjacent point exists
                if 0 <= adjacent_point[0] < len(garden) and 0 <= adjacent_point[1] < len(garden[0]):
                    # If adjacent point not in region then this is part of perimeter
                    if not (adjacent_point in region):
                        perimeter += 1
                # if doesn't exist this is a perimeter side
                else:
                    perimeter += 1

        sum += area * perimeter
    return sum

puzzle_input = """"""

garden = [[col for col in row] for row in puzzle_input.split("\n")]
regions = get_regions(garden)
print(get_fence_prices(regions))