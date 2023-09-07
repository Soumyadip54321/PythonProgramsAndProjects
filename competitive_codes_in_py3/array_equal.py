
"""def check(arr1, arr2, length):
    count = 0
    for i in range(length):
        if arr1[i] in arr2:
            if arr2.count(arr1[i]) == arr1.count(arr1[i]):
                count += 1
            else:
                count = 0
        else:
            return False
    if count == 0:
        return False
    else:
        return True"""


def check(arr1, arr2, length):
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else:
        return False


print(check([1, 2, 5, 13, 19, 27], [2, 4, 15, 19, 27, 33], 6))



