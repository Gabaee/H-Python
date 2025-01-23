print("Welcome to my pizzeria!")
# Math bs
people = int(input("How many people will be eating tonight? "))
slices = int(input("How many slices will each person eat? "))
cost_per_pizza = float(input("What is the cost per pizza? "))
tip = float(input("What percent tip will you pay in decimal form? "))
total_slices_needed = people * slices
pizzas_needed = total_slices_needed // 8
extra_slices_needed = total_slices_needed % 8
pizza_cost = pizzas_needed * cost_per_pizza
extra_slice_cost = extra_slices_needed * (cost_per_pizza / 8)
tip_amount = pizza_cost * tip
tax_amount = (pizza_cost + tip_amount) * 0.0625
total_cost = pizza_cost + tip_amount + tax_amount + extra_slice_cost
cost_per_person = total_cost / people
cost_per_slice = cost_per_pizza / 8
# Printing bs
print("The cost per pizza is $", str(cost_per_pizza))
print("The cost per individual slice is", round(cost_per_slice, 2))
print("The total number of slices needed is",str(total_slices_needed))
print("The total number of pizzas needed is", str(pizzas_needed))
print("The number of extra slices needed is", str(extra_slices_needed))
print("The pizza will cost $",str(pizza_cost), "and the extra slices will cost", round(extra_slice_cost, 2))
print("The total cost for pizza is $", str(total_cost - tip_amount - tax_amount))
print("The tip will be $", str(tip_amount))
print("The tax will be $", round(tax_amount, 2))
print("The total cost is $", round(total_cost, 2))
print("The total cost per person is $", round(cost_per_person, 2))
