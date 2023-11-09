

print("How much is your product today?")
current_price = float(input())

print("How much was your product in the past?")
past_price  = float(input())

print ("How many years ago was that?")
years  = float(input())

# Calculate the annual inflation rate using the formula
annual_inflation_rate = (current_price / past_price) ** (1 / years) - 1

# Convert the annual inflation rate to a percentage
annual_inflation_rate = annual_inflation_rate * 100

# Print the result
print(f"The annual inflation rate for the product is {annual_inflation_rate:.2f}%")