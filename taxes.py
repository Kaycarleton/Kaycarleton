"""
The tax calculator
"""

TAX_RATE=.20
STANDARD_DEDUCTION=12000
DEPENDENT_DEDUCTION=2000

income = float(input("Enter your income: "))
dependents = int(input("How many dependents: "))

taxable_income = (income - STANDARD_DEDUCTION) - dependents* DEPENDENT_DEDUCTION
taxes_due = taxable_income * TAX_RATE

print("Taxable income: ", taxable_income)
print("Taxable income: " + "$" + str(taxable_income))
print("Taxable income: $%.2f" % (taxable_income))
#python 3
print("Taxable income: ${:,.2f}".format(taxable_income))
print(f"Taxable income: ${ taxable_income:,.2f}")

print(taxes_due)