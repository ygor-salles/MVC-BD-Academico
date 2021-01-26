CREATE TABLE cursos (
	nome VARCHAR(30) PRIMARY KEY
);

CREATE TABLE alunos (
	nro_matric INTEGER PRIMARY KEY,
	nome VARCHAR(50),
	curso_id VARCHAR(30),
		FOREIGN KEY (curso_id) REFERENCES cursos(nome) ON DELETE SET NULL ON UPDATE CASCADE 
);

CREATE TABLE grades (
	ano SMALLINT,
	curso_id VARCHAR(30) UNIQUE,
	PRIMARY KEY(curso_id, ano),
		FOREIGN KEY (curso_id) REFERENCES cursos(nome) ON DELETE CASCADE ON UPDATE CASCADE 
);

CREATE TABLE disciplinas(
	codigo VARCHAR(10) PRIMARY KEY,
	nome VARCHAR(50),
	carga_horaria SMALLINT
);

CREATE TABLE grade_disciplina(
	grade_id_ano SMALLINT,
	grade_id_curso VARCHAR(30),  
	disciplina_id VARCHAR(10),
	PRIMARY KEY(grade_id_curso, grade_id_ano, disciplina_id),
		FOREIGN KEY(grade_id_curso, grade_id_ano) REFERENCES grades(curso_id, ano) ON DELETE CASCADE ON UPDATE CASCADE,
		FOREIGN KEY(disciplina_id) REFERENCES disciplinas(codigo) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE historicos (
	id SERIAL PRIMARY KEY,
	nro_matric INTEGER NOT NULL,
	semestre SMALLINT CHECK(semestre=1 OR semestre=2),
	ano SMALLINT,
		FOREIGN KEY (nro_matric) REFERENCES alunos(nro_matric) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE historico_disciplina (
	historico_id INTEGER,
	disciplina_id VARCHAR(10),
	nota_disciplina FLOAT,
	PRIMARY KEY(historico_id, disciplina_id),
		FOREIGN KEY (historico_id) REFERENCES historicos(id) ON DELETE CASCADE ON UPDATE CASCADE,
		FOREIGN KEY (disciplina_id) REFERENCES disciplinas(codigo) ON DELETE CASCADE ON UPDATE CASCADE 
);

INSERT INTO cursos(nome) VALUES ('Sistemas de Informação');
INSERT INTO cursos(nome) VALUES ('Ciencia da Computação');

INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201701, 'Ygor Salles', 'Sistemas de Informação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201702, 'Caio Ribeiro', 'Sistemas de Informação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201703, 'Leticia Alves', 'Ciencia da Computação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201704, 'Fabio Antonio', 'Sistemas de Informação');

INSERT INTO grades(ano, curso_id) VALUES (2017, 'Sistemas de Informação');
INSERT INTO grades(ano, curso_id) VALUES (2017, 'Ciencia da Computação');

INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('COM110', 'Fundamentos de Programação', 80);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('COM111', 'Estrutura de Dados 1', 96);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('MAT001', 'Calculo 1', 96);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('SIN110', 'Auditoria SI', 46);

INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'COM110');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'COM111');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'SIN110');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'COM110');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'COM111');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'MAT001');

INSERT INTO historicos(nro_matric, semestre, ano) VALUES (201701, 1, 2017);
INSERT INTO historicos(nro_matric, semestre, ano) VALUES (201701, 2, 2017);

INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina) VALUES (1, 'MAT001', 2.5);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina) VALUES (1, 'COM111', 4.7);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina) VALUES (1, 'SIN110', 9);