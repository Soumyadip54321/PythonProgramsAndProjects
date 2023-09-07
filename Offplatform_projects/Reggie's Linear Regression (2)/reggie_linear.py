def get_y(m, b, x):
    return m*x + b


def calculate_error(m, b, point):
    x_point, y_point = point
    return abs(get_y(m, b, x_point) - y_point)


print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)
print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]


def calculate_all_error(m, b, points):
    error = 0
    for point in points:
        error += calculate_error(m, b, point)
    return error


print(calculate_all_error(1, 0, datapoints))
print(calculate_all_error(1, 1, datapoints))
print(calculate_all_error(-1, 1, datapoints))

possible_ms = [val/10 for val in range(-100, 101)]
possible_bs = [val/10 for val in range(-200, 201)]
#for val1 in possible_ms:
#    print(val1)
#for val2 in possible_bs:
#    print(val2)

smallest_error = float("inf")
best_m = best_b = 0

for slope in possible_ms:
    for intercept in possible_bs:
        difference = calculate_all_error(slope, intercept, datapoints)
        if difference < smallest_error:
            smallest_error = difference
            best_m = slope
            best_b = intercept
print(smallest_error, best_m, best_b)









