data = open("data.txt", "r").read().strip()
arr = [int(x) for x in data.split(" ")]

history = {}


def find_len(stone, iterations):
    if iterations == 0:
        return 1
    if (stone, iterations) in history:
        return history[(stone, iterations)]
    history[(stone, iterations)] = sum(
        [find_len(x, iterations-1) for x in blink(stone)])
    return history[(stone, iterations)]


def blink(stone):
    ans = []
    if stone == 0:
        ans.append(1)
    elif len(str(stone)) % 2 == 0:
        tmp = str(stone)
        ans.append(int(tmp[:len(tmp) // 2]))
        ans.append(int(tmp[len(tmp) // 2:]))
    else:
        ans.append(stone * 2024)
    return ans


print(arr)
count = 0
for item in arr:
    count += find_len(item, 75)
    print(item)
print("Count:", count)
