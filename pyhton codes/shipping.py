
weight = float(input("Enter your package's weight here\n"))

print("The shipping options available to you are\n")
print("For Ground Shipping press 1\n")
print("For Ground Shipping premium press 2\n")
print("For Drone Shipping press 3\n")

option = int(input("Enter the method you'd want us to ship your package safely and securely\n"))

if option == 1:
    flat_charge=20.00
    if weight <= 2:
        cost = (weight*1.50)+flat_charge
        print("Total cost would be: ", cost)
    elif (weight > 2) and (weight <= 6):
        cost = (weight*3.00)+flat_charge
        print("Total cost would be: ", cost)
    elif (weight > 6) and (weight <= 10):
        cost = (weight*4.00)+flat_charge
        print("Total cost would be: ", cost)
    else:
        cost = (weight * 4.75) + flat_charge
        print("Total cost would be: ", cost)
elif option == 2:
    print("Total cost would be: ", 125.00)
else:
    if weight <= 2:
        cost = (weight*4.50)
        print("Total cost would be: ", cost)
    elif (weight > 2) and (weight <= 6):
        cost = (weight*9.00)
        print("Total cost would be: ", cost)
    elif (weight > 6) and (weight <= 10):
        cost = (weight*12.00)
        print("Total cost would be: ", cost)
    else:
        cost = (weight * 14.25)
        print("Total cost would be: ", cost)






