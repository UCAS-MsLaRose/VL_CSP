# VL, Reading and Writing to Files

with open("7th/practice.txt", "r+") as file: #lets you read and appending
    content = file.read()
    content = "Chapter 1:\n" + content + " And Christopher Robin was sitting on his doorstep putting on his big boots."
    file.write(content)

with open("7th/practice.txt", "a") as file:
    file.write("\nWinnie the Pooh and the Blustery Day")