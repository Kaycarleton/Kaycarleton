"""
Gold Dollar Price Equivalent Calculator by Kayla Carleton 
Date of Assignment: 1/31/23
The purpose of this program is to figure out how much gold is worth (in USD) based on how many ounces/grams you have. 
This would be useful for investors to see how much their gold is worth. 
"""

OUNCE=28.3495 #Ounces to grams conversion
POUND=453.592 #pounds to grams conversion
GOLD_PRICE_OZ=1868.40
GOLD_PRICE_GRAM=65.90


total_pounds= float(input("How many pounds: "))
total_ounces= float(input("How many ounces: "))

total_weight_grams= (total_pounds * POUND ) + (total_ounces*OUNCE)
total_weight_oz= total_weight_grams / OUNCE
total_kilos= (total_weight_grams / 1000)

total_cost_oz= (total_weight_oz* GOLD_PRICE_OZ)


print(f"\nThe total weight is {total_weight_grams:,.2f} grams ({total_kilos:,.2f} kilograms)")

print(f"The total cost of {total_weight_oz:,.2f} ounces of gold is ${total_cost_oz:,.2f}\n")

print("Cost per ounce: $1868.40")
print("Cost per gram: $65.90")