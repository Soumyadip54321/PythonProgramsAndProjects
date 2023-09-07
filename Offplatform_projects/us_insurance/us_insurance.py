#This is a off-platform project using a csv file to analyze data.

import csv


def readfile(a, b, c, d, e, f, g):
    with open('insurance.csv', newline='') as insurance:
        dict_list = csv.DictReader(insurance)
        for item in dict_list:
            a.append(item['age'])
            b.append(item['sex'])
            c.append(item['bmi'])
            d.append(item['children'])
            e.append(item['smoker'])
            f.append(item['region'])
            g.append(item['charges'])


def print_lists(title):
    for element in title:
        print(element)


def print_all(title_list):
    for lists in title_list:
        print_lists(lists)


def field_analysis(title, category):        #function to analyse distribution in various categories of male & female
    sexes_count = {}
    for item in title:
        if not(item in sexes_count.keys()):
            sexes_count[item] = {}
            (sexes_count[item])[category[1]] = 0
        (sexes_count[item])[category[0]] = sexes_count[item].get(category[0], 0) + 1
    return sexes_count


def child_spread_count(title, fields):
    cs_count = {}
    for item in title:
        if int(item) == 0:
            cs_count[fields[0]] = cs_count.get(fields[0], 0) + 1
        elif int(item) == 1:
            cs_count[fields[1]] = cs_count.get(fields[1], 0) + 1
        else:
            cs_count[fields[2]] = cs_count.get(fields[2], 0) + 1
    return cs_count


def total_charged(title):       #func to figure out charges levied due to smoking.
    charge = 0.0
    for item in title:
        charge += float(item)
    return charge


#def smoker_classifier(title1, title2, fields):
    #sc = {}
    #for item in title1:


age = []                #Lists holding the respective values.
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
fields1 = ['no children', 'with 1 child', 'more than 2 child']
fields2 = ['female smoker', 'male smoker']
field = ['count', 'smokers']
readfile(age, sex, bmi, children, smoker, region, charges)
whole_list = [age, sex, bmi, children, smoker, region, charges]
#print("AGE:", age, "\nSEX:", sex, "\nBMI:", bmi, "\nCHILDREN:", children, "\nSMOKER:", smoker, "\nREGION:", region, "\nCHARGES:", charges)
print("SEX DISTRIBUTION WITH SMOKER COUNT:", field_analysis(sex, field))
#print("REGION DISTRIBUTION:", analysis(region))
#print("SMOKERS DISTRIBUTION:", analysis(smoker))
#print("child spread:-", child_spread_count(children, fields1))
#print("Total charges levied towards insurance in '000 USD: $"+str(total_charged(charges)/1000))






