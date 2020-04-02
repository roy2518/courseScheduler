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


