x = 1
y = 2

z = x + y

print(z)

x = input("What's x?: ")
y = input("what's y?: ")

z = x + y
print(z) 

z = int(x) + int(y)
print(z)

x = int(input("What's x?: "))
y = int(input("What's y?: "))

z = x + y
print(z)

print("-----FLOATS-----")

x = float(input("What's x?: "))
y = float(input("What's y?: "))

print(x + y)

x = float(input("What's x?: "))
y = float(input("What's y?: "))

z = round(x + y, 1)
print(z)
print(f"{z:,}")

print("-----FORMATING FLOATS-----")

x = float(input("What's x?: "))
y = float(input("What's y?: "))

z = x / y
print(z)

x = float(input("What's x?: "))
y = float(input("What's y?: "))

z = round(x / y, 2)
print(z)

x = float(input("What's x?: "))
y = float(input("What's y?: "))

z = x / y
print(f"{z:.2f}")