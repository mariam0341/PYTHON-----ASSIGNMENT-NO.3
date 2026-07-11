# Bank Information
bank_name = "Python National Bank"
branch_name = "Main Branch"
branch_code = 280
city = "Busan"

# Customer Information
customer_name = "Zaviyan Zeeshan"
father_name = "Zeeshan Ahmed"
age = 28
phone_number = "03001234567"
email = "zaviyan@gmail.com"

# Account Information
account_number = "123456789"
account_type = "Savings"
currency = "PKR"
account_balance = 28000
loan_amount = 100000
atm_card_number = "1234-5678-9012-3456"

# Account Status
account_active_status = True
loan_approved_status = False

# Updated Balance
deposit = 10000
updated_balance = account_balance + deposit

print("=======================================")
print("         PYTHON NATIONAL BANK")
print("=======================================")
print()
print("Welcome", customer_name, "to", bank_name)
print()
print("--- Bank Information ---")
print("Bank Name:", bank_name)
print("Branch Name:", branch_name)
print("Branch Code:", branch_code)
print("City:", city)
print()
print("--- Customer Information ---")
print("Customer Name:", customer_name)
print("Father Name:", father_name)
print("Age:", age)
print("Phone Number:", phone_number)
print("Email Address:", email)
print()
print("--- Account Information ---")
print("Account Number:", account_number)
print("Account Type:", account_type)
print("Currency:", currency)
print("Old Balance:", account_balance)
print("Updated Balance:", updated_balance)
print("Loan Amount:", loan_amount)
print("ATM Card Number:", atm_card_number)
print()
print("--- Account Status ---")
print("Account Active:", account_active_status)
print("Loan Approved:", loan_approved_status)
print()
print("--- Data Types ---")
print(type(customer_name))
print(type(age))
print(type(account_balance))
print(type(account_active_status))
