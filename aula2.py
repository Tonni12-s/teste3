
(
 id INT PRIMARY KEY,
 e-mail professor INT,
 telelfone-professor INT,
 nome-professor INT,
);

CREATE TABLE aluno
(
 e-mail aluno INT,
 telelfone-aluno INT,
 nome-aluno INT,
 id-do-aluno: INT,
 UNIQUE (id-do-aluno:)
);

CREATE TABLE aula
(
 data-aula INT,
 id INT PRIMARY KEY,
 id INT PRIMARY KEY,
 id INT PRIMARY KEY,
);

ALTER TABLE aula ADD FOREIGN KEY(id) REFERENCES professor (id)
ALTER TABLE aula ADD FOREIGN KEY(id) REFERENCES aluno (id)