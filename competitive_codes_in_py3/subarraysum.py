
def sub_array_sum(input_list, n, s):
    if sum(input_list) < s:
        return [-1]
    elif sum(input_list) == s:
        return 1, n
    else:
        start = 0
        while start < n:
            # start = i
            end = n
            sum_of_subarray = sum(input_list[start:end])
            while sum_of_subarray > s:
                end -= 1
                sum_of_subarray = sum(input_list[start:end])
            if s == sum_of_subarray:
                return start + 1, end
            start += 1
        return [-1]




#print(sub_array_sum([1, 2, 3, 7, 5], 5, 12))
#print(sub_array_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 35))
print(sub_array_sum([101, 168, 93, 188, 133, 157, 175], 7, 167))









