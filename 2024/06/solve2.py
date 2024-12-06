import copy
data = open("./data.txt", "r").read().strip()

turn_map = {'>': 'v', 'v': '<', '<': '^', '^': '>'}
xcoord = 0
ycoord = 0


# 1000 - 15855
# 2000 - 15562
# 4000 - 14489
# 8000 - 2188
def stuck_in_loop(arr):
    c_arr = copy.deepcopy(arr)
    coords = [xcoord, ycoord]
    history = set()
    while not make_move(c_arr, coords):
        position = coords[0] + coords[1] * 1000 + \
            ord(c_arr[coords[0]][coords[1]]) * 1000000
        if position in history:
            return True
        history.add(position)
    return False


def make_move(arr, coords):
    # find the arrow and do a movement
    i = coords[0]
    j = coords[1]
    x = 0
    y = 0
    match arr[i][j]:
        case '^':
            x = 0
            y = -1
        case '>':
            x = 1
            y = 0
        case 'v':
            x = 0
            y = 1
        case '<':
            x = -1
            y = 0
    if i+y >= len(arr) or i+y < 0 or j+x >= len(arr[0]) or j+x < 0:
        arr[i][j] = 'X'
        return True
    if arr[i+y][j+x] == '.' or arr[i+y][j+x] == 'X':
        arr[i+y][j+x] = arr[i][j]
        arr[i][j] = 'X'
    elif arr[i+y][j+x] == '#':
        arr[i][j] = turn_map[arr[i][j]]
        return False
    coords[0] = i + y
    coords[1] = j + x
    return False


# print(data)
arr = [list(line) for line in data.split("\n")]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '.' or arr[i][j] == '#' or arr[i][j] == 'X':
            continue
        else:
            xcoord = i
            ycoord = j
            break

# get path of original
coords = [xcoord, ycoord]
while not make_move(arr, coords):
    pass
arr[xcoord][ycoord] = '^'


count = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 'X':
            arr[i][j] = '#'
            if stuck_in_loop(arr):
                count += 1
            arr[i][j] = '.'
    print(i)
print("Count:", count)
