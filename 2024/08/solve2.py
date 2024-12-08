data = open("data.txt", "r").read().strip()

arr = [list(x) for x in data.split("\n")]
answer = [[0]*len(arr[0])]*len(arr)
answer = [[0]*len(arr[0]) for _ in range(len(arr[0]))]


def update_antinode(i, j, x, y):
    a_x = i + (i - x)
    a_y = j + (j - y)
    print("i - x:", i - x)
    print("j - y:", j - y)
    while a_x < len(arr) and a_x >= 0 and a_y < len(arr[0]) and a_y >= 0:
        print(f"check: ({a_x},{a_y})")
        answer[a_x][a_y] = 1
        a_x = a_x + (i - x)
        a_y = a_y + (j - y)
    a_x = x
    a_y = y
    while a_x < len(arr) and a_x >= 0 and a_y < len(arr[0]) and a_y >= 0:
        print(f"check: ({a_x},{a_y})")
        answer[a_x][a_y] = 1
        a_x = a_x - (i - x)
        a_y = a_y - (j - y)


def calc_antinodes(i, j):
    chr = arr[i][j]
    # which side is further away, and limit it based on other side
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == chr and not (x == i and y == j):
                print(f"{chr}:({i},{j}) ({x},{y})")
                update_antinode(i, j, x, y)


for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] != '.':
            # check for antinodes
            calc_antinodes(i, j)
            for row in answer:
                print(row)

print("Count:", sum([sum(x) for x in answer]))
