if __name__=="__main__":
    from util import average
    student_info={}
    n=int(input("enter no of students: "))
    for i in range (n):
        name=input("enter name of student: ")
        marks=list(map(int,input("enter marks of student: ").split(',')))
        student_info[name]=marks
    query=input("enter name to find average:")
    print(average(student_info,query))