CREATE TABLE users ( 
    user_id        INTEGER,
    user_email               VARCHAR NOT NULL,
    subject_id        INTEGER
);

CREATE TABLE subject ( 
    subject_id        INTEGER,
    subject_title     VARCHAR NOT NULL
);

CREATE TABLE student ( 
    user_id        INTEGER,
    level               VARCHAR,
    education_form        VARCHAR,
	subject_id        INTEGER
);

CREATE TABLE group_student ( 
    user_id        INTEGER,
    group_id     INTEGER
);

CREATE TABLE teacher ( 
    teacher_id        INTEGER,
    email               VARCHAR NOT NULL,
    group_id        INTEGER
);