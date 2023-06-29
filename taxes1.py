"""
The tax calculator
"""

TAX_RATE = .20
STANDARD_DEDUCTION = 12000
DEPENDENT_DEDUCTION = 2000

income = float(input("Enter your income: "))
dependents = int(input("How many dependents"))

taxable_income = (income - STANDARD_DEDUCTION) - dependents * DEPENDENT_DEDUCTION
taxes_due = taxable_income * TAX_RATE

print(taxable_income)
print(taxes_due)