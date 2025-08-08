CREATE DATABASE School;

USE school;

-- Create teacher table
CREATE TABLE teacher (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject VARCHAR(100),
    hire_date DATE
);

-- Create student table
CREATE TABLE student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    class VARCHAR(10),
    birth_date DATE
);

