import math


def increasing(arr):
    for i in range(len(arr)-1):
        prev = arr[i]
        if (prev > arr[i+1]
            or math.fabs(arr[i+1] - prev) > 3
                or prev == arr[i+1]):
            return False
    return True


def decreasing(arr):
    for i in range(len(arr)-1):
        prev = arr[i]
        if (prev < arr[i+1]
            or math.fabs(arr[i+1] - prev) > 3
                or prev == arr[i+1]):
            return False
    return True


def report_safe(report):
    arr = [int(x) for x in report.split(' ')]
    if increasing(arr) or decreasing(arr):
        print("Safe:", arr)
        return True
    print("Unsafe:", arr)
    return False


fd = open("data.txt", "r")
count = 0
for line in fd:
    if report_safe(line.strip()):
        count += 1

print("Number of safe reports:", count)
