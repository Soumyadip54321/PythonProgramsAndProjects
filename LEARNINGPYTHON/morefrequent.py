

def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    elif lst.count(item1) < lst.count(item2):
        return item2


def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        lst[index] = 2*lst[index]
        return lst


def middle_element(lst):
    mid = len(lst)%2
    mid_index = int(len(lst)/2);
    if mid == 0:
        return (lst[mid_index]+lst[mid_index-1])/2
    else:
        return lst[mid_index]

def delete_starting_evens(lst):
    for number in lst:
        if number%2 == 0:
            lst = lst[1:]
        else:
            break
    return lst


def same_values(lst1, lst2):        #assuming both lists have equal size
    indexlst = []
    for i in range(len(lst1)):
        if lst2[i] == lst1[i]:
            indexlst.append(i)
    return indexlst


def reversed_list(lst1, lst2):
    flag = 0
    for i in range(len(lst1)):
        if lst1[i]==lst2[len(lst2)-(i+1)]:
            flag = 1
            continue
        else:
            flag = 0
            break
    if flag == 1:
        return True
    else:
        return False


def letter_check(word, letter):
    flag = 0
    for char in word:
        if char == letter:
            flag = 1
            break
    if flag == 1:
        return True
    else:
        return False


def common_letters(string_one,string_two):
    common = []
    for char in string_one:
        if char in string_two and not(char in common):
            common.append(char)
    return common


def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
      return first_name+last_name
  else:
      return first_name[:3]+last_name[:4]


def password_generator(user_name):
    password = ""
    for i in range(len(user_name)):
        password += user_name[i-1]
    return password




user_name = username_generator("Abe","Simpson")
print(password_generator(user_name))
print(user_name)
# print(common_letters("banana","nalpine"))
# print(letter_check("strawberry", "g"))
# print(more_frequent_item([2, 3, 3, 2, 3, 2, 3], 2, 3))
# print(double_index([3, 8, -10, 12], 2))
# print(reversed_list([1, 7, 3, 4], [4, 3, 7, 1]))




