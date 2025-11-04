employees = {"Husnain","Mobeen","Ale","Dawood","Suleman","Ahmad"}
leave_employees = {"Faizan","Ahmad"}

print("Present employees today:",employees-leave_employees)
print("Employees not present today:",leave_employees-employees)
print("Common employees :",employees&leave_employees)