from sys import stdin


arr = []
for line in stdin:
    try:
        arr.append(int(line))
    except: 
        pass

count = 0
for i in range(1, len(arr)):
    count += (arr[i] > arr[i - 1])

print(len(arr), count)

