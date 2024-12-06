data = open("./data.txt", "r").read()

rules = {}


def update_rules(line):
    left = int(line.split("|")[0])
    right = int(line.split("|")[1])
    if left in rules:
        rules[left].append(right)
    else:
        rules[left] = [right]


def ordered(update):
    arr = [int(x) for x in update.split(",")]
    for i in range(1, len(arr)):
        left = arr[:i]
        if arr[i] in rules.keys():
            for rule in rules[arr[i]]:
                if rule in left:
                    return False
    return True


for line in data.split("\n"):
    if line == "":
        break
    update_rules(line)


count = 0
updates = data.split("\n\n")[1].strip()
for update in updates.split("\n"):
    if not ordered(update):
        arr = update.split(",")
        count += int(arr[len(arr)//2])
        print(update)
print(updates)
print("Count:", count)
