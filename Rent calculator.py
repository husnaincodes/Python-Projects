rent = int(input("Enter Your Flat/Room Rent Please : "))

food = int(input("Enter Your Food Expenses Please : "))

electricity = int(input("Enter Your Total Unit of Electircity : "))

charge = int(input("Enter the Each charge Price : "))

person = int(input("Enter Number of persons :"))

total_bill = electricity*charge
total_expense = (rent+food+total_bill)/person

print(f"Each person will pay : {total_expense} ")