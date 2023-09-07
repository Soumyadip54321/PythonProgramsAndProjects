

paintings_str = "The Two Fridas, My Dress Hangs Here, Tree of Hope, Self Portrait With Monkeys"
date_str = "1939, 1933, 1946, 1940"
#print(paintings_str)

p = paintings_str.split(',')
paintings = []
for painting in p:
    paintings.append(painting.strip())

for drawing in paintings:
    print(drawing)

d = date_str.replace(', ', ':')
#print(d)
dates = d.split(':')
#for date in dates:
#    print(date)

paintings = list(zip(paintings, dates))
for paint in paintings:
    print(paint)

paintings += [('The Broken Column', 1944), ('The Wounded Deer', 1946), ('Me and My Doll', 1937)]
print("The new list is\n")
for paint in paintings:
    print(paint)

print(len(paintings))
audio_tour_number = list(range(1, len(paintings)+1))

master_list = list(zip(paintings,audio_tour_number))

for item in master_list:
    print(item)


