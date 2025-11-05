

present = set()
leave = set()

while True:
    status = input("\nPress 'p' to add Present employee, 'a' to add Absent employee, 'q' to quit: ")

    if status == 'q':
        print("Program ended...")
        break

    elif status == 'p':
        name = input("Enter the name of employee who is present today (or type 'done' to finish): ")
        if name != "done":
            present.add(name)

    elif status == 'a':
        name = input("Enter the name of employee who is on leave today (or type 'done' to finish): ")
        if name != "done":
            leave.add(name)

    else:
        print("Invalid input, please try again.")

# Results
print("\n--- Attendance Summary ---")

print("Employees present today:", present)
print("Employees on leave today:", leave)
print("Present but not on leave:", present - leave)
print("On leave but not present:", leave - present)
print("Common in both lists (if any):", present & leave)
