if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
marks=[]      
for student in students:
    marks.append(student[1])
unique_marks=sorted(set(marks))
second_low=unique_marks[1]
final_students=[]
for student in students:
   if student[1]==second_low:
     final_students.append(student[0])
final_students.sort()
for i in final_students:
    print(i)      