"""
Gabriel Sicurella
1/25/23
"""
subtotal = 0

#Sandwich
sandwich = input("What type of sandwich would you like? Chicken for $5.25, Beef for $6.25, or Tofu for $5.75? ")
print("So you chose", sandwich)
if sandwich == "Chicken" or "chicken":
    subtotal = subtotal + 5.25
elif sandwich == "Beef" or "beef":
    subtotal = subtotal + 6.25
elif sandwich == "Tofu" or "tofu":
    subtotal = subtotal + 5.75
print("----------------------------------------")

#Fries
fries = input("Would you like fries with that order? ")
if fries == "yes" or fries == "Yes":
    fries_size = input("Small $1, Medium $1.75, or Large $2.25? ")
    if fries_size == "Small" or "small":
        mega_size = input("And would you like to mega-size that? ")
        if mega_size == "yes" or "Yes":
            print("Okay, mega-sizing that")
            subtotal = subtotal + 2.25
        else:
            print("Okay no mega-size")
            subtotal = subtotal + 2.25
        
    elif fries == "Medium" or "medium":
        subtotal = subtotal + 1.75
    else:
        subtotal = subtotal + 2.25
else:
    print("Okay no fries")
print("Okay so your total right now is $", subtotal)
print("----------------------------------------")

#Drink
drink = input("Would you like a drink? ")
if drink == "yes":
    drink_size = input("Small $1, Medium $1.75, or Large $2.25 ")
    print("Okay so a", drink_size, "drink...")
    if drink == "Small":
        subtotal = subtotal + 1
    elif drink == "Medium":
        subtotal = subtotal + 1.75
    else:
        subtotal = subtotal + 2.25
else:
    print("Okay no drink")
    drink_size = "no drink"
print("----------------------------------------")
#Ketchup Packets
packets = input("Would you like any ketchup packets? ")
if packets == "Yes" or "yes":
    numofpackets = int(input("How many would you like? "))
    packet_price = numofpackets + .25
    subtotal = subtotal + packet_price
else:
    print("Okay, no packets")
#Final
print("Okay so your current total is", subtotal)
finish = input("Is everything done? ")
if finish == "yes" or "Yes":
    if sandwich == "Chicken" or "Beef" or "Tofu" and fries == "Yes" or "yes" and drink == "Yes" or "yes":
        subtotal = subtotal - 1
        print("Okay so you ordered a", sandwich, "sandwich. A", fries_size, "fry. And a", drink_size, "drink, along with", numofpackets, "ketchup packets. You ordered a combo deal of a sandwich, drink, and fry so 1 dollar will be discounted.")
    else:
        print("Okay so you ordered a", sandwich, "sandwich. A", fries_size, "fry. And a", drink_size, "drink, along with", numofpackets, "ketchup packets.")
total = subtotal
print("Okay so your total will be $", total, "have a nice day!!")
