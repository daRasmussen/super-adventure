with open('data.txt') as file:
    data = file.readlines()
    data = [x.strip() for x in data]
    code = data[0].split(",")
    print(code)
