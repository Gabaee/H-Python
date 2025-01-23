def area():
    d = int(input("What is the diameter in feet? ")) 
    r = d / 2
    pi = 3.14
    a = pi * r ** 2
    print("The area of the circle is", str(a), "feet squared")

def mpg():
    miles = int(input("How many miles did you drive? "))
    gallons = float(input("How many gallons of gas were used during your drive? "))
    mipg = miles / gallons
    print("Your car operated at", str(mipg), "miles per gallon")

def temp():
    ask = input("If you would like to convert celsius to fahrenheit, type C. If you would like to convert fahrenheit to celsius, type F: ")
    if ask == "F":
        celsius = int(input("What is the temperature in celsius? "))
        fahrenheit = celsius * 1.8 + 32
        print("The temperature of", celsius, "celsius, converts to", fahrenheit, "fahrenheit")
    else:
        fahrenheit = int(input("What is the temperature in fahrenheit? "))
        celsius = (fahrenheit -32) * (5/9)
        print("The temperature of", fahrenheit, "fahrenheit", "converts to", celsius, "celsius")

def investment():
    P = 10000
    N = 12
    R = .07
    T = int(input("How many years will you be investing? "))
    A = P * (1 + (R/N))**(N*T)
    print(A)

investment()
