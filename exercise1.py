#convert weight from lbs to kg and vice versa
# 1 lb = 0.45 kg
# 1 kg = 2.2 lbs

weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
weight = float(weight)

if unit == "L" or unit == "l": #or unit.upper() == "L"
    converted = weight * 0.45
    print("Weight in Kg:", converted)
else:
    converted = weight * 2.20
    print("Weight in Lbs:", converted)