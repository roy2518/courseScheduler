CREATE TABLE Class (
    name VARCHAR(256) NOT NULL,
    type VARCHAR(256) NOT NULL,
    units DECIMAL(2,1) NOT NULL,
    attribute VARCHAR(256),
    rating FLOAT,
    PRIMARY KEY (name, type)
);

CREATE TABLE Corequisite (
    main_name VARCHAR(256) NOT NULL,
    main_type VARCHAR(256) NOT NULL,
    supplement_name VARCHAR(256) NOT NULL,
    supplement_type VARCHAR(256) NOT NULL,
    PRIMARY KEY(supplement_name, supplement_type),
    FOREIGN KEY(supplement_name, supplement_type) REFERENCES Class(name, type),
    FOREIGN KEY(main_name, main_type) REFERENCES Class(name, type)
);

CREATE TABLE Department (
    name VARCHAR(256) NOT NULL PRIMARY KEY
);

CREATE TABLE Professor (
    prof_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE CourseDept (
    course_name VARCHAR(256) NOT NULL,
    course_type VARCHAR(256) NOT NULL,
    dept_name VARCHAR(256) NOT NULL REFERENCES Department(name),
    PRIMARY KEY(course_name, dept_name),
    FOREIGN KEY(course_name, course_type) REFERENCES Class(name, type)
);

CREATE TABLE CourseOff (
    course_name VARCHAR(256) NOT NULL,
    course_type VARCHAR(256) NOT NULL,
    course_id INTEGER NOT NULL,
    time VARCHAR(256) NOT NULL,
    PRIMARY KEY(course_name, course_type, course_id),
    FOREIGN KEY(course_name, course_type) REFERENCES Class(name, type)
);

CREATE TABLE CourseProf (
    course_name VARCHAR(256) NOT NULL,
    course_type VARCHAR(256) NOT NULL,
    course_id INTEGER NOT NULL,
    rating FLOAT,
    prof_id INTEGER NOT NULL REFERENCES Professor(prof_id),
    PRIMARY KEY(course_name, course_type, course_id, prof_id),
    FOREIGN KEY(course_name, course_type, course_id) REFERENCES CourseOff(course_name, course_type, course_id)
);

CREATE TABLE Schedule (
    net_id VARCHAR(256) NOT NULL,
    sched_num INTEGER NOT NULL,
    course_name VARCHAR(256) NOT NULL,
    course_type VARCHAR(256) NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY(net_id, sched_num, course_name, course_type, course_id),
    FOREIGN KEY(course_name, course_type, course_id) REFERENCES CourseOff(course_name, course_type, course_id)
);
