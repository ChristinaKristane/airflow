Table student , Table teacher: 

1. display the number of students from one table (screenshot1)
    > SELECT COUNT(*) as count FROM student WHERE teschers='Ivanov' 

without duplicated id's (screenshot2):

    > SELECT COUNT(DISTINCT student.student_id) FROM student WHERE teschers= 'Ivanov'    

2 . combining the table for all parameters  (screenshot3):

    > select * from student
join teacher on teacher.teacher_id = teacher.teacher_id
where teacher.teacher_id= 11  

3 . All students from the teacher  (screenshot4):

    > select student.student_id from student
join teacher on teacher.teacher_id = teacher.teacher_id
where teacher.teacher_id = 11    


5. count the number of students (screenshot5):

    > SELECT COUNT(DISTINCT student.student_id) FROM student
join teacher on teacher.teacher_id = teacher.teacher_id
where teacher.teacher_id = 11   

6. all students and teacher (screenshot6):

    > SELECT student.student_id, student.teschers FROM student
join teacher on teacher.teacher_id = teacher.teacher_id
where teacher.teacher_id = 11  

Table student_teacher:

7. count numbers of students (screenshot7)

    > SELECT COUNT(DISTINCT student_teacher.student_id) FROM student_teacher WHERE teacher_id= 11    

8. students id and  teacher id  (screenshot8)

    > SELECT student_teacher.student_id, student_teacher.teacher_id FROM student_teacher WHERE teacher_name = 'Ivanov'  
