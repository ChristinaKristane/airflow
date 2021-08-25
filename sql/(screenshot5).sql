SELECT COUNT(DISTINCT student.student_id) FROM student
join teacher on teacher.teacher_id = teacher.teacher_id
where teacher.teacher_id = 11