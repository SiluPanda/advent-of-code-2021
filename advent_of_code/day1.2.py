from sys import stdin

arr = []


for line in stdin:
    try:
        arr.append(int(line))

    except:
        continue

count = 0
for i in range(3, len(arr)):
    count += (sum(arr[i-2:i+1]) > sum(arr[i-3:i]))

print(len(arr), count)