
def get_data(fname):
    data = open(fname, "r").read().strip()
    byte_arr = []
    for row in data.split("\n"):
        x = int(row.split(",")[0])
        y = int(row.split(",")[1])
        byte_arr.append((y, x))
    return byte_arr


def find_path(arr, i, j, y, x):
    arr[i][j] = -1
    if i == y and j == x:
        return [(i, j)]
    # otherwise, look around
    ans = []
    if j < len(arr[0])-1 and arr[i][j+1] == 0:
        ans.append(find_path(arr, i, j+1, y, x))
    if j > 0 and arr[i][j-1] == 0:
        ans.append(find_path(arr, i, j-1, y, x))
    if i < len(arr) - i and arr[i+1][j] == 0:
        ans.append(find_path(arr, i+1, j, y, x))
    if i > 0 and arr[i-1][j] == 0:
        ans.append(find_path(arr, i-1, j, y, x))


def find_layer(arr, step):
    ans = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == step:
                if j < len(arr[0])-1 and arr[i][j+1] == 0:
                    arr[i][j+1] = step+1
                    ans.append((i, j+1))
                if j > 0 and arr[i][j-1] == 0:
                    arr[i][j-1] = step+1
                    ans.append((i, j-1))
                if i < len(arr) - 1 and arr[i+1][j] == 0:
                    arr[i+1][j] = step+1
                    ans.append((i+1, j))
                if i > 0 and arr[i-1][j] == 0:
                    arr[i-1][j] = step+1
                    ans.append((i-1, j))
    return ans


def reachable(arr):
    outer = [(0, 0)]
    i = 1
    while (arr[70][70] == 0):
        for spot in outer:
            arr[spot[0]][spot[1]] = i
        outer = find_layer(arr, i)
        if outer == []:
            return False
        i += 1
    return True


byte_arr = get_data("./data.txt")
arr = [[0]*(70+1) for _ in range(70+1)]
for i in range(2870):
    arr[byte_arr[i][0]][byte_arr[i][1]] = -1

count = 2869
while reachable(arr):
    print(count)
    count += 1
    arr[byte_arr[count][0]][byte_arr[count][1]] = -1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 0:
                arr[i][j] = 0

print("Count:", count)
print(f"coords:({byte_arr[count][0]},{byte_arr[count][1]})")
