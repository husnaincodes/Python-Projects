

transactions = [5000, -2000, 3000, -1500, 4000, -1000,-500]

deposits = 0
withdrawals = 0 

for t in transactions:
    if t > 0:
        deposits =deposits+t
    else:
        withdrawals =withdrawals+t

net_balance = deposits + withdrawals

print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Net Balance:", net_balance)
