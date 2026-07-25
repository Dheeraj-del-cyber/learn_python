n=int(input())
numbers=[]
for i in range(n):
    number=int(input())
    numbers.append(number)
for number in numbers:
    if numbers[0]==7:
        print("YES")
    elif numbers[0]==8:
        print("YES")
    elif numbers[0]==9:
        print("YES")
    else:
        print("NO")        