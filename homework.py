#在 student 表中查询系别是‘计算机’的学生的所有信息，并按 Sno 降序排列。
select * from student order by Sno desc 
#把 course 表中课程号为 3 的课程的学分修改为 3
update course set grade = 3 where classid=3
#在student表中查询年龄大于18的学生的所有信息，并按学号降序排列
select * from student where Sage > 18 order by  Sno desc
#在以上三个表中查询选的课程的“学分”为3，并且成绩大于80的学生的学号、姓名和性别
select Student.Sno,Student.Sname,Student.Ssex from course join sc on course.id=sc.courseid join Student on Student.id=sc.id where sc.grade>80 and course.grade=3