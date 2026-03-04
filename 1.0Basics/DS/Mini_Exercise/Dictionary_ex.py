def grade(num):
    if(num>90 and num<=100):
        return 'A+';
    elif(num>80 and num<=90):
         return 'A';
    elif(num>70 and num<=80):
         return 'B+';
    elif(num>60 and num<=70):
         return 'B';
    elif(num>50 and num<=60):
         return 'C';
    elif(num>40 and num<=50):
         return 'D';
    else:
         return 'F';

student_marks={'A':92,'B':78,'C':56,'D':41,'E':99,'F':34}
updated_stu_dic={}
print(student_marks)
print(updated_stu_dic)
for i in student_marks.items():
     updated_stu_dic[i[0]]=grade(i[1])
print(updated_stu_dic)