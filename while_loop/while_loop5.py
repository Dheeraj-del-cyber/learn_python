password= input("enter the password:")
attempt=1
while password !="dheeraj" and attempt<5:
    print("wrong password")
    print("attempts left",5-attempt)
    password=input("enter the password:")
    attempt +=1
if password == "dheeraj":
    print("access granted")
else:
    print("access denied")