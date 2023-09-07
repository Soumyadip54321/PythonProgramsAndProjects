

def equillibrium(input_list, n):
    if n%2==0:
        mid=int(n/2)
    else:
        mid=int((n-1)/2)
    states_visited=[]
    while not (sum(input_list[:mid]) == sum(input_list[mid + 1:])):
        states_visited.append(mid)
        if sum(input_list[:mid])>sum(input_list[mid + 1:]):
            mid-=1
            if mid == n-1 or mid == 0 or temp==mid:
                return -1
        elif sum(input_list[:mid])<sum(input_list[mid + 1:]):
            mid+=1
            if mid == n-1 or mid == 0 or temp==mid:
                return -1


    if sum(input_list[:mid]) == sum(input_list[mid + 1:]):
        return mid+1


print(equillibrium([17, 3, 9, 14, 6, 21, 25], 7))













