def decode_format(diskmap):
    # Converts a dense format diskmap into a string representation of the disk with . representing free space
    # Also returns the maximum id number for this disk as needed when compacting
    disk = ""

    # Use a bool to know if looking at length of file or length of free space
    free_space = False
    i = 0

    # Keep track of ID number using an int
    id = 0

    while i < len(diskmap):
        if not free_space:
            disk += str(id) * int(diskmap[i])
            id += 1
        else:
            disk += "." * int(diskmap[i])
        i += 1
        free_space = not free_space

    return disk, id-1

def compact(disk, max_id):
    # Take in string representation of disk (and max id number) and compact it using the amphipod's process
    compact_disk = disk
    print(disk)
    print()

    # Move file blocks one at a time (from the end) until no gaps between fileblocks
    # Also keep track of size of fileblocks being looked at using num digits
    current_id = max_id
    block_size = len(str(current_id))
    i = len(compact_disk) - block_size
    while compact_disk[:i].count(".") > 0:
        # Get index of first free space from the left that can fit current block_size
        # .index() finds first occurence of item
        free_space_index = compact_disk.index(".")
        print()
        print(len(compact_disk) - i)
        print()

        file_block = compact_disk[i:i + block_size]
        free_space = compact_disk[free_space_index]
        print(block_size)
        print(file_block)
        print(free_space)
        print()
        # Swap free space with file block at end of disk
        before_space = compact_disk[:free_space_index]
        between = compact_disk[free_space_index+1:i]
        after_file_block = compact_disk[i + block_size:]
        compact_disk = before_space + file_block + between + "."

        # Now change file block size if next file block looking at is different
        next_file_block = compact_disk[i:i + block_size]
        if next_file_block != file_block:
            current_id -= 1
            block_size = len(str(current_id))

        i -= block_size

        print()
        print(compact_disk)
        print()
    return compact_disk


def checksum(disk):
    # Take in string representation of a disk and return its checksum
    sum = 0

    # Use a count to account for ids being more than one digit
    count = 0

    for position in range(0, len(disk)):
        id = disk[position]
        if id != ".":
            sum += position * int(id)

    return sum


puzzle_input = "156769588015262926819037393"

disk, id = decode_format(puzzle_input)
print(checksum(compact(disk, id)))
