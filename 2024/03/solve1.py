import re

data = open("./data.txt", "r").read()
pattern = r'mul\(([0-9]+),([0-9]+)\)|do\(\)|don\'t\(\)'

print(len(data))

count = 0
switch = True
for match in re.finditer(pattern, data):
    print(match.group(0))
    if match.group(0) == "do()":
        switch = True
    if match.group(0) == "don't()":
        switch = False
    if match.group(0)[:4] == "mul(" and switch:
        print("mul:", match.group(1), match.group(2))
        count += int(match.group(1)) * int(match.group(2))

print("sum:", count)
