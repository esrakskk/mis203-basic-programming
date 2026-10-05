# Week 3 Lab - Order Approval Policy

## Test Note

I tested the order approval program with order amounts of 499.99 TRY, 500 TRY, and 500.01 TRY.

| Order Amount | Member | Expected Result |
|---:|---|---|
| 499.99 TRY | Yes | Approved, no discount |
| 500 TRY | Yes | Approved, 10% discount |
| 500.01 TRY | Yes | Approved, 10% discount |

After testing, I changed the discount condition to `order_amount >= 500` so that the customer receives the discount starting exactly at 500 TRY.
