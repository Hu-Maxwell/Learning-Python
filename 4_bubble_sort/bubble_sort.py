num = input("Enter the numbers seperated by spaces.")

# num_list is now a list of strings
num_list = num.split() 

# map(type, iterable) takes an iterable then changes all of it into the map data type
# an iterable is something that is returned one at a time
# inside mapped_list, it has a reference (conceptually similar to pointer, but different name) to the iterable (which is num_list in string form)
# and the type it will be converted to. so if you change something in num_list after it is mapped, the map will also be affected. 

mapped_list = map(int, num_list)

# list() turns the map data type into a list data type
num_list = list(mapped_list)

# bubble sort
n = len(num_list)
for i in range(n - 1): 
    swapped = False
    for j in range(n - 1 - i):
        if num_list[j] > num_list[j + 1]:
            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
            swapped = True
    if not swapped: 
        break

for x in range(0, len(num_list)):
    print(f"{num_list[x]} ")