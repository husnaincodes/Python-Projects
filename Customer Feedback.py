ratings = [1, 2, 3, 4, 5, 3, 2, 1, 5, 4, 3, 3, 2, 5, 1, 4, 2, 3, 4, 5,5,4]

for i  in range(1,6):
    count = ratings.count(i)
    print(f"Rating{i} : {count} customers")