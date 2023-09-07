#STOCK BUY SELL

def largest_array_with_zero_sum(arr, n):
    length_list = []
    largest_length = 0
    new_list = []
    prev = 0
    max = -1
    zero_pos = 0
    for i in range(n):
        length_list.append(arr[i]+prev)
        prev = length_list[i]
    for item in length_list:
        new_list.append(item)
    length_list.reverse()

    for element in new_list:
        if not(element == 0):
            largest_length = abs(((n-1)-length_list.index(element)) - new_list.index(element))
            if largest_length > max:
                max = largest_length
        else:
            max = n - length_list.index(element)
    print(length_list, new_list, max)


# largest_array_with_zero_sum([-776, 794, 387, -648, 363, 691, 764, -539, -171, -210, -566, 783, -861, 68, 930, -21, -68, 394, -10, -228, 422, 785, 199, -314, -412, -90, -955, 863, -995, 306, 85, 337, 847, 314, 125, 583, 815, 435, -42, -86, -275, -787, -402, 755, 933, -675, -738, -225, -93, 796, -433, -466, 98, -316, -651, -300, -285, 866, 445, 441, 32, 98, 482, 710, 568, -496, 587, 307, 220, -527, 733, 504, 271, -707, 341, 797, 619, 847, 922, 380, -763, -840, -192, -33], 84)
largest_array_with_zero_sum([-1, 1, -1, 1], 4)



