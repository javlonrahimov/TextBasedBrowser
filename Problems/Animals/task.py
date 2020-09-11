file = open('animals.txt', 'r')
file2 = open('animals_new.txt', 'w')
for line in file:
    file2.write(line.replace("\n", " "))
file.close()
file2.close()