
def transform_sentence(sentence):               #coOL dog
    new_string = ""
    new_string += sentence[0]
    i = 1
    while i < len(sentence):
        if sentence[i] != ' ':
            if ord(sentence[i].lower()) > ord(sentence[i-1].lower()):
                new_string += sentence[i].upper()
            elif ord(sentence[i].lower()) < ord(sentence[i-1].lower()):
                new_string += sentence[i].lower()
            else:
                new_string += sentence[i]
        else:
            new_string += sentence[i]
            i += 1
            new_string += sentence[i]
        i += 1
    return new_string


def password_checker(T, string_list):
    for i in range(T):
        condition = [0, 0, 0]
        for char in string_list[i]:
            if char.isupper() and condition[0] != 1:
                condition[0] = 1
            if char.islower() and condition[1] != 1:
                condition[1] = 1
            if char.isdigit() and condition[2] != 1:
                condition[2] = 1
        if condition.count(1) == 3:
            print("yes")
        else:
            print("no")
        print(condition)


#print(transform_sentence("a Blue MOON"))
password_checker(2, ["GfG1", "Geeks"])
