
# Week 5 Lab: Reusable Shipping Quote

## Description

This program calculates shipping quotes for two sample orders.

It uses four separate functions:
- `calculate_subtotal()`
- `calculate_discount_rate()`
- `calculate_shipping_fee()`
- `calculate_final_total()`

Discount rules:
- Subtotal below 500: 0% discount
- Subtotal from 500 to 999: 5% discount
- Subtotal 1000 or more: 10% discount

Shipping fees:
- Local: 50
- National: 100

## Testing

I tested the program with two sample orders.

I also used assert statements to test subtotal,
discount rates, shipping fees and final totals.

Test:
`calculate_discount_rate(500) == 0.05`

The test passed.

## Changes After Testing

After testing, I added a boundary test for a subtotal
of 500 to check the discount threshold.

I also added a final message to show that all tests passed.

## print() and return

`print()` displays information on the screen.

`return` sends a value back to the part of the program
that called the function.

The returned value can be stored in a variable
and used in another calculation.

## AI Usage

I used ChatGPT to understand the assignment,
learn about Python functions, and prepare the code.

I reviewed the code and tested it.
