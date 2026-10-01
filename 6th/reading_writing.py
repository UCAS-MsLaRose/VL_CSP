# VL, Reading and Writing to Files

with open('6th/practice.txt', "r+") as file:
    content = file.read()
    print(content)
    word = content.find("LaRose")
    lengeth = len("LaRose")
    content += " Treyson!"
    file.write(content)

with open("6th/practice.txt", "a") as file:
    file.write("Another line")