from pyscript import display

# --- Restaurant Order System (Python Data Types) ---

# String
restaurant_name = "VICtuals"
owner_name = "Victor Buenvenida"

# Integer
year_since = 2025   

# Float
tax_rate = 0.08

# Boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

# List
product_names = ["Carbonara", "Garlic Bread", "Caesar Salad"]
beverages = ["Iced Tea", "Sparkling Water"]

# Tuple
business_hours = ("10:00 AM", "9:00 PM")

# Dictionary
menu = {
    "Carbonara": 79.99,
    "Garlic Bread": 50.00,
    "Caesar Salad": 150.00,
    "Iced Tea": 30.00,
    "Sparkling Water": 20.00
}

# Set
common_allergens = {"gluten", "dairy", "nuts"}

# --- Display restaurant information ---
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display("Menu Pricelist", target="heading1")

# --- Display menu items ---
display(product_names[0], target="prod1")
display(f"₱{menu['Carbonara']:.2f}", target="price1")

display(product_names[1], target="prod2")
display(f"₱{menu['Garlic Bread']:.2f}", target="price2")

display(product_names[2], target="prod3")
display(f"₱{menu['Caesar Salad']:.2f}", target="price3")

display(beverages[0], target="prod4")
display(f"₱{menu['Iced Tea']:.2f}", target="price4")

display(beverages[1], target="prod5")
display(f"₱{menu['Sparkling Water']:.2f}", target="price5")

# --- Display additional information ---
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

# --- Display order type ---
if is_dine_in:
    display("Dine-in Available", target="orderType")
elif has_delivery:
    display("Delivery Available", target="orderType")
elif is_takeaway:
    display("Takeaway Only", target="orderType")
