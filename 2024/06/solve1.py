data = open("./data.txt", "r").read().strip()

turn_map = {'>': 'v', 'v': '<', '<': '^', '^': '>'}


def make_move(arr):
    # find the arrow and do a movement
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == '.' or arr[i][j] == '#' or arr[i][j] == 'X':
                continue
            match arr[i][j]:
                case '^':
                    x = 0
                    y = -1
                case '>':
                    x = 1
                    y = 0
                case 'v':
                    x = 0
                    y = 1
                case '<':
                    x = -1
                    y = 0
            if i+y >= len(arr) or i+y < 0 or j+x >= len(arr[0]) or j+x < 0:
                arr[i][j] = 'X'
                return True
            if arr[i+y][j+x] == '.' or arr[i+y][j+x] == 'X':
                arr[i+y][j+x] = arr[i][j]
                arr[i][j] = 'X'
            elif arr[i+y][j+x] == '#':
                arr[i][j] = turn_map[arr[i][j]]
            return False


# print(data)
arr = [list(line) for line in data.split("\n")]

while not make_move(arr):
    pass
count = 0
for row in arr:
    count += row.count('X')

print("Count:", count)
