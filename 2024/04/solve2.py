data = open("./data.txt", "r").read()

# Find every instance of "XMAS" in the data
count = 0


def check_mas(i, j, arr):
    print(f"({i},{j})")
    if arr[i-1][j-1] == 'M' and arr[i+1][j+1] == 'S':
        if arr[i-1][j+1] == 'M' and arr[i+1][j-1] == 'S':
            return 1
        if arr[i-1][j+1] == 'S' and arr[i+1][j-1] == 'M':
            return 1
    if arr[i-1][j-1] == 'S' and arr[i+1][j+1] == 'M':
        if arr[i-1][j+1] == 'M' and arr[i+1][j-1] == 'S':
            return 1
        if arr[i-1][j+1] == 'S' and arr[i+1][j-1] == 'M':
            return 1
    return 0


arr = [list(x) for x in data.split("\n")][:-1]
print(arr)
print(f"({len(arr[0])},{len(arr)})")
for i in range(1, len(arr)-1):
    for j in range(1, len(arr[0])-1):
        if arr[i][j] == 'A':
            count += check_mas(i, j, arr)

print("Count:", count)
