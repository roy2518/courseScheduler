CREATE TABLE department (
    name VARCHAR(256) NOT NULL PRIMARY KEY
);

CREATE TABLE class (
    subject VARCHAR(256) NOT NULL REFERENCES department(name),
    num INTEGER NOT NULL,
    unit DECIMAL(2,1) NOT NULL,
    alp Boolean NOT NULL,
    cz Boolean NOT NULL,
    ns Boolean NOT NULL,
    qs Boolean NOT NULL,
    ss Boolean NOT NULL,
    cci Boolean NOT NULL,
    ei Boolean NOT NULL,
    sts Boolean NOT NULL,
    fl Boolean NOT NULL,
    r Boolean NOT NULL,
    w Boolean NOT NULL,
    rating FLOAT,
    description VARCHAR(256),
    PRIMARY KEY (subject, num)
);

CREATE TABLE corequisite (
    main_subject VARCHAR(256) NOT NULL,
    main_num INTEGER NOT NULL,
    main_type VARCHAR(256) NOT NULL,
    sup_subject VARCHAR(256) NOT NULL,
    sup_num INTEGER NOT NULL,
    sup_type VARCHAR(256) NOT NULL,
    PRIMARY KEY(sup_subject, sup_num, sup_type),
    FOREIGN KEY(sup_subject, sup_num) REFERENCES class(subject, num),
    FOREIGN KEY(main_subject, main_num) REFERENCES class(subject, num)
);


CREATE TABLE professor (
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);


CREATE TABLE courseoff (
    subject VARCHAR(256) NOT NULL,
    course_num INTEGER NOT NULL,
    type VARCHAR(256) NOT NULL,
    id INTEGER NOT NULL,
    mon Boolean NOT NULL,
    tues Boolean NOT NULL,
    wed Boolean NOT NULL,
    thur Boolean NOT NULL,
    fri Boolean NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    PRIMARY KEY(subject, course_num, type, id),
    FOREIGN KEY(subject, course_num) REFERENCES class(subject, num)
);

CREATE TABLE courseprof (
    subject VARCHAR(256) NOT NULL,
    course_num INTEGER NOT NULL,
    type VARCHAR(256) NOT NULL,
    id INTEGER NOT NULL,
    prof_id INTEGER NOT NULL REFERENCES professor(id),
    rating DECIMAL(2,1),
    
    PRIMARY KEY(subject, course_num, type, id, prof_id),
    FOREIGN KEY(subject, course_num, type, id) REFERENCES courseoff(subject, course_num, type, id)
);

CREATE TABLE schedule (
    net_id VARCHAR(256) NOT NULL,
    sched_num INTEGER NOT NULL,
    subject VARCHAR(256) NOT NULL,
    course_num INTEGER NOT NULL,
    type VARCHAR(256) NOT NULL,
    id INTEGER NOT NULL,
    PRIMARY KEY(net_id, sched_num, subject, course_num, type, id),
    FOREIGN KEY(subject, course_num, type, id) REFERENCES courseoff(subject, course_num, type, id)
);


