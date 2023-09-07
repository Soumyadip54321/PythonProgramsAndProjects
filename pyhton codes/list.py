#This illustrates usage of list in python3

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
# print(preferred_size)

customer_data = [[first_names[0], preferred_size[0], True], [first_names[1], preferred_size[1], False], [first_names[2], preferred_size[2], True], [first_names[3], preferred_size[3], False]]
# print(customer_data)

customer_data[-2][-1] = False
customer_data[1].remove(False)
#print(customer_data)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

