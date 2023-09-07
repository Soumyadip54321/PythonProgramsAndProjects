
def leaders(a, n):
    l = []
    max = a[n - 1]
    l.append(a[n-1])
    for i in range(n-2, -1, -1):
        if a[i] >= max:
            l.append(a[i])
            max = a[i]
    l.reverse()
    return l


print(leaders([1,2,3,4,0], 5))

