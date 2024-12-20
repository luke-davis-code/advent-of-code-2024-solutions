import math

# PART ONE

def get_smallest(list):
    # Return index of smallest item in list
    smallest = math.inf
    index = -1
    for i in range(len(list)):
        num = list[i]
        if num != -1:
            if num < smallest:
                smallest = num
                index = i
    return index

puzzle_input = """"""

leftlist = []
rightlist = []
for line in puzzle_input.split("\n"):
    leftlist.append(int(line.split("   ")[0]))
    rightlist.append(int(line.split("   ")[1]))

# Get total difference score

total = 0
count = 0

while count < len(leftlist):
    index1 = get_smallest(leftlist)
    index2 = get_smallest(rightlist)
    num1 = leftlist[index1]
    num2 = rightlist[index2]
    total += abs(num1 - num2)
    leftlist[index1] = -1
    rightlist[index2] = -1
    count += 1

print(total)


# PART TWO

# Reset lists
leftlist = []
rightlist = []
for line in puzzle_input.split("\n"):
    leftlist.append(int(line.split("   ")[0]))
    rightlist.append(int(line.split("   ")[1]))

def get_similarity(leftnum, rightlist):
    count = 0
    for rightnum in rightlist:
        if leftnum == rightnum:
            count += 1
    return leftnum * count

# Get total similarity score
total = 0
for num in leftlist:
    total += get_similarity(num, rightlist)

print(total)










