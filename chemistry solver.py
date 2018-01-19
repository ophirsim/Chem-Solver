from __future__ import print_function
def mol():
    
    
    #Defining initial values for the math to work upon
    possible_units = ["mol", "mols", "grams", "gram", "g", "liter", "liters", "L", "molecules", "molecule", "atoms", "atom", "formula unit", "formula units"]
    unit = str(raw_input("What is your unit?  "))
    quantity_of_unit = float(raw_input("How much of that unit do you have (MUST be number) "))
    desired_unit = str(raw_input("what unit do you want it to end up as?  "))
    
    #checking for any answers which would stop the code and re-input'ing them
    while unit not in possible_units:
        unit = raw_input("Try again. What is your unit?  ")
    while desired_unit not in possible_units:
        desired_unit = raw_input("Try again. What unit do you want it to end up as?  ")
    
    
    
    #making the first step from any unit to 'mol'
    if unit == "gram" or unit == "grams" or unit == "g":
        molar_mass = float(raw_input("What is the molar mass of the substance?  "))
        quantity_of_unit /= float(molar_mass)
    elif unit == "liter" or unit == "liters" or unit == "L":
        quantity_of_unit /= float(22.4)
    else:
        quantity_of_unit /= float(6.02*(10**23))
        molar_mass = float(raw_input("What is the molar mass of the substance?  "))
        
    #converting from 'mol' to desired_unit
    if desired_unit == "gram" or desired_unit == "grams" or desired_unit == "g":
        quantity_of_unit *= molar_mass
    elif desired_unit == "liter" or desired_unit == "liters" or desired_unit == "L":
        quantity_of_unit *= 22.4
    elif desired_unit == "atom" or desired_unit == "atoms":
        quantity_of_unit *= (6.02*(10**23))
    print(quantity_of_unit, desired_unit)