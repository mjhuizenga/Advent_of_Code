import sys
sys.setrecursionlimit(21002)


def get_data(fname):
    data = open(fname, "r").read()
    map = data.split("\n\n")[0]
    map = [list(row) for row in map.split("\n")]
    arr = []
    for row in map:
        tmp = []
        for cell in row:
            if cell == "#" or cell == ".":
                tmp.append(cell)
                tmp.append(cell)
            elif cell == "@":
                tmp.append("@")
                tmp.append(".")
            else:
                tmp.append("[")
                tmp.append("]")
        arr.append(tmp)
    moves = data.split("\n\n")[1].replace("\n", "")
    print("num moves =", len(moves))
    return arr, moves


def locate_robot(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "@":
                return i, j


def make_move(arr, i, j, di, dj):
    if di == 0:
        make_move_h(arr, i, j, dj)
    else:
        make_move_v(arr, i, j, di)


def make_move_h(arr, i, j, dj):
    tj = j + dj
    prev = "@"
    arr[i][j] = "."
    while arr[i][tj] != ".":
        tmp = arr[i][tj]
        arr[i][tj] = prev
        prev = tmp
        tj += dj
    arr[i][tj] = prev


def make_move_v(arr, i, j, di):
    ti = i + di
    prev = arr[i][j]
    arr[i][j] = "."
    while arr[ti][j] != ".":
        if arr[ti][j] == "[":
            make_move_v(arr, ti, j+1, di)
        elif arr[ti][j] == "]":
            make_move_v(arr, ti, j-1, di)
        tmp = arr[ti][j]
        arr[ti][j] = prev
        prev = tmp
        ti += di
    arr[ti][j] = prev


def obstructed_h(arr, i, j, di, dj):
    if dj == 0:
        return False
    tj = j + dj
    while arr[i][tj] != ".":
        if arr[i][tj] == "#":
            return True
        tj += dj
    return False


def obstructed_v(arr, i, j, di, dj):
    if di == 0:
        return False
    ti = i + di
    while arr[ti][j] != ".":
        if arr[ti][j] == "#":
            return True
        elif arr[ti][j] == "[":
            return obstructed_v(arr, ti, j, di, 0) or obstructed_v(arr, ti, j+1, di, 0)
        elif arr[ti][j] == "]":
            return obstructed_v(arr, ti, j, di, 0) or obstructed_v(arr, ti, j-1, di, 0)
        ti += di
    return False


def make_moves(arr, moves, i, j):
    if moves == "":
        return
    # print("Making move " + moves[0])
    match moves[0]:
        case '<':
            di = 0
            dj = -1
        case '>':
            di = 0
            dj = 1
        case '^':
            di = -1
            dj = 0
        case 'v':
            di = 1
            dj = 0
    if obstructed_h(arr, i, j, di, dj) or obstructed_v(arr, i, j, di, dj):
        return make_moves(arr, moves[1:], i, j)
    else:
        make_move(arr, i, j, di, dj)
        # for row in arr:
        #     for cell in row:
        #         print(cell, end="")
        #     print()
        # print()
        return make_moves(arr, moves[1:], i+di, j+dj)


def calc_gps(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "[":
                count += i*100 + j
    return count


arr, moves = get_data("./data.txt")
# for row in arr:
#     for cell in row:
#         print(cell, end="")
#     print()

i, j = locate_robot(arr)

# print()
make_moves(arr, moves, i, j)
# for row in arr:
#     for cell in row:
#         print(cell, end="")
#     print()
print("Count:", calc_gps(arr))
