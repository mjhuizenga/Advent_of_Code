data = open("data.txt", "r").read().strip()

ext = []
i = 0
empt_index = 0


def swap_to_empty(x):
    global empt_index
    # print("".join(ext))
    # print("Empt:", empt_index, ext[empt_index])
    # print("X:", x, ext[x])
    while ext[empt_index] != '.':
        # print("Skip:", ext[empt_index])
        empt_index += 1
    ext[empt_index] = ext[x]
    ext[x] = '.'
    empt_index += 1


def calc_check(ext):
    x = 0
    check = 0
    while (ext[x] != '.'):
        check += x * int(ext[x])
        x += 1
    return check


for file in data:
    if i % 2 == 0:
        ext += [str(i//2) for _ in range(int(file))]
    else:
        ext += list('.' * int(file))
    i += 1

for i in range(len(ext)-1, -1, -1):
    if '.' in ext[:i]:
        if ext[i] != '.':
            swap_to_empty(i)
    else:
        break
# print(data)
count = calc_check(ext)
print("Count:", count)
