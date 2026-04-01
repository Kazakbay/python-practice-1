name = input("Enter customer name: ")

total_items = 0
subtotal = 0.0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    
    price = float(input("Enter price: "))
    subtotal += price
    total_items += 1

print(f"Customer : {name.upper()}")
print(f"Items : {total_items}")
print(f"Subtotal : {subtotal} KZT")

hour = int(input("Enter current hour (0-23): "))

if 6 <= hour < 12:
    label = "Morning discount"
    discount_percent = 0.10
elif 12 <= hour < 17:
    label = "No discount"
    discount_percent = 0.0
elif 17 <= hour < 22:
    label = "Evening discount"
    discount_percent = 0.05
else:
    print("Closed")
    exit()

discount_amount = subtotal * discount_percent
subtotal_after_discount = subtotal - discount_amount
tip = subtotal_after_discount * 0.10
final_total = subtotal_after_discount + tip

print("-" * 30)
print(f"Time period : {label}")
print(f"Discount : {discount_amount} KZT")
print(f"Tip (10%) : {tip} KZT")
print(f"Total : {final_total} KZT")
print("-" * 30)

print(f"Name uppercase : {name.upper()}")
print(f"Name lowercase : {name.lower()}")
print(f"Name length : {len(name)}")

if name[0].upper() == 'A' or name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")
