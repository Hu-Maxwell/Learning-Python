# i think this is bubble sort? i did it from memory, so this is probably not very optimized. 
# especially how i and j go back to start after swapping, instead it should stay where it is and continue swapping until the end and then go back to 0

list = [5, 4, 2, 1, 6]

i = 0
j = 1

while True: 
    if list[i] > list[j]:
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

        i = 0
        j = 1
    else:
        i = i + 1
        j = j + 1
        if j == len(list) - 1 and list[i] < list[j]: 
            break

for x in range(0, len(list)):
    biag = list[x] 
    print(f"{list[x]} ")

# while true
    # iterate through the list, pointer1 at list[1] and pointer2 at list[2]
    # if pointer1 > pointer2, swap
    # repeat until pointer2 is at end and pointer1 < pointer2