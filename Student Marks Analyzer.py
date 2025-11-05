marks = [45, 67, 89, 34, 76, 50, 92, 38]

highest = lowest = marks[0]
total = 0
passed = failed = 0

for m in marks:
    total += m
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    if m >= 50:
        passed += 1
    else:
        failed += 1

average = total / len(marks)

print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Average Mark:", average)
print("Passed:", passed)
print("Failed:", failed)
