# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, SmallInteger, String, Table, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Course(Base):
    __tablename__ = 'courses'

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))

    students = relationship('Student')
    grid = relationship('Grid', uselist=False, cascade="all, delete", passive_deletes=True)
    def __repr__(self):
        return f'Course(name={self.name}, students={self.students}, grid={self.grid})'


class Grid(Course):
    __tablename__ = 'grids'

    course_id = Column(ForeignKey('courses.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    year = Column(SmallInteger, nullable=False)
    course_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))

    disciplines = relationship('Discipline', secondary='grid_discipline') 
    def __repr__(self):
        return f'Grid(year={self.year}, course_id={self.course_id}, disciplines={self.disciplines})'


class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(UUID, primary_key=True)
    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    workload = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    deleted_at = Column(DateTime)

    def __repr__(self):
        return f'Discipline(code={self.code}, name={self.name}, workload={self.workload})'


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    deleted_at = Column(DateTime)

    def __repr__(self):
        return f'User(name={self.name}, email={self.email})'


class Student(Base):
    __tablename__ = 'students'

    id = Column(UUID, primary_key=True)
    matriculation = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    course_id = Column(ForeignKey('courses.id', ondelete='SET NULL', onupdate='CASCADE'))

    def __repr__(self):
        return f'Student(matriculation={self.matriculation}, name={self.name})'


t_grid_discipline = Table(
    'grid_discipline', metadata,
    Column('grid_id', ForeignKey('grids.course_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('discipline_id', ForeignKey('disciplines.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)


class Historic(Base):
    __tablename__ = 'historics'
    __table_args__ = (
        CheckConstraint('(semester = 1) OR (semester = 2)'),
    )

    id = Column(UUID, primary_key=True)
    semester = Column(SmallInteger, nullable=False)
    year = Column(SmallInteger, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    student_id = Column(ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))

    student = relationship('Student', uselist=False)
    disciplines = relationship('HistoricDiscipline')
    def __repr__(self):
        return f'Historic(semester={self.semester}, year={self.year}, student={self.student}, disciplines={self.disciplines})'

class HistoricDiscipline(Base):
    __tablename__ = 'historic_discipline'
    __table_args__ = (
        CheckConstraint("((status)::text = 'APROVADO'::text) OR ((status)::text = 'REPROVADO'::text)"),
    )

    historic_id = Column(ForeignKey('historics.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    discipline_id = Column(ForeignKey('disciplines.id'), primary_key=True, nullable=False)
    note_discipline = Column(Float(53), nullable=False)
    status = Column(String(10), nullable=False)
    required = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))

    discipline = relationship('Discipline')
    def __repr__(self):
        return f'HistoricDiscipline(historic_id={self.historic_id}, discipline_id={self.discipline_id}, note_discipline={self.note_discipline}, status={self.status}, required={self.required})'