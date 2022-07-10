data = open('sketch.txt')
print(type(data))

print(data.readline(), end='')

data.seek(0)

for each_line in data:
    print(type(each_line))
    print(each_line, end='')
    (role, line_spoken) = each_line.split(':')
    print(role, end="")
    print("said", end="")
    print(line_spoken, end="")

data.close()


