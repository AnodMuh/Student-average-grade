numOfStudent=eval(input("Enter number of the students:"))
average= 0;
grade=0;
sumOfgrade=0;
for i in range(numOfStudent):
    grade = eval(input("Enter grade of the students "+str(i+1)+"please: "))
    sumOfgrade =sumOfgrade + grade;
    
average=sumOfgrade//numOfStudent;
print("the students average grade is "+str(average))