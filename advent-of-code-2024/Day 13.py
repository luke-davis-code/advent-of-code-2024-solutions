# PART ONE

def get_info(claw_machine):
    # Take in claw machine in form of a list (example below)
    """
    [Button A: X+94, Y+34,
    Button B: X+22, Y+67,
    Prize: X=8400, Y=5400]
    """
    # Parse inputs to get relevant information
    a_button = claw_machine[0].split(",")
    a_vector = (int(a_button[0][a_button[0].index("+")+1:]), int(a_button[1][a_button[1].index("+")+1:]))

    b_button = claw_machine[1].split(",")
    b_vector = (int(b_button[0][b_button[0].index("+")+1:]), int(b_button[1][b_button[1].index("+")+1:]))

    prize = claw_machine[2].split(",")
    prize_vector = (int(prize[0][prize[0].index("=")+1:]), int(prize[1][prize[1].index("=")+1:]))

    return a_vector, b_vector, prize_vector

def get_cheapest(a_vec, b_vec, prize_vec):
    # Each vector of the form (x,y)

    possible = False

    # Most expensive possible path is 400
    cheapest = 401

    # "You estimate that each button would need to be pressed no more than 100 times to win a prize."
    for a_press in range(0,101):
        for b_press in range(0,101):
            x_location = (a_vec[0]*a_press) + (b_vec[0]*b_press)
            y_location = (a_vec[1]*a_press) + (b_vec[1]*b_press)
            if (x_location, y_location) == prize_vec:
                possible = True
                cost = (3 * a_press) + b_press
                if cost < cheapest:
                    cheapest = cost

    return possible, cheapest


puzzle_input = """"""

# Parse input
claw_machines = []
lines = puzzle_input.split("\n")
for i in range(len(lines)):
    if lines[i] == "":
        claw_machines.append(lines[i-3:i])

# Run through each claw machine and if there is a cheapest way add the cost in tokens to total
total = 0
for claw_machine in claw_machines:
    a_vector, b_vector, prize_vector = get_info(claw_machine)
    solution = get_cheapest(a_vector, b_vector, prize_vector)
    if solution[0]:
        total += solution[1]

print(total)