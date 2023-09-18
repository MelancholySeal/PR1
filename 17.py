count,m = 0,0
f = open('17.txt')
arr = [int(i) for i in f]
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] * arr[j] % 34 != 0:
            count += 1 
            m = max(m, arr[i] + arr[j])
print(count, m)