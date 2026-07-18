try:
    with open("demo.txt","r") as file:
      print(file.read())
except:
   print("file not found")      


