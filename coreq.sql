Create view coreq as select a.subject as main_subject, a.course_num as main_num, a.type as main_type, b.subject as sup_subject, b.course_num as sup_num, b.type as sup__type from courseoff a, courseoff b WHERE a.subject = b.subject and a.course_num = b.course_num and a.type = 'lec' and (b.type = 'lab' or b.type = 'dis');

Create view coreq2 as select a.subject as main_subject, a.course_num as main_num, a.type as main_type, b.subject as sup_subject, b.course_num as sup_num, b.type as sup__type from courseoff a, courseoff b WHERE a.subject = b.subject and a.course_num = b.course_num and a.type = 'lecasfd' and (b.type = 'lab' or b.type = 'dis');

Insert into corequisite (select * from coreq UNION select * from coreq2);

DROP VIEW coreq;
DROP VIEW coreq2;