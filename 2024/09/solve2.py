data = open("small_data.txt", "r").read().strip()

ext = []
i = 0


# move a file to the leftmost empty section
def swap_to_empty(y, x):
    # print(f"Swapping {y}-{x}")
    empt_index = 0
    gap = x - y + 1
    # find the first empty spot
    # while ext[empt_index] != '.':
    #     empt_index += 1
    next_empt = empt_index
    while next_empt - empt_index < gap:
        empt_index = next_empt
        if empt_index >= y:
            return False
        while ext[empt_index] != '.':
            empt_index += 1
        next_empt = empt_index
        while ext[next_empt] == '.' and next_empt < y:
            next_empt += 1
    for k in range(gap):
        ext[empt_index] = ext[y+k]
        ext[y+k] = '.'
        empt_index += 1


# Calculate checksum of the array
def calc_check(arr):
    check = 0
    for x in range(len(arr)):
        if arr[x] != '.':
            check += x * int(arr[x])
    return check


# Convert filesystem string into array
for file in data:
    if i % 2 == 0:
        ext += [str(i//2) for _ in range(int(file))]
    else:
        ext += list('.' * int(file))
    i += 1

# print("".join(ext))
# Move file segments from right to left until there
# is no more empty places to put them
i = len(ext) - 1
while i > -1:
    # print("I", i)
    if '.' in ext[:i]:
        if ext[i] != '.':
            j = i
            while ext[j] == ext[i]:
                j -= 1
            j += 1
            swap_to_empty(j, i)
            i = j
            # print("I", i)
            # print("".join(ext))
    else:
        break
    i -= 1
# print("".join(ext))
count = calc_check(ext)
print("Count:", count)
