#This program takes a weight and decides which method is the cheapest and displays the cost of shipping via that method

weight = float(input("Enter the weight of the package in kgs\n"))
#GROUND SHIPPING
flat_charge = 20;
ground_shipping_premium = 125;
if weight<=2:
    cost = (1.5*weight)+flat_charge
elif (weight>2) and (weight<=6):
    cost = (3.0 * weight) + flat_charge
elif (weight>6) and (weight<=10):
    cost = (4.0 * weight) + flat_charge
else:
    cost = (4.75 * weight) + flat_charge
print("Ground shipping costs:",cost,"$")
print("Premium Ground shipping costs:",ground_shipping_premium,"$");
#DRONE SHIPPING
if weight<=2:
    cost = (4.5*weight)
elif (weight>2) and (weight<=6):
    cost = (9.0 * weight)
elif (weight>6) and (weight<=10):
    cost = (12.0 * weight)
else:
    cost = (14.25 * weight)
print("Drone shipping costs:",cost,"$")



