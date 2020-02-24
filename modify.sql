/*User looks at their first schedule*/
SELECT * FROM Schedule WHERE netid='01' AND sched_num=01;
/*User removes CS330 from their schedule*/
DELETE FROM Schedule WHERE netid='01' AND sched_num=02 AND course_name='CS330';
/*User deletes their first schedule*/
DELETE FROM Schedule WHERE netid='01' AND sched_num=01;

/*Verify delete is correct*/
SELECT * FROM Schedule;

/*User adds a class to their second schedule*/
INSERT INTO Schedule VALUES('01', 02, 'CS316', 'lec', '01');
/*How many classes in the schedule?*/
SELECT count(*) FROM Schedule WHERE netid='01' AND sched_num=02;
/*User creates a new schedule*/
INSERT INTO Schedule VALUES('01', 03, 'EOS101', 'lec', 01);
INSERT INTO Schedule VALUES('01', 03, 'CS330', 'lec', 01);
INSERT INTO Schedule VALUES('01', 03, 'CS330', 'dis', 02);
/*What times are the classes in the new schedule?*/
SELECT time FROM Schedule NATURAL JOIN CourseOff WHERE net_id='01' AND sched_num=03;
