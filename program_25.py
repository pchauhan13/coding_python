opened_file = open("a.txt", "r")
for line in opened_file.readlines():
    print(line)
opened_file.close()
