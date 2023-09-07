
toppings = []
toppings += ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = []
for i in range(len(toppings)):
    pizza_and_prices.append([prices[i], toppings[i]])
#print(pizza_and_prices)
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0][-1]
priciest_pizza = pizza_and_prices[-1][-1]
print(cheapest_pizza,priciest_pizza)
pizza_and_prices.pop()
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
