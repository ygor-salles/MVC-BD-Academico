from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

class DAOCrud():
    def getSession(Base):
        engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/academico', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        return session

    def insere(sessao, obj):
        sessao.add(obj)

    def deleta(session, obj):
        session.delete(obj)

    def consulta(session, objId):
        obj = session.query(objId).filter(objId == id).first()
        return obj
    