# Open a kr.csv and print it's contents.

files = open("kr.csv", "r")
while True:
    file = files.readline()
    if not file:
        break
    print(file)

files.close()
