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

list1 = []
list2 = []
for line in puzzle_input.split("\n"):
    list1.append(int(line.split("   ")[0]))
    list2.append(int(line.split("   ")[1]))

total = 0
count = 0

while count < len(list1):
    index1 = get_smallest(list1)
    index2 = get_smallest(list2)
    num1 = list1[index1]
    num2 = list2[index2]
    total += abs(num1 - num2)
    list1[index1] = -1
    list2[index2] = -1
    count += 1

print(total)







