# coding: utf-8
import csv
import os
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!
# len is used in this array to calculate the number of objects stored in the loan list.
number_of_loans = len(loan_costs)
# the number of loans is now printed with descriptive message using the f string.
print(f"the number of loans in the list is :, {number_of_loans}")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!
# the sum function is used here to add up all the numerical values in an iterable and returns the total of those values.
total_amount = sum(loan_costs)
# the total amount of the loans is returned by printing the total amount with descriptive message using f string.
print(f"the sum of all loans in the list is :, ${total_amount}")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!
# the average loan amount is calculated by dividing the total amount or sum of the loan cost in line 32 by the number of loans  already calculated using the len function in line 23.
Average_loan_amount = sum(loan_costs)/number_of_loans
# the average loan amount is printed along with descriptive message using f string.
print(f"Average loan amount is :, ${Average_loan_amount}")

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

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!
# Using the get() function on the additiona dictionary information  for loan in line 69, each of the variables line 70 to 73 are printed along with descriptive messages.
print(f"The current loan price is :, ${loan.get('loan_price')}")

print(f"The remaining loan months is :, {loan.get('remaining_months')}")

print(f"The repayment interval is :, {loan.get('repayment_interval')}")

print(f"Future Value of loan is :, ${loan.get('future_value')}")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# YOUR CODE HERE!
# the minumum return is given as 20%, this is declared in line 94 as discout rate.
discount_rate = 0.2
# the present value is declared below using the formular 'Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months'
# Future value given in 86 and remaining months on line 82 
present_value = loan.get("future_value") / (1+ discount_rate/12)**(loan.get("remaining_months"))
# present value is calculated and print below with descriptive message.
print(f"Present value for the remaining months is :, ${present_value :.2f}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!
# a conditional statement is declared in line 107  to determine if the loan is really worth, or if it make sense to buy the loan at its cost
if present_value in loan >= loan.get("loan_price"):
# if the present value is less than the loan, the print function returns the message that the loan is worth the cost to buy it in line 109 
    print("the loan is worth at least the cost to buy it")
else:
# implies that line 107 is not true hence the print function returns the message that the loan is too expensive and not worth the price in line 112  
    print("the loan is too expensive and not worth the price")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!
# Using the new loan dictionary given in lines 126 to 131, a new function to be used in calculating present value are shown below in lines, 139, 141, 143 and 145, however line 143 is not a required output so it is commented out.
# get () function accepts a key as an argument and returns the value associated with that key in the dictionary, hence it is used here to code 
new_loan.get('loan_price')

new_loan.get('remaining_months')

# new_loan.get('repayment_interval')

new_loan.get('future_value')

# The `annual_discount_rate` of 0.2 for the new loan is a given parameter.
annual_discount_rate = 0.2

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

# YOUR CODE HERE!
# the present value of the new loan is declared below using the formulae 'Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months'
present_value_new_loan = new_loan.get("future_value") / (1+ annual_discount_rate/12)**(new_loan.get("remaining_months"))

#present_value__new_loan = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)




# present value is calculated and printed below with descriptive message. The :.2f enables the output value to be rounded off in 2 decimal places.

print(f"Present value of the new loan is :, ${present_value_new_loan :.2f}")

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

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

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
# An empty list is created in line 202 with [] indicating that it is a list.
inexpensive_loans =[]

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
# to get the the loan prices only in the dictionary a get function is used for (loan_price:700, loan_price:500, loan_price:200, loan_price:900)
# the values of the loan price is represented by (i) 
# for i in [0 , 1, 2, 3]
#  in the for loop  in line 200 the range and len functions are used to determine the length and range of the loan price in the dictionary of loans line 172 to 197
for i in range(len(loans)):
  
# the print(loan_price in loans) using the get function in line 212 returns the array of loan prices in the dictionary.
    print(loans[i].get('loan_price'))
   
# However, only the loan prices that meets the criteria ' loan price $500 or less is required to populate the empty inexpensive loan list
# In the code below, i represents one of the elements in the list of indices, and j represents one of the elements in the list of dictionaries
# there are four indices (i) or repeatitive tasks in the dictionary, and a range of integers represented by 0 to 3 and four dictionaries represented by (j)
# len function is used here to represent the length or number of loans in the dictionary in this case 
# the zip() is used to map the similar index of multiple containers in this case four, so that they can be used just as single entity., hence 
for (i, j) in zip(range(len(loans)), loans):  
# a conditional statement is declared in line 221 and used inside the for loop, to determine if the loan_price is less than 500
    if j["loan_price"] <= 500:
# if any of the loan prices in the dictionary is equal or less than $500, then the values meeting this criteria are appended in the empty list that was created in line 202
        inexpensive_loans.append(j["loan_price"])
# the appended values in the inexpensive loans list is now printed   
# for clarity the ouput  for inexpensive loans is printed with a descriptive message in line 226 
print(f"The inexpensive loan is :, ${inexpensive_loans}")

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
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
#output_path = Path("inexpensive_loans.csv")
# os is used for joining folders with file names. Analysis folder was created and inexpensive file joined to the Analysis folder.
output_path = os.path.join("Analysis", "inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
# the output file was opened as csvfilew, with w indicating mode, and newline is to remove any empty row when writing.
with open(output_path, "w",newline="") as csvfilew:
    # csv.writer is a built in function in csv module (just like a pen for writing)
    csvwriter = csv.writer(csvfilew)
    #csvwriter.writerow([header[0]]) if considering only one row of the header 
    #csv writer used to write the header
    csvwriter.writerow(header)
    # look through inexpensive list and write to the file
    for  loan in loans:
       if inexpensive_loans.count(loan["loan_price"])>0:
            csvwriter.writerow([loan["loan_price"], loan["remaining_months"], loan["repayment_interval"], loan["future_value"]])

