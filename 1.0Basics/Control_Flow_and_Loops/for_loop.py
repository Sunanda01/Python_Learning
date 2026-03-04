heights=input("Enter list of heights=> ").split()
count=0
total_ht=0
for i in heights:
    count+=1

for h in range(count):
    heights[h]=int(heights[h])

for height in heights:
    total_ht+=height

avg_ht=round(total_ht/count)
print(total_ht)