

def two_sum(nums, target):
    i = 0
    while i < len(nums):
        start = i
        end = start + 1
        while end != len(nums):
            if nums[start] + nums[end] == target:
                return start, end
            end += 1
        i += 1


#print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 3], 6))