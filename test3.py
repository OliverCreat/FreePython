#operators
price = 25
print(price >10 and price < 30)

#and (both)
#or (at least one)
#not (opposite)

#conditional statements
temperature = input("What is temperature today? ")
temperature = int(temperature)
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30]
    print("It's a nice day")
elif temperature > 10: # (10, 20]
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")