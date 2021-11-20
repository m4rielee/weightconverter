print("What value are you converting from? Pounds (lb) or kilograms? (kg)")
value = input()
kg = "kilograms"
lbs = "pounds"
if value == kg:
    kgvalue = int(input("How many kilograms?"))
    lbsconverted = kgvalue * 2.205
    newvalue = lbsconverted
elif value == lbs:
    lbsvalue = int(input("How many pounds?"))
    kgconverted = lbsvalue/2.205
    newvalue = kgconverted
else:
    print("Please type kilograms or pounds only.")
print(newvalue)

