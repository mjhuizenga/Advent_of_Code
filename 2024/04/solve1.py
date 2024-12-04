data = open("./data.txt", "r").read()

# Find every instance of "XMAS" in the data
count = 0


def check_mas(i, j, arr):
    print(f"({i},{j})")
    sum = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if x == 0 and y == 0:
                continue
            if (i + 3*x) < 0 or (i + 3*x) >= len(arr[0]):
                continue
            if (j + 3*y) < 0 or (j + 3*y) >= len(arr):
                continue
            if arr[i + x][j + y] == "M":
                if arr[i + 2*x][j + 2*y] == "A":
                    if arr[i + 3*x][j + 3*y] == "S":
                        sum += 1
    return sum


arr = [list(x) for x in data.split("\n")][:-1]
print(arr)
print(f"({len(arr[0])},{len(arr)})")
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 'X':
            count += check_mas(i, j, arr)

print("Count:", count)
