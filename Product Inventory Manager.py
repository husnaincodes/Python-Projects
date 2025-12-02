products = [("Apple", 100), ("Banana", 60), ("Apple", 80), ("Orange", 120)]
inventory = {}

for item, qty in products:
    inventory[item] = inventory.get(item, 0) + qty
print(inventory)
