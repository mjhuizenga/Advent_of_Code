
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


def update_robot(arr, index):
    arr[index][0] += arr[index][2]
    arr[index][1] += arr[index][3]
    arr[index][0] %= 101
    arr[index][1] %= 103


arr = get_data("./data.txt")

for row in arr:
    print(row)

for j in range(100):
    for i in range(len(arr)):
        update_robot(arr, i)

quads = [0, 0, 0, 0]
for robot in arr:
    if robot[0] < 50 and robot[1] < 51:
        quads[0] += 1
    if robot[0] > 50 and robot[1] < 51:
        quads[1] += 1
    if robot[0] < 50 and robot[1] > 51:
        quads[2] += 1
    if robot[0] > 50 and robot[1] > 51:
        quads[3] += 1
print("Count:", quads[0]*quads[1]*quads[2]*quads[3])
