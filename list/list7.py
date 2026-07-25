n=int(input())
numbers=[]
for i in range(n):
    number=int(input())
    numbers.append(number)
for number in numbers:
    first_digit=int(str(number)[0])
    if first_digit==7:
        print("YES")
    elif first_digit==8:
        print("YES")
    elif first_digit==9:
        print("YES")
    else:
        print("NO")        