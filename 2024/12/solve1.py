import copy
data = open("./data.txt", "r").read().strip()

arr = [list(line) for line in data.split("\n")]

# for row in arr:
#     print(row)
ans = [[0]*len(arr[0]) for _ in range(len(arr))]


def calc_border(i, j):
    ch = arr[i][j]
    count = 0
    if i == 0 or arr[i-1][j] != ch:
        # print("Left:", arr[i-1][j])
        count += 1
    if j == 0 or arr[i][j-1] != ch:
        # print("Up:", j)
        count += 1
    if i == len(arr)-1 or arr[i+1][j] != ch:
        # print("Right:", i, arr[i+1][j])
        count += 1
    if j == len(arr[0])-1 or arr[i][j+1] != ch:
        # print("Down:", j, arr[i][j+1])
        count += 1
    return count


def spread_calc(coverage, ans, val, i, j, ch):
    coverage[i][j] = '.'
    ans[i][j] += val
    if i > 0 and coverage[i-1][j] == ch:
        spread_calc(coverage, ans, val, i-1, j, ch)
    if j > 0 and coverage[i][j-1] == ch:
        spread_calc(coverage, ans, val, i, j-1, ch)
    if i < len(arr)-1 and coverage[i+1][j] == ch:
        spread_calc(coverage, ans, val, i+1, j, ch)
    if j < len(arr[0])-1 and coverage[i][j+1] == ch:
        spread_calc(coverage, ans, val, i, j+1, ch)


for i in range(len(arr)):
    for j in range(len(arr[0])):
        bds = calc_border(i, j)
        tmp = copy.deepcopy(arr)
        spread_calc(tmp, ans, bds, i, j, arr[i][j])
    print(i)

print("Count:", sum([sum(row) for row in ans]))
