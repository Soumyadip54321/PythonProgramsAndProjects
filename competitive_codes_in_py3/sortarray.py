

def first_to_occur_k_times(lst, n, k):
    ktimes = {}
    for element in lst:
        if lst.count(element) >= k:
            ktimes[element] =[]
    if len(ktimes) == 0:
        return -1
    for i in range(n):
        if lst[i] in ktimes.keys():
            ktimes[lst[i]].append(i)
    first_to_occur = 0
    val = float('inf')
    for element in ktimes.keys():
        diff = (ktimes[element])[k-1]
        if diff < val:
            val = diff
            first_to_occur = element
    return first_to_occur,ktimes


print(first_to_occur_k_times([5, 4, 3, 4], 4, 3))
# print(first_to_occur_k_times([4, 2, 2, 2, 3, 4, 4, 4, 3, 2], 10, 3))
















