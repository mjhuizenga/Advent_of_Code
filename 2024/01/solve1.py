import math

data = open("data.txt", "r").read()

# Format data into two arrays
left = []
right = []
for line in data.split('\n'):
    if line != '':
        pair = line.split('   ')
        left.append(int(pair[0]))
        right.append(int(pair[1]))

# Sort the arrays
left.sort()
right.sort()

# Find sum of distances
distance = 0
for i in range(len(left)):
    distance += math.fabs(left[i] - right[i])

print("Distance:", distance)
