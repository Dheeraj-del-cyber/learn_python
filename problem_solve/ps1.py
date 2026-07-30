nums=[]
for i in range(5):
    num = int(input(f"Enter a number {i+1}:"))
    nums.append(num)
count = 0
for num in nums:
    if num % 2 == 0:
        count += 1
print("The number of even numbers is:", count)            