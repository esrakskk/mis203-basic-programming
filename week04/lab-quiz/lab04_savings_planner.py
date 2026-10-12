
# Week 4 Lab: Savings Goal Planner

# Get a valid starting balance
while True:
    starting_balance = float(input("Enter starting balance: "))

    if starting_balance < 0:
        print("Starting balance cannot be negative.")
    else:
        break

# Get a valid monthly deposit
while True:
    monthly_deposit = float(input("Enter monthly deposit: "))

    if monthly_deposit <= 0:
        print("Monthly deposit must be positive.")
    else:
        break

# Get a valid monthly interest rate
while True:
    interest_rate = float(input("Enter monthly interest rate (%): "))

    if interest_rate < 0:
        print("Interest rate cannot be negative.")
    else:
        break

# Get a valid savings goal
while True:
    savings_goal = float(input("Enter savings goal: "))

    if savings_goal <= 0:
        print("Savings goal must be positive.")
    else:
        break

balance = starting_balance
total_interest = 0
month = 0

# Check whether the goal is already reached
if balance >= savings_goal:
    print("Savings goal already reached!")
else:
    print("\nMonth | Interest Earned | New Balance")
    print("--------------------------------------")

    while month < 60:
        month = month + 1

        interest = balance * interest_rate / 100
        balance = balance + interest
        total_interest = total_interest + interest

        balance = balance + monthly_deposit

        print(f"{month:5} | {interest:15.2f} | {balance:11.2f}")

        if balance >= savings_goal:
            break

# Print the final results
if balance >= savings_goal:
    print(f"\nSavings goal reached in {month} months.")
else:
    print("\nSavings goal not reached within 60 months.")

print(f"Final balance: {balance:.2f}")
print(f"Total interest earned: {total_interest:.2f}")
