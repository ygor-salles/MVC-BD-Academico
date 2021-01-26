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
	carga_horaria SMALLINT,
	ativo BOOL DEFAULT true
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
	status VARCHAR(10) CHECK(status='APROVADO' or status='REPROVADO'),
	obrigatorio BOOL,
	PRIMARY KEY(historico_id, disciplina_id),
		FOREIGN KEY (historico_id) REFERENCES historicos(id) ON DELETE CASCADE ON UPDATE CASCADE,
		FOREIGN KEY (disciplina_id) REFERENCES disciplinas(codigo) 
);

INSERT INTO cursos(nome) VALUES ('Sistemas de Informação');
INSERT INTO cursos(nome) VALUES ('Ciencia da Computação');

INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201701, 'Benedito José', 'Sistemas de Informação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201702, 'Claudio Magalhaes', 'Sistemas de Informação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201703, 'Diana Jacinto', 'Sistemas de Informação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201704, 'Duarte Pereira', 'Ciencia da Computação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201705, 'Pereira Barbosa', 'Ciencia da Computação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201706, 'Joaquim Mamona', 'Sistemas de Informação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201707, 'Pangolin Gilberto', 'Ciencia da Computação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201708, 'Mario Ribeiro', 'Sistemas de Informação');
INSERT INTO alunos(nro_matric, nome, curso_id) VALUES (201709, 'Marcos Santos', 'Ciencia da Computação');

INSERT INTO grades(ano, curso_id) VALUES (2017, 'Sistemas de Informação');
INSERT INTO grades(ano, curso_id) VALUES (2017, 'Ciencia da Computação');

INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('COM110', 'Fundamentos de Programação', 80);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('COM111', 'Estrutura de Dados 1', 96);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('MAT001', 'Calculo 1', 96);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('SIN130', 'Fundamentos de Computação', 64);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('COM312', 'Informática de Sociedade', 64);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('MAT011', 'GA', 64);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('CIC270', 'Computação Gráfica', 48);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('CIC271', 'Processamento de Img', 64);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('SIN414', 'Auditoria em SI', 48);
INSERT INTO disciplinas(codigo, nome, carga_horaria) VALUES ('SIN210', 'Governança em TI', 64);

INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'COM110');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'COM111');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'SIN130');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'COM312');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'SIN414');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Sistemas de Informação', 'SIN210');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'COM110');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'COM111');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'MAT001');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'COM312');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'MAT011');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'CIC270');
INSERT INTO grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) VALUES (2017, 'Ciencia da Computação', 'CIC271');

INSERT INTO historicos(nro_matric, semestre, ano) VALUES (201701, 1, 2017);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (1, 'COM110', 7, 'APROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (1, 'MAT001', 2.5, 'REPROVADO', false);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (1, 'COM111', 4.7, 'REPROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (1, 'SIN130', 9, 'APROVADO', true);

INSERT INTO historicos(nro_matric, semestre, ano) VALUES (201704, 2, 2018);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (2, 'COM111', 9, 'APROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (2, 'COM312', 4, 'REPROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (2, 'MAT011', 4.5, 'REPROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (2, 'CIC270', 3.2, 'REPROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (2, 'SIN414', 6.5, 'APROVADO', false);

INSERT INTO historicos(nro_matric, semestre, ano) VALUES (201702, 1, 2018);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (3, 'COM110', 6.8, 'APROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (3, 'MAT001', 9, 'APROVADO', false);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (3, 'SIN130', 4.3, 'REPROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (3, 'COM312', 6.6, 'APROVADO', true);
INSERT INTO historico_disciplina(historico_id, disciplina_id, nota_disciplina, status, obrigatorio) VALUES (3, 'CIC270', 4, 'REPROVADO', false);

-- Para deletar

-- delete from historicos;
-- delete from historico_disciplina;
-- delete from grades;
-- delete from grade_disciplina;
-- delete from disciplinas;
-- delete from alunos;
-- delete from cursos;
