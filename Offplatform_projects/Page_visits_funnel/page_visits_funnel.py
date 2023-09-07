import pandas as pd
import numpy as np

#lists all users having visited,put items in cart, checkedout and finally purchased items on the website
visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

#print(visits.head(), "\n", cart.head(), "\n", checkout.head(), "\n", purchase.head())
#list that contains people visited who stacked items on their cart as well
visit_cart_list = visits.merge(cart, how="left")
#print("LIST WITH USER'S WHO VISITED AND PUT ITEMS IN CART\n", visit_cart_list.head(), visit_cart_list.info())
visit_cart_list['cart visited?'] = ~visit_cart_list.cart_time.isnull()
#print("Modified list:-\n", visit_cart_list.head())
cart_visit_list = visit_cart_list.groupby('cart visited?').user_id.count().reset_index()
#print(cart_visit_list)
cart_not_visited = visit_cart_list[visit_cart_list['cart visited?'] == 0].reset_index(drop=True)
#print("list of Users who did not place order in their carts\n", cart_not_visited.head(), "\nnumber of users who did not put items in cart\n", cart_not_visited.user_id.count())
print("% of users visiting site who did not place orders:\n", (cart_not_visited.user_id.count()/visit_cart_list.user_id.count())*100)

cart_checkout_merge = cart.merge(checkout, how='left')
#print(cart_checkout_merge.head())
user_list_notcheckout = cart_checkout_merge[cart_checkout_merge.checkout_time.isnull()].reset_index(drop=True)
#print("LIST OF USER'S WHO DID NOT CHECKOUT\n", user_list_notcheckout.head())
print("% of user's who didn't checkout=".upper(), 100*(user_list_notcheckout.user_id.count()/visit_cart_list.user_id.count()))
all_data_1 = visits.merge(purchase, how="left")
all_data_2 = all_data_1.merge(cart, how="left")
all_data = all_data_2.merge(checkout, how="left")
#print("FULL LIST\n", all_data.head())
user_checkedout = all_data[(~all_data.checkout_time.isnull()) & (all_data.purchase_time.isnull())].reset_index(drop=True)
#print("LIST OF CHECKEDOUT USERS WHO DID NOT PURCHASE\n", user_checkedout.head())
print("% OF USERS CHECKEDOUT BUT DID NOT PURCHASE\n", 100*(user_checkedout.user_id.count()/visit_cart_list.user_id.count()))
all_data['Time_to_purchase'] = all_data.purchase_time-all_data.visit_time
#print(all_data.head())
print("AVG TIME TO PURCHASE FOR A USER WHO VISITS SITE\n", all_data.Time_to_purchase.mean())

