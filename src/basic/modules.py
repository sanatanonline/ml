try:
    data = open('sketch.txt')
    print(type(data))
    print(data.readline(), end='')
    data.seek(0)

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(sep=':', maxsplit=3)
            print(role, end="")
            print("said", end="")
            print(line_spoken, end="")
        except ValueError:
            pass

    data.close()
except IOError:
    print("File not found")
