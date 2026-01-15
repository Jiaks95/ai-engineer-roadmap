# print("meow")
# print("meow")
# print("meow")

print("-" * 10 + "While Loops" + "-" * 10)

# The while loop while repeat a block of code over and over
# It'll only stop when a condition is met

i = 3

# while i != 0:     This would run infinitely
#     print("meow")

# while i != 0:
#     print("meow")
#     i -= 1

i = 0

while i < 3:
    print("meow")
    i += 1

print("-" * 10 + "For Loops" + "-" * 10)

# The for loop will iterate trhough a list of items

# for i in [0, 1, 2]:  With each iteration, 'i' will have the value of the corresponding item of the list
#     print("meow")

# for i in range(3):
#     print("meow")

for _ in range(3):
    print("meow")

# I never use 'i' explicitly, Python needs 'i' to store the number of the 
# iteration of the loop, but I never use it for something else.
# For such a variable without other significance, I can simply represent it
# as '_'.

print("-" * 10 + "More improvements" + "-" * 10)

print("meow" * 3)

print("meow\n" * 3, end="")