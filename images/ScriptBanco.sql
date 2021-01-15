CREATE TABLE curso (
	nome varchar(30) primary key
);

CREATE TABLE aluno (
	nro_matric int primary key,
	nome varchar(50),
	curso_id varchar(30),
		foreign key (curso_id) references curso(nome)
);

CREATE TABLE grade (
	ano smallint,
	curso_id varchar(30) unique,
	primary key(curso_id, ano),
		foreign key (curso_id) references curso(nome) on delete cascade 
);

CREATE TABLE disciplina(
	codigo varchar(10) primary key,
	nome varchar(50),
	carga_horaria smallint
);

CREATE TABLE grade_disciplina(
	grade_id_ano smallint,
	grade_id_curso varchar(30),  
	disciplina_id varchar(10),
	primary key(grade_id_curso, grade_id_ano, disciplina_id),
		foreign key(grade_id_curso, grade_id_ano) references grade(curso_id, ano),
		foreign key(disciplina_id) references disciplina(codigo)
);

insert into curso(nome) values ('Sistemas de Informação');
insert into curso(nome) values ('Ciencia da Computação');

insert into aluno(nro_matric, nome, curso_id) values (201701, 'Ygor Salles', 'Sistemas de Informação');
insert into aluno(nro_matric, nome, curso_id) values (201702, 'Caio Ribeiro', 'Sistemas de Informação');
insert into aluno(nro_matric, nome, curso_id) values (201703, 'Leticia Alves', 'Ciencia da Computação');
insert into aluno(nro_matric, nome, curso_id) values (201704, 'Fabio Antonio', 'Sistemas de Informação');

insert into grade(ano, curso_id) values ('Sistemas de Informação', 2017);
insert into grade(ano, curso_id) values ('Ciencia da Computação', 2017);

insert into disciplina(codigo, nome, carga_horaria) values ('COM110', 'Fundamentos de Programação', 80);
insert into disciplina(codigo, nome, carga_horaria) values ('COM111', 'Estrutura de Dados 1', 96);
insert into disciplina(codigo, nome, carga_horaria) values ('MAT001', 'Calculo 1', 96);
insert into disciplina(codigo, nome, carga_horaria) values ('SIN110', 'Auditoria SI', 46);

insert into grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) values ('Sistemas de Informação', 2017, 'COM110');
insert into grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) values ('Sistemas de Informação', 2017, 'COM111');
insert into grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) values ('Sistemas de Informação', 2017, 'SIN110');
insert into grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) values ('Ciencia da Computação', 2017, 'COM110');
insert into grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) values ('Ciencia da Computação', 2017, 'COM111');
insert into grade_disciplina(grade_id_ano, grade_id_curso, disciplina_id) values ('Ciencia da Computação', 2017, 'MAT001');
