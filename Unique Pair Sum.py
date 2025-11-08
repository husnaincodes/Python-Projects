nums = (2, 4, 6, 3, 5, 7)
target = int(input("Enter target sum: "))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print((nums[i], nums[j]))
