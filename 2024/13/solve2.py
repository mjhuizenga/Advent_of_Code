data = open("./data.txt", "r").read()

machines = [x.split("\n") for x in data.split("\n\n")[:-1]]


def calc_tokens(machine):
    x1 = int(machine[0].split("X+")[1].split(",")[0])
    y1 = int(machine[0].split("Y+")[1])
    x2 = int(machine[1].split("X+")[1].split(",")[0])
    y2 = int(machine[1].split("Y+")[1])
    xp = int(machine[2].split("X=")[1].split(",")[0]) + 10000000000000
    yp = int(machine[2].split("Y=")[1]) + 10000000000000
    # print(x1, x2, y1, y2, xp, yp)
    a = 1
    b = 1
    min_b_x2 = 10000000000000 // x2
    for i in range(min(xp // x1, 100)):
        for j in range(min(xp // x2, 100)):
            if x1*i + x2*j == xp and y1*i + y2*j == yp:
                a = i
                b = j
                break
    if a == 1 and b == 1:
        for i in range(min(yp // y1, 100)):
            for j in range(min(yp // y2, 100)):
                if x1*i + x2*j == xp and y1*i + y2*j == yp:
                    a = i
                    b = j
                    break
    if a == 1 and b == 1:
        return 0
    return a * 3 + b


# 94a + 22b = 8400
# 34a + 67b = 5400


count = 0
for machine in machines:
    count += calc_tokens(machine)
print("Count:", count)
