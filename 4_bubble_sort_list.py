list = [5, 4, 2, 1, 3]
n = len(list)

# bubble sort
for i in range(n - 1): 
    swapped = False
    for j in range(n - 1 - i):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
            swapped = True
    if not swapped: 
        break

for x in range(0, len(list)):
    biag = list[x] 
    print(f"{list[x]} ")