nums=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    num = int(input(f"Enter a number {i+1}:"))
    nums.append(num)
count = 0
for num in nums:
    if num % 2 == 0:
        count += 1
print("The number of even numbers is:", count) 
print()
