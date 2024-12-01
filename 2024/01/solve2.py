data = open("data.txt", "r").read()

# Format data into two arrays
left = []
right = []
for line in data.split('\n'):
    if line != '':
        pair = line.split('   ')
        left.append(int(pair[0]))
        right.append(int(pair[1]))

# Find sum of distances
simularity = 0
for item in left:
    simularity += right.count(item) * item


print("Simularity:", simularity)
