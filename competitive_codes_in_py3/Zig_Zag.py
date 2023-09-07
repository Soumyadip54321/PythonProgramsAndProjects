
def zig_zag(input_list, n):
    i = 0
    while i <= n-1:
        first = i
        second = i+1
        last = i+2
        if second in range(n):
            if input_list[first] > input_list[second]:
                temp = input_list[first]
                input_list[first] = input_list[second]
                input_list[second] = temp
            if last in range(n):
                if input_list[second] < input_list[last]:
                    temp = input_list[second]
                    input_list[second] = input_list[last]
                    input_list[last] = temp
        else:
            break
        i = last
    return input_list


# print(zig_zag([4, 3, 7, 8, 6, 2, 1], 7))
print(zig_zag([1, 4, 3, 2], 4))







