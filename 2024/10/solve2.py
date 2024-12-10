import copy
data = open("./data.txt", "r").read().strip()
arr = [[int(cell) for cell in line] for line in data.split("\n")]


def dfs(arr, i, j):
    # recursively look in every direction for an increasing
    # slope
    if arr[i][j] == 9:
        return 1
    count = 0
    if i > 0:
        if arr[i-1][j] == arr[i][j] + 1:
            count += dfs(arr, i-1, j)
    if j > 0:
        if arr[i][j-1] == arr[i][j] + 1:
            count += dfs(arr, i, j-1)
    if i < len(arr)-1:
        if arr[i+1][j] == arr[i][j] + 1:
            count += dfs(arr, i+1, j)
    if j < len(arr[0])-1:
        if arr[i][j+1] == arr[i][j] + 1:
            count += dfs(arr, i, j+1)
    return count


# for row in arr:
#     print(row)

count = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            # print("Found a trailhead")
            tmp = copy.deepcopy(arr)
            count += dfs(tmp, i, j)
print("Count:", count)
