# while True:
#     n = int(input("What's n: "))
    
#     if n < 0:
#         continue  This tells Python to go to the next iteration of the loop
#     else:
#         break  This tells Python to break out of a loop early before finishing it's iterations

# while True:
#     n = int(input("What's n: "))

#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n: "))

        if n > 0:
            return n # return can also end a loop early

def meow(n):
    for _ in range(n):
        print("meow")

main()