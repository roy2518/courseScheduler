/**INSERT DATA**/
Insert into Class VALUES ('CS316', 'lec', 1.0, 'QS', 5.0);
Insert into Class VALUES ('CS330', 'lec', 1.0, 'QS', 3.7);
Insert into Class VALUES ('CS330', 'dis', 0.0, NULL, NULL);
Insert into Class VALUES ('EOS101', 'lec', 1.0, 'NS', 4.3);

Insert into Corequisite VALUES ('CS330', 'lec', 'CS330', 'dis');

Insert into Department VALUES ('CS');
Insert into Department VALUES ('EOS');

Insert into Professor VALUES (1, 'Sudeepa Roy');
Insert into Professor VALUES (2, 'Kamesh Munglala');
Insert into Professor VALUES (3, 'Emily Klein');

Insert into CourseDept VALUES ('CS316', 'lec', 'CS');
Insert into CourseDept VALUES ('CS330', 'dis', 'CS');
Insert into CourseDept VALUES ('EOS101', 'lec', 'EOS');

Insert into CourseOff VALUES ('CS330', 'lec', '01', 'MW4');
Insert into CourseOff VALUES ('CS330', 'dis', '01', 'F1');
Insert into CourseOff VALUES ('CS330', 'dis', '02', 'F2');
Insert into CourseOff VALUES ('CS330', 'dis', '03', 'F3');
Insert into CourseOff VALUES ('CS316', 'lec', '01', 'TTH5');
Insert into CourseOff VALUES ('EOS101', 'lec', '01', 'MW5');

Insert into CourseProf VALUES ('EOS101', 'lec', '01', 4.6, 3);
Insert into CourseProf VALUES ('CS330', 'dis', '01', NULL, 2);
Insert into CourseProf VALUES ('CS330', 'dis', '02', NULL, 2);
Insert into CourseProf VALUES ('CS330', 'dis', '03', NULL, 2);
Insert into CourseProf VALUES ('CS330', 'lec', '01', 3.9, 2);
Insert into CourseProf VALUES ('CS316', 'lec', '01', 4.9, 1);

Insert into Schedule Values ('jac', 1, 'COMPSCI', 330, 'dis', 1);
Insert into Schedule Values ('jac', 1, 'COMPSCI', 330, 'lec', 1);
Insert into Schedule Values ('jac', 2, 'EOS', 101, 'lec', 1);
Insert into Schedule Values ('jac', 2, 'COMPSCI', 330, 'dis', 2);
Insert into Schedule Values ('jac', 2, 'COMPSCI', 330, 'lec', 1);

/**SOME QUERIES TO UPDATE TABLES ON BEHALF OF USER**/

/*User looks at their first schedule*/
SELECT * FROM Schedule WHERE net_id='jac' AND sched_num=01;
/*User removes CS330 from their schedule*/
DELETE FROM Schedule WHERE net_id='jac' AND sched_num=02 AND subject='CS' AND course_num = 330;
/*User deletes their first schedule*/
DELETE FROM Schedule WHERE net_id='jac' AND sched_num=01;
/*Verify delete is correct*/
SELECT * FROM Schedule;
/*User adds a class to their second schedule*/
INSERT INTO Schedule VALUES('jac', 2, 'COMPSCI', 316, 'lec', 1);
/*How many classes in the schedule?*/
SELECT count(*) FROM Schedule WHERE net_id='jac' AND sched_num=2;
/*User creates a new schedule*/
INSERT INTO Schedule VALUES('jac', 03, 'EOS', 101, 'lec', 1);
INSERT INTO Schedule VALUES('jac', 03, 'COMPSCI' , 330, 'lec', 1);
INSERT INTO Schedule VALUES('jac', 03, 'COMPSCI' , 330, 'dis', 02);
/*What times are the classes in the new schedule?*/
SELECT start_time, end_time FROM Schedule NATURAL JOIN CourseOff WHERE net_id='jac' AND sched_num=3;
/*What times are the MONDAY classes in the new schedule?*/
SELECT start_time, end_time FROM Schedule NATURAL JOIN CourseOff WHERE net_id='jac' AND sched_num=3 AND mon;


