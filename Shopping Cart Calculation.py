price  = []
i = 0
while True:
    
    input_price = int(input("Enter the price of items or (Enter 0 to quit the program) : "))
    price.append(input_price)
    total = sum(price)
    if input_price==0:
        print("Program closing.....")
        break
    else:
    
        if total >5000:
            discount = total*0.10
        else:
            discount = 0
    final_amount = total-discount
    print(f"Original total = {total}")
    print(f"Discount : {discount}")
    print(f"Final Amount to pay {final_amount}")
    
