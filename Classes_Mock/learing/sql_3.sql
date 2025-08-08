USE School; 

CREATE TABLE marks(
	id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    HINDI FLOAT,
	MARATHI FLOAT,
    ENGLISH FLOAT,
    MATHS FLOAT,
    CONSTRAINT Student_Table_Connection FOREIGN KEY (student_id) REFERENCES student(student_id)
);

ALTER TABLE marks 
ADD COLUMN month_id INT,
ADD CONSTRAINT Student_Month_Connection FOREIGN KEY (month_id) REFERENCES student_data_month(id);

INSERT INTO marks (student_id, HINDI, MARATHI, ENGLISH, MATHS, month_id)
VALUES
(1, 78.5, 82.0, 85.0, 90.0, 1),  -- Suresh Taylor, November 2023
(2, 80.0, 84.5, 87.0, 91.5, 2),  -- Suresh Taylor, April 2023
(2, 65.0, 70.5, 72.0, 68.5, 3),  -- Pankaj Anderson, November 2024
(2, 68.0, 73.0, 74.5, 70.0, 4),  -- Pankaj Anderson, April 2024
(3, 88.0, 85.5, 89.0, 92.0, 5),  -- Raj Moore, November 2025
(3, 90.0, 88.5, 91.0, 94.5, 6),  -- Raj Moore, April 2025
(4, 72.5, 74.0, 70.0, 75.5, 1),  -- Adarsh Wilson, November 2023
(5, 80.0, 78.5, 83.0, 85.5, 2);  -- Faizan Clark, April 2023

TRUNCATE marks;
SELECT * FROM marks;

DELETE FROM marks 
WHERE student_id = 2 AND MATHS = 70;

CREATE VIEW Check_Mark AS 
SELECT s.student_id, s.first_name, s.last_name, m.HINDI, m.MARATHI, m.ENGLISH, m.MATHS, sm.months, sy.years
FROM student s
LEFT JOIN marks m
ON s.student_id = m.student_id
LEFT JOIN student_data_month sm
ON m.month_id = sm.id
LEFT JOIN student_data_year sy
ON sm.year_id = sy.id

UNION

SELECT s.student_id, s.first_name, s.last_name, m.HINDI, m.MARATHI, m.ENGLISH, m.MATHS, sm.months, sy.years
FROM student s
RIGHT JOIN marks m
ON s.student_id = m.student_id
RIGHT JOIN student_data_month sm
ON m.month_id = sm.id
RIGHT JOIN student_data_year sy
ON sm.year_id = sy.id;

SELECT * FROM Check_Mark;
DROP VIEW Check_Mark;

SHOW FULL TABLES WHERE Table_type = 'VIEW';

SHOW CREATE VIEW Check_Mark;

--  NOT Work Because Use Multiple Join in Views
-- DELETE FROM Check_Mark
-- WHERE first_name = 'Pankaj' AND months = 'April' AND MATHS = 70;