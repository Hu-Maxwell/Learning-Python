infile = open('input.txt', 'r')

lines_list = infile.readlines()

total_letters = 0
total_words = 0

for i in range(len(lines_list)): 
    total_words = total_words + len(lines_list[i].split())
    total_letters = total_letters + len(lines_list[i])

with open('output.txt', 'w') as outfile: 
    outfile.write(f"Total letters: {total_letters}\n")
    outfile.write(f"Total words: {total_words}\n")
    outfile.write(f"Total lines: {len(lines_list)}\n\n")

    outfile.write("File input.txt in uppercase: \n")
    for line in lines_list: 
        outfile.write(line.upper())
