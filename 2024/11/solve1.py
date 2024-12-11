data = open("data.txt", "r").read().strip()
arr = [int(x) for x in data.split(" ")]


def blink(arr):
    ans = []
    for stone in arr:
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
for i in range(25):
    arr = blink(arr)
print(len(arr))
