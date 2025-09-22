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



# Business Hours
display('Weekdays: ' + business_hours['Weekdays'] + ' | Weekends: ' + business_hours['Weekends'], target="Business_Hours")