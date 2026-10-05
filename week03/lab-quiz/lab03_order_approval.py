order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
member = input("Is the customer a member? (yes/no): ").lower()

if requested_quantity <= 0:
    print("Order rejected: requested quantity must be greater than 0.")

elif requested_quantity > available_stock:
    print("Order rejected: insufficient stock.")

else:
    print("Order approved: requested quantity is available.")

    final_price = order_amount

    if member == "yes" and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Member discount: 10%")
    else:
        print("No discount applied.")

    print(f"Final price: {final_price:.2f} TRY")
