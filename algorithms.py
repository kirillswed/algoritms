n = 6
mas = [3, 4, 4 , 2 , 1, 2]


# bubble
for run in range(n):
    for i in range(n-1-run):
        if mas[i] > mas[i+1]:
            mas[i], mas[i+1] = mas[i+1], mas[i]
          
# selection sort      
for i in range(n-1):
    for j in range(i+1, n):
        if mas[i] > mas[j]:
            mas[i], mas[j] = mas[j], mas[i]

# insertion sort
for i in range(1, n):
    for j in range(i, 0, -1):
        if mas[j] < mas[j-1]:
            mas[j], mas[j-1] = mas[j-1], mas[j]
        else:
            break

# count sort
n = 5 # [0, 1, 2, 3, 4]
count = [0]*n 
for i in mas:
    count[i] += 1
print(count)

# binary search 
l, r = 1, 100

while l < r:
    m = (l + r) // 2
    resp = input(f'x > {m}? ')
    if resp == 'yes':
        l = m + 1
    else:
        r = m

print(f'x = {l}')
