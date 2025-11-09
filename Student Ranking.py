students = [("Ali", 78), ("Sara", 92), ("Zara", 85), ("Bilal", 92)]

highest = max(students, key=lambda x: x[1])[1]

print("Highest Marks:", highest)
print("Students with highest marks:")
for name, marks in students:
    if marks == highest:
        print(name)
