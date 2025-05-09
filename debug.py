n = 6
mas = [5, 7, 4 , 3 , 8, 2]


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
    
         
print(mas)