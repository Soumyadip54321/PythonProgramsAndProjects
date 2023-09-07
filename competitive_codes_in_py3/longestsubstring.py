

def lengthoflongestsubstring(s):
    temp = ""
    str = ""
    long = -1
    for i in range(len(s)):
        temp += s[i]
        for j in range(i+1, len(s)):
            if s[j] not in temp:
                temp += s[j]
            else:
                break
        if len(temp) > long:
            long = len(temp)
            str = temp
        temp = ""
    return len(str), str


length_of_string, phrase = lengthoflongestsubstring("abcabcbb")
print(phrase, length_of_string)

