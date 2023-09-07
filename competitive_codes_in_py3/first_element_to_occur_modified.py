
def first_element_k_time(a, n, k):
    ktimes = {}
    first_to_occur = 0
    val = float('inf')
    for i in range(n):
        if a.count(a[i]) >= k:
            if a[i] not in ktimes.keys():
                ktimes[a[i]] = []
            ktimes[a[i]].append(i)
        if len(ktimes[a[i]]) == k and ktimes[a[i]][k-1] < val:
            val = ktimes[a[i]][k-1]
            first_to_occur = a[i]
    if len(ktimes) == 0:
        return -1
    for element in ktimes.keys():
        diff = (ktimes[element])[k - 1]
        if diff < val:
            val = diff
            first_to_occur = element
    return first_to_occur


# print(first_element_k_time([1, 7, 4, 3, 7, 7, 4, 8, 7], 9, 2))
# print(first_element_k_time([5, 4, 3, 4], 4, 3))
print(first_element_k_time([1, 1, 4, 1, 1, 4, 2, 4, 1], 9, 2))
# print(first_element_k_time([1, 7, 7, 31, 28, 28, 28, 4, 3, 4, 8, 7], 12, 3))
