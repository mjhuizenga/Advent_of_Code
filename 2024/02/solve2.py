import math


def dampened_check(arr):
    if increasing(arr):
        return True
    for i in range(len(arr)):
        if increasing(arr[:i] + arr[i+1:]):
            return True
    if decreasing(arr):
        return True
    for i in range(len(arr)):
        if decreasing(arr[:i] + arr[i+1:]):
            return True
    return False


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
    if dampened_check(arr):
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
