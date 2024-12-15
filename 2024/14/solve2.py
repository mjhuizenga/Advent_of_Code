import argparse


def get_data(fd):
    data = open(fd, "r").read().strip()
    arr = []
    for line in data.split("\n"):
        px = int(line.split("p=")[1].split(",")[0])
        py = int(line.split(",")[1].split(" ")[0])
        vx = int(line.split("v=")[1].split(",")[0])
        vy = int(line.split("v=")[1].split(",")[1])
        arr.append([px, py, vx, vy])
    return arr


def display(floor):
    for row in floor:
        for tile in row:
            if tile != 0:
                print('#', end='')
            else:
                print(".", end='')
        print()


def look_like_tree(floor, diff):
    # thic = 0
    # for i in range(8):
    #     layer = sum([sum(row) for row in floor[i*10:(i*10+10)]])
    #     if layer > thic:
    #         thic = layer
    #     else:
    #         return False
    # return True

    top = sum([sum(row) for row in floor[:25]])
    middle = sum([sum(row) for row in floor[25:50]])
    bottom = sum([sum(row) for row in floor[50:]])
    if top < (middle-diff) and top+middle < (bottom-diff):
        display(floor[:25])
        print()
        display(floor[25:50])
        print()
        display(floor[50:])
        return True
    return False


def update_robot(arr, index):
    arr[index][0] += arr[index][2]
    arr[index][1] += arr[index][3]
    arr[index][0] %= 101
    arr[index][1] %= 103


arr = get_data("./data.txt")
parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help')
parser.add_argument("count")
args = parser.parse_args()

# for j in range(int(args.count) * 20, int(args.count) * 20 + 20, 1):
for j in range(6243):
    for i in range(len(arr)):
        update_robot(arr, i)
floor = [[0]*101 for _ in range(103)]
for robot in arr:
    floor[robot[1]][robot[0]] = 1
display(floor)
# if look_like_tree(floor, int(args.count)):
#     print(j)
# display(floor)
