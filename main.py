CREATE TABLE Departments (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);


CREATE TABLE Employees (
    id INT PRIMARY KEY,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(id)
);


CREATE TABLE Projects (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES Employees(id)
);


CREATE TABLE Tasks (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES Projects(id)
);


CREATE TABLE EmployeeTasks (
    id INT PRIMARY KEY,
    employee_id INT,
    task_id INT,
    FOREIGN KEY (employee_id) REFERENCES Employees(id),
    FOREIGN KEY (task_id) REFERENCES Tasks(id)
);



INSERT INTO Departments 
VALUES
(1, 'IT'),
(2, 'Marketing'),
(3, 'Finance');


INSERT INTO Employees 
VALUES
(1, 'Azamat',  'Tohirov',  1),
(2, 'Dilshod', 'Karimov',  2),
(3, 'Malika',  'Xasanova', 3);


INSERT INTO Projects 
VALUES
(1, 'CRM System',  1),
(2, 'Ad Campaign', 2),
(3, 'Budget Plan', 3);


INSERT INTO Tasks 
VALUES
(1, 'Backend yozish',      1),
(2, 'Reklama dizayni',     2),
(3, 'Hisobot tayyorlash',  3);


INSERT INTO EmployeeTasks 
VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);
