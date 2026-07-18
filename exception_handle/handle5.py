file_name=input("enter the file name:")
total=0
elements=0
try:
    with open(file_name,"r") as file:
      for line in file:
        total+=int(line)
        elements+=1
    print("total marks:",total)
    print("average marks:",total/elements)
except ValueError:
   print("invalid data in file")
except FileNotFoundError:
   print("file not found") 
except ZeroDivisionError:
   print("file is empty") 
else:
   print("marks calculated successfully")
finally:
   print("thank you for using this program")            
