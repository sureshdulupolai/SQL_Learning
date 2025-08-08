USE School;

SELECT * FROM teacher;
SELECT * FROM student;

CREATE TABLE student_data_year(
	id INT PRIMARY KEY AUTO_INCREMENT,
    years VARCHAR(10) NOT NULL
);

CREATE TABLE student_data_month(
	id INT PRIMARY KEY AUTO_INCREMENT,
    months VARCHAR(50) NOT NULL,
    year_id INT,
    CONSTRAINT Year_Month_Connection FOREIGN KEY (year_id) REFERENCES student_data_year(id)
);

INSERT INTO student_data_year (years)
VALUES 
('2023'),
('2024'),
('2025');

INSERT INTO student_data_month (months, year_id)
VALUES 
('November', 1), -- 2023
('April', 1),    -- 2023
('November', 2), -- 2024
('April', 2),    -- 2024
('November', 3), -- 2025
('April', 3);    -- 2025

SELECT * FROM student_data_year;
SELECT * FROM student_data_month;