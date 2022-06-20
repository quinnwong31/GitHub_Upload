# coding: utf-8
from __future__ import with_statement
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
print("========================================================================================")
print("Part 1: Automate the Calculations")
print("========================================================================================")
loan_costs = [500, 600, 200, 1000, 450]

# Calculate the total number of loans in the list.
# Use the `len` function to calculate the total number of loans in the list.
num_loans = len(loan_costs)
# Print the number of loans from the list
print(f"number of loans = {num_loans}")

# Calculate the total value (sum) of all loans in the list.
# Use the `sum` function to calculate the total of all loans in the list.
total_amount_loans = sum(loan_costs)
# Print the total value of the loans
print(f"total amount of loans = {total_amount_loans}")

# Using the sum of all loans and the total number of loans, calculate the average loan price.
avg_loan_amount = total_amount_loans / num_loans
# Print the average loan amount
print(f"average loan amount = {avg_loan_amount}")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""
print("\n")
print("========================================================================================")
print("Part 2: Analyze Loan Data")
print("========================================================================================")
# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_value = loan.get("future_value")
print(f"future_value = {future_value}")

remaining_months = loan.get("remaining_months")
print(f"remaining_months = {remaining_months}")


# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
DISCOUNT_RATE = .20

#   Calculate the fair value of the loan using the present value formula and a 20% discount rate
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
present_value = future_value / (1 + DISCOUNT_RATE / 12) ** remaining_months
print(f"present_value = {present_value}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price")
if present_value >= loan_price:
    print("The present_value is greater than or equal to the loan_cost.")
    print("The loan is worth buying.")
else:
    print("The present_value is less than the loan cost. ")
    print("The loan is too expensive.")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

print("\n")
print("========================================================================================")
print("Part 3: Perform Financial Calculations")
print("========================================================================================")

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#
# This function returns the `present_value` for the loan.
#


def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    print(f"calculating present_value...")
    print(f"future_value = {future_value}")
    print(f"remaining_months = {remaining_months}")
    print(f"annual_discount_rate = {annual_discount_rate}")
    present_value = future_value / \
        (1 + annual_discount_rate / 12) ** remaining_months
    return present_value


# Use the function to calculate the present value of the new loan given below.
# Use an `annual_discount_rate` of 0.2 for this new loan calculation.
present_value = calculate_present_value(
    future_value, remaining_months, DISCOUNT_RATE)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
print("\n")
print("========================================================================================")
print("Part 4: Conditionally filter lists of loans")
print("========================================================================================")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan.get("loan_price") < 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print(f"inexpensive_loans = {inexpensive_loans}")


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
print("\n")
print("========================================================================================")
print("Part 5: Save the results")
print("========================================================================================")

# Set the output header
header = ["loan_price", "remaining_months",
          "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    # Create a csvwriter
    print("Creating csvwriter...")
    csvwriter = csv.writer(csvfile)

    # Write the header to the CSV file
    print("Writing header to the CSV file...")
    csvwriter.writerow(header)

    # Write the values of each row from inexpensive_loans list
    print("Write the values of each row from inexpensive loans list...")
    for row in inexpensive_loans:
        print(f"row = {row.values()}")
        csvwriter.writerow(row.values())

    print("Finished writing to CSV file.")
