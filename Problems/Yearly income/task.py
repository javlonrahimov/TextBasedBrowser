with open('salary.txt') as f1, \
        open('salary_year.txt', "a", encoding='utf-8') as f2:
    for line in f1:
        f2.write(str(12 * int(line.strip())) + "\n")
