date = int(input("What is the date (Between 1900, and 2099)"))
if date > 2099 or date < 1900:
    idiot = True
else:
    idiot = False
while idiot:
    print("Error you stupid dumb idiot, try again")
    date = int(input("What is the date (Between 1900, and 2099)" ))

a = date % 19
b = date % 4
c = date % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e

if date == 1954 or date == 1981 or date == 2049 or date == 2076:
    dateofeaster = dateofeaster - 7
    
    
if dateofeaster <= 31:
    month = "March"
else:
    month = "April"
    dateofeaster = dateofeaster - 31
dateofeaster = str(dateofeaster)+ "th"


print(dateofeaster, "of", month)
