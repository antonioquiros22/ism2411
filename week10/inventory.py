# Reflection
# 1. The most surprising thing about lists is how flexible they are. You can
#    add, remove, sort, and slice them in place, and negative indices let you
#    count from the end without knowing the length. I also did not expect
#    slicing to be so compact, like [::2] to grab every other item.
#
# 2. In a retail or sales job, you might get daily sales numbers and need to
#    flag every day above a target, or apply a discount to a whole price list.
#    In Excel that means helper columns, filters, and copying formulas by hand.
#    With a Python list, a short loop does it in a few lines and can be reused
#    on next month's data without redoing the work.

print("--- Exercise 1 Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2 Index Practice ---")
print(inventory[0])            # first item
print(inventory[-1])           # last item
middle = len(inventory) // 2   # compute the middle index from the length
print(inventory[middle])       # middle item

print("--- Exercise 3 Slicing Practice ---")
print(inventory[:3])    # first three items
print(inventory[-2:])   # last two items
print(inventory[::2])   # every other item

print("--- Exercise 4 Modify ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5 Tuple comparison ---")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught:", e)
    print("Tuples are useful for coordinates because a location should be "
          "fixed; immutability prevents accidental changes to latitude/longitude.")
print(coords)

print("--- Exercise 6 Average of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

print("--- Exercise 7 Accumulator pattern ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print("Original:", prices)
print("Discounted:", discounted)

print("--- Exercise 8 Filter above threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales:
    if s > 300:
        high_sales.append(s)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))