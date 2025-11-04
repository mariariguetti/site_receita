from sqlalchemy import Column, DateTime, func, ForeignKey, Integer, String, Delete, create_engine
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/receita')

local_secao = sessionmaker(bind=engine)
Base = declarative_base()


class Ingredientes(Base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    unidade_base = Column(String(4), nullable=False)

    def __repr__(self):
        return f'<Ingredientes(nome={self.nome}, unidade_base={self.unidade_base})>'

class Receita(Base):
    __tablename__ = 'receita'
    id = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(String(150), nullable=False)
    tempo_preparo = Column(Integer, nullable=False)
    dificuldade = Column(String(50), nullable=False)
    rendimento = Column(Integer, nullable=False)
    custo = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<Receita(nome={self.nome}, descricao={self.descricao}, tempo_preparo={self.tempo_preparo}, dificuldade={self.dificuldade}, rendimento={self.rendimento}, custo={self.custo})>'


