"""
Hourly Rate
"""
# I decided to have 50 weeks be a constant to find the annual pay. 
# The hours*wage will allow you to get how much you will be paid for one week.
# So, this set up for the weekly wage to be multiplied by 50 (number of weeks you work).
WEEKS = 50
WEEKS_PER_MONTH= 4

wage = float(input("Enter your hourly wage: "))
hours = float(input("Enter your hours per week: "))

weekly_pay = (hours*wage)

monthly_pay = (hours*wage)*WEEKS_PER_MONTH

annual_pay = (hours*wage)*WEEKS

print(weekly_pay)
print(monthly_pay)
print(annual_pay)
