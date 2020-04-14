Insert into Class VALUES ('CS316', 'lec', 1.0, 'QS', 5.0);
Insert into Class VALUES ('CS330', 'lec', 1.0, 'QS', 3.7);
Insert into Class VALUES ('CS330', 'dis', 0.0, NULL, NULL);
Insert into Class VALUES ('EOS101', 'lec', 1.0, 'NS', 4.3);

Insert into Corequisite VALUES ('CS330', 'lec', 'CS330', 'dis');

Insert into Department VALUES ('CS');
Insert into Department VALUES ('EOS');

Insert into Professor VALUES (1, 'Sudeepa Roy');
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

Insert into Schedule Values ('01', 01, 'CS316', 'lec', '01');
Insert into Schedule Values ('01', 01, 'CS330', 'dis', '01');
Insert into Schedule Values ('01', 01, 'CS330', 'lec', '01');
Insert into Schedule Values ('01', 02, 'EOS101', 'lec', '01');
Insert into Schedule Values ('01', 02, 'CS330', 'dis', '02');
Insert into Schedule Values ('01', 02, 'CS330', 'lec', '01');

Insert into courseofftest VALUES ('CS330', 'lec', '01', 'MW4');
Insert into courseofftest VALUES ('CS330', 'dis', '01', 'F1');
Insert into courseofftest VALUES ('CS330', 'dis', '02', 'F2');
Insert into courseofftest VALUES ('CS330', 'dis', '03', 'F3');
Insert into courseofftest VALUES ('CS316', 'lec', '01', 'TTH5');
Insert into courseofftest VALUES ('EOS101', 'lec', '01', 'MW5');