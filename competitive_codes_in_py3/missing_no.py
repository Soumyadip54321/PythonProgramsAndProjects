

def missing_number(input_list, n):
    sum_of_nos = int((n * (n + 1)) / 2)
    return sum_of_nos - sum(input_list)


print(missing_number([6, 1, 2, 8, 3, 4, 7, 10, 5], 10))



