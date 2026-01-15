def print_separator(name):
    print(f"{"-" * 10}{name}{"-" * 10}")

print_separator("Lists")

students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

for student in students:
    print(student)

for i in range(len(students)):
    print(f"{i + 1}. {students[i]}")

print_separator("Dictionaries")

# Dictionaries are data structures that allows associating keys with values

students.append("Draco")
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students: This only prints the names of the students
#     print(student)

# for student in students:
#     print(student, students[student])

for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(f"Name: {student["name"]} - House: {student["house"]} - Patronus: {student["patronus"]}")