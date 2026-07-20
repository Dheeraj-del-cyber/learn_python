if __name__ == '__main__':
    N = int(input())
arr=[]    
for i in range(N):    
    command=input()
    parts=command.split()
    if parts[0]=='append':
        arr.append(int(parts[1]))
    if parts[0]=='insert':
        arr.insert(int(parts[1]),int(parts[2]))
    if parts[0]=='print':
        print(arr)
    if parts[0]=='remove':
        arr.remove(int(parts[1]))
    if parts[0]=='sort':
        arr.sort()  
    if parts[0]=='pop':
        arr.pop()   
    if parts[0]=='reverse':
        arr.reverse()       
