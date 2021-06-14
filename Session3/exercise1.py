shirt_price = float(input('What is the price of the shirt?'))
shirt_colour = input("What colour is the shirt?")

shirt_is_colour = shirt_colour.title() == "Yellow"
shirt_in_budget = shirt_price <= 25.00 
print(f'Shirt is available within budget and correct colour: {shirt_in_budget and shirt_is_colour}')

