
def reverse_array_in_groups(input_list, length, group):
    no_of_group_rev = int(length / group)
    start = i = 0
    while no_of_group_rev != 0:
        end = group + i - 1
        j = end
        while i <= j:
            temp = input_list[i]
            input_list[i] = input_list[j]
            input_list[j] = temp
            i += 1
            j -= 1
        i = start = end + 1
        no_of_group_rev -= 1

    end = length - 1
    while i < end:
        temp = input_list[i]
        input_list[i] = input_list[end]
        input_list[end] = temp
        i += 1
        end -= 1

    return input_list


print(reverse_array_in_groups([81, 80, 86, 80, 65, 48, 79, 14, 59, 60, 45, 3, 61, 74, 50, 22, 58, 19, 60, 98, 54, 38, 47, 6, 67, 34], 26, 20))
# print([81, 80, 86, 80, 65, 48, 79, 14, 59, 60, 45, 3, 61, 74, 50, 22, 58, 19, 60, 98, 54, 38, 47, 6, 67, 34], 26, 20)







