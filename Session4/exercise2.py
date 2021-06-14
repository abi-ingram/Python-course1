def shopping_calculator(shopping_cost, discount_applicable):
    if shopping_cost >= 20 and discount_applicable == True:
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

shopping_calculator(45, False)