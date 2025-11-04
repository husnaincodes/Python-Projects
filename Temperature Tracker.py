temps = (30, 32, 33, 31, 29, 35, 36)

hottest = max(temps)
coolest = min(temps)

print(f"Hottest Temperature : {hottest}°C")
print(f"Coolest Temperature :{coolest}°C")
print("Day above 32°C")
for temp in temps:
    if temp>32:
        print(temp)
