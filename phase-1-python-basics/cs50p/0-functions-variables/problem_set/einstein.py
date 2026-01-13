def main():

    mass_kg = int(input("Enter the mass in kg: "))

    e = einstein_formula(mass_kg)

    print(f"E: {e}")

def einstein_formula(mass):

    return mass * 300000000 ** 2

main()