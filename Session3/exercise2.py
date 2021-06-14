shopping_cost = float(input('What is the total price of your shopping? ')) 
discount_applicable = input('Do you have a discount code? y/n ')

if shopping_cost >= 20 and discount_applicable.lower() == "y":
    total_cost_before_shipping = shopping_cost * 0.9
elif shopping_cost >= 100:
    total_cost_before_shipping = shopping_cost * 0.95
else:
    total_cost_before_shipping = shopping_cost

if total_cost_before_shipping < 30:
    total_cost = total_cost_before_shipping + 5 
else:
    total_cost = total_cost_before_shipping

print(f'The total cost is £{round(total_cost, 2)}')