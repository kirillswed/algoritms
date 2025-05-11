n = 6
a = [5, 7, 4 , 3 , 8, 2]

"""Place for test my skills"""

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
            
print(a)

