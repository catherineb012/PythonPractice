#9 - Calculating the Atomic weight of Hydrocarbons (Alkanes)

print("9 - Calculating the Atomic weight of Hydrocarbons (Alkanes)")
print()


carbon_atoms = int(input("Enter the number of carbon atoms: "))
hydrogen_atoms = (carbon_atoms * 2) + 2

atomic_mass = carbon_atoms * 12 + hydrogen_atoms

print("The atomic mass of C3H8 is", atomic_mass)

#when doing arithmetic calculations the computer follows the rules of BOMDAS, so make sure to put brackets where necessary
