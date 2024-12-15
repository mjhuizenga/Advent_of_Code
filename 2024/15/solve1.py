import sys
sys.setrecursionlimit(20002)


def get_data(fname):
    data = open(fname, "r").read()
    map = data.split("\n\n")[0]
    map = [list(row) for row in map.split("\n")]
    moves = data.split("\n\n")[1].replace("\n", "")
    print("num moves =", len(moves))
    return map, moves


def locate_robot(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "@":
                return i, j


def make_move(arr, i, j, di, dj):
    ti = i + di
    tj = j + dj
    while arr[ti][tj] != ".":
        ti += di
        tj += dj
    arr[ti][tj] = "O"
    arr[i+di][j+dj] = "@"
    arr[i][j] = "."


def obstructed(arr, i, j, di, dj):
    ti = i + di
    tj = j + dj
    while arr[ti][tj] != ".":
        if arr[ti][tj] == "#":
            return True
        ti += di
        tj += dj
    return False


def make_moves(arr, moves, i, j):
    if moves == "":
        return
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
    if obstructed(arr, i, j, di, dj):
        return make_moves(arr, moves[1:], i, j)
    else:
        make_move(arr, i, j, di, dj)
        return make_moves(arr, moves[1:], i+di, j+dj)


def calc_gps(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "O":
                count += i*100 + j
    return count


arr, moves = get_data("./data.txt")

i, j = locate_robot(arr)

make_moves(arr, moves, i, j)
print("Count:", calc_gps(arr))
