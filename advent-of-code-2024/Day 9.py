# PART ONE

def decode_format(diskmap):
    # Converts a dense format diskmap into a string representation of the disk with . representing free space
    # Also returns the maximum id number for this disk as needed when compacting
    disk = []

    # Use a bool to know if looking at length of file or length of free space
    free_space = False
    i = 0

    # Keep track of ID number using an int
    id = 0

    while i < len(diskmap):
        if not free_space:
            for j in range(int(diskmap[i])):
                disk.append(str(id))
            id += 1
        else:
            for j in range(int(diskmap[i])):
                disk.append(".")
        i += 1
        free_space = not free_space

    return disk



def compact(disk):
    # Take in list representation of disk and compact it using the amphipod's process
    compact_disk = disk.copy()

    # Move file blocks one at a time (from the end) until no gaps between fileblocks

    # Have a pointer i - points to current fileblock being looked at (from the right)
    i = len(disk)

    while compact_disk[:i].count(".") > 0:
        i -= 1

        free_space_index = compact_disk.index(".")
        file_block = compact_disk[i]

        # Now swap these
        compact_disk[free_space_index] = file_block
        compact_disk[i] = "."

    return compact_disk

def checksum(filesystem):
    total = 0
    # Take in a filesystem as a list and return its checksum
    for position in range(len(filesystem)):
        if filesystem[position] != ".":
            total += position * int(filesystem[position])

    return total

puzzle_input = ""

print(checksum(compact(decode_format(puzzle_input))))
