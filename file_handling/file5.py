with open("demo.txt","w") as file:
    file.write("10")
    file.write("\n20")
with open("demo.txt","r") as file:
    print(file.read())    