#organising subjects and grades using python
subjects = []
subjects += ["physics","calculus","poetry","history"]
grades = [98, 97, 85, 88]
gradebook = []
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

for i in range(len(subjects)):
    gradebook.append([subjects[i], grades[i]])
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
gradebook[-1][-1] += 5

for i in range(len(gradebook)):
    if gradebook[i][0] == 'poetry':
        gradebook[i][-1]='Pass'

full_gradebook = gradebook+last_semester_gradebook
print(full_gradebook)