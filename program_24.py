opened_file = open("a.txt", "r+")

print(opened_file.readable())
print(opened_file.read())

opened_file.close()
