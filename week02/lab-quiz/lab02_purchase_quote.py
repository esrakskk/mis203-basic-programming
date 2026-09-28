item1_name = input("Enter first item name: ")
item1_quantity = int(input("Enter first item quantity: "))
item1_price = float(input("Enter first item unit price: "))

item2_name = input("Enter second item name: ")
item2_quantity = int(input("Enter second item quantity: "))
item2_price = float(input("Enter second item unit price: "))

delivery_fee = float(input("Enter delivery fee: "))
tax_percentage = float(input("Enter tax percentage: "))

item1_subtotal = item1_quantity * item1_price
item2_subtotal = item2_quantity * item2_price

subtotal = item1_subtotal + item2_subtotal
tax = subtotal * (tax_percentage / 100)
final_total = subtotal + tax + delivery_fee

print("\n===== PURCHASE QUOTE =====")
print(f"{item1_name}: {item1_quantity} x {item1_price:.2f} TRY = {item1_subtotal:.2f} TRY")
print(f"{item2_name}: {item2_quantity} x {item2_price:.2f} TRY = {item2_subtotal:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax: {tax:.2f} TRY")
print(f"Delivery Fee: {delivery_fee:.2f} TRY")
print(f"Final Total: {final_total:.2f} TRY")
