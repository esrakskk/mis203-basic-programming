
# Week 5 Lab: Reusable Shipping Quote

def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_discount_rate(subtotal):
    if subtotal >= 1000:
        return 0.10
    elif subtotal >= 500:
        return 0.05
    else:
        return 0


def calculate_shipping_fee(destination):
    if destination == "local":
        return 50
    elif destination == "national":
        return 100
    else:
        return 0


def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount = subtotal * discount_rate
    final_total = subtotal - discount + shipping_fee
    return final_total


# Sample Order 1
price1 = 200
quantity1 = 3
destination1 = "local"

subtotal1 = calculate_subtotal(price1, quantity1)
discount_rate1 = calculate_discount_rate(subtotal1)
shipping_fee1 = calculate_shipping_fee(destination1)
total1 = calculate_final_total(
    subtotal1, discount_rate1, shipping_fee1
)

print("Order 1")
print("Subtotal:", subtotal1)
print("Discount rate:", discount_rate1)
print("Shipping fee:", shipping_fee1)
print("Final total:", total1)


# Sample Order 2
price2 = 300
quantity2 = 4
destination2 = "national"

subtotal2 = calculate_subtotal(price2, quantity2)
discount_rate2 = calculate_discount_rate(subtotal2)
shipping_fee2 = calculate_shipping_fee(destination2)
total2 = calculate_final_total(
    subtotal2, discount_rate2, shipping_fee2
)

print("\nOrder 2")
print("Subtotal:", subtotal2)
print("Discount rate:", discount_rate2)
print("Shipping fee:", shipping_fee2)
print("Final total:", total2)


# Assertions
assert calculate_subtotal(200, 3) == 600
assert calculate_discount_rate(499) == 0
assert calculate_discount_rate(500) == 0.05
assert calculate_discount_rate(1000) == 0.10
assert calculate_shipping_fee("local") == 50
assert calculate_final_total(600, 0.05, 50) == 620

print("\nAll tests passed!")
