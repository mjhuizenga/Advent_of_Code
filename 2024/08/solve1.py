data = open("data.txt", "r").read().strip()

arr = [list(x) for x in data.split("\n")]
answer = [[0]*len(arr[0])]*len(arr)
answer = [[0]*len(arr[0]) for _ in range(len(arr[0]))]


def update_antinode(i, j, x, y):
    a_x = i + (i - x)
    a_y = j + (j - y)
    print(f"check: ({a_x},{a_y})")
    answer[a_x][a_y] = 1


def calc_antinodes(i, j):
    chr = arr[i][j]
    # which side is further away, and limit it based on other side
    x_range = min(i, len(arr[0])-1-i)
    y_range = min(j, len(arr)-1-j)
    for x in range(i-x_range, i+x_range+1):
        for y in range(j-y_range, j+y_range+1):
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
