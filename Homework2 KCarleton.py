"""
Benny's Burger Menu 
"""
#Variables-prices for each menu item
beef=5.75
beyond_beef=6.25
double_patty=2.00
triple_patty=3.50
cheese_topping=0.50
bacon_topping=1.25
avocado_topping=0.75
chili_topping=2.50
fries=2.00
onion_rings=2.25

order_summary=0
sales_report=()

beef_count=0
beyond_count=0


#Input variables
meat=(input("Please choose beef(b) or beyond beef (y): "))
while meat != 'b' and meat != 'y':
    meat=(input("Please choose beef(b) or beyond beef (y): "))
patties=(input("Would you like to make it a double(d) or triple(t) or n?: "))
toppings=(input("Would you like to add toppings? (y or n): "))
cheese=(input("Would you like cheese? (y or n): "))
bacon=(input("Would you like bacon? (y or n): "))
avocado=(input("Would you like avocado? (y or n): "))
chili=(input("Would you like chili? (y or n): "))
sides=(input("Would you like fries (f) or rings(r) or No (n):"))

#To make sure all inputs are upper
meat=meat.upper()
patties=patties.upper()
toppings=toppings.upper()
cheese=cheese.upper()
bacon=bacon.upper()
avocado=avocado.upper()
chili=chili.upper()
sides=sides.upper()

print("Order Summary:")
print("-"*15)

for i in meat:
    if 'B' in meat:
        print("Beef Burger")
        order_summary+=float(beef)
        beef_count+=1
    if 'Y' in meat:
        print("Beyond Beef Burger")
        order_summary+=float(beyond_beef)
        beyond_count+=1

for i in patties:
    if 'D' in patties:
        print("Double")
        order_summary+=float(double_patty)
    if 'T' in patties:
        print("Triple")
        order_summary+=float(triple_patty)

for i in toppings:
    if 'Y' in toppings:
        print("Toppings: ") 

for i in cheese:
    if "Y" in cheese:
        print("Cheese")
        order_summary+=float(cheese_topping)

for i in bacon:
    if 'Y' in bacon:
        print("Bacon")
        order_summary+=float(bacon_topping)

for i in avocado:
    if 'Y' in avocado:
        print("Avocado")
        order_summary+=float(avocado_topping)

for i in sides:
    if 'F' in sides:
        print("Fries")
        order_summary+=float(fries)
    if 'R' in sides:
        print("Rings")
        order_summary+=float(onion_rings)


print(f'Order Total:${order_summary:.2f}')
print()
quit=(input("Press enter to continue, Q to quit: "))

quit=quit.upper()

for i in quit:
    if '\n' in quit:
        print(sales_report)
    if 'Q' in quit:
        print(sales_report)

rows=0
for x in range(rows):
    for j in range(x):
        print(x,end='*')
print(f"{'*':<30}{'*'}")
for x in range(rows+1):
    for j in range(x):
        print(x,end='*')
print(f"{'**':<30}{'**'}")
for x in range(rows+1):
    for j in range(x):
        print(x,end='*')
print(f"{'***':<30}{'***'}")
print("=========== Sales Report ===========")
rows=0
for x in range(rows):
    for j in range(x):
        print(x,end='*')
print(f"{'***':<30}{'***'}")
for x in range(rows+1):
    for j in range(x):
        print(x,end='*')
print(f"{'**':<30}{'**'}")
for x in range(rows+1):
    for j in range(x):
        print(x,end='*')
print(f"{'*':<30}{'*'}")

bey=order_summary*beyond_count
beefy=order_summary*beef_count
count=(beef_count+beyond_count)



print(f"{'Type':<18}{'Count':<10}{'Total'}")
print(f'{"Beef":<20}{beef_count:<9}{beefy:.2f}')
print(f'{"Beyond Beef":<20}{beyond_count:<9}{bey:.2f}')
print("-"*40)
print(f'{"Grand Totals:":<20}{count:<9}{order_summary:.2f}')





