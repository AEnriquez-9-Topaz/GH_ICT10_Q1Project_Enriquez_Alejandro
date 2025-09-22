# data types for restaurant
from pyscript import display

# variables
restaurant_Name = 'Happy Giraffe' #string
owner_name = 'Alejandro Enriquez' #string
year_established = 2023 #integer
popular_item = 145.20 #float
has_delivery = True #boolean
product_names = ['Bean Sprouts',  'Noodles', 'Mango Shake', 'Fried Rice', 'Tokwa'] #list with an extra two products
business_hours = {'Weekdays': '6am - 8pm', 'Weekends': '8am - 8pm'} #dict
menu_prices = {'Bean Sprouts': 120.50, 'Noodles': 145.20, 'Mango Shake': 99.99, 'Fried Rice': 130.75, 'Tokwa': 30.2} #dict
common_allergens = ['Peanuts', 'Celery', 'Oat'] #list
tax_rate = 0.20 #float

# Header
display(owner_name + ', since ' + str(year_established), target="owner")
display(restaurant_Name, target="Restaurant_name")

# Menu Items
display(product_names[0], target="Bean_Sprout")
display(product_names[1], target="Noodles")
display(product_names[2], target="Mango_Shake")
display(product_names[3], target="Fried_Rice")
display(product_names[4], target="Tokwa")

# Menu Prices
display(menu_prices['Bean Sprouts'], target="Bean_Sprouts_Price")
display(menu_prices['Noodles'], target="Noodles_Price")
display(menu_prices['Mango Shake'], target="Mango_Shake_Price")
display(menu_prices['Fried Rice'], target="Fried_Rice_Price")
display(menu_prices['Tokwa'], target="Tokwa_Price")

# Equation with Tax
bean_sprouts_with_tax = menu_prices['Bean Sprouts'] * (1 + tax_rate)
display(round(bean_sprouts_with_tax, 2), target="Bean_Sprouts_with_Tax")
noodles_with_tax = menu_prices['Noodles'] * (1 + tax_rate)
display(round(noodles_with_tax, 2), target="Noodles_with_Tax")
mango_shake_with_tax = menu_prices['Mango Shake'] * (1 + tax_rate)
display(round(mango_shake_with_tax, 2), target="Mango_Shake_with_Tax")
fried_rice_with_tax = menu_prices['Fried Rice'] * (1 + tax_rate)
display(round(fried_rice_with_tax, 2), target="Fried_Rice_with_Tax")
tokwa_with_tax = menu_prices['Tokwa'] * (1 + tax_rate)
display(round(tokwa_with_tax, 2), target="Tokwa_with_Tax")

# Business Hours
display('Weekdays: ' + business_hours['Weekdays'] + ' | Weekends: ' + business_hours['Weekends'], target="Business_Hours")