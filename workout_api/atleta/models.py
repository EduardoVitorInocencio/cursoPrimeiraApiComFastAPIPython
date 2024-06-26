from sqlalchemy import DateTime,Integer, String, Float, ForeignKey
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class AtletaModel():
    __tablename__ = 'atletas'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key = True) #Chave Primária
    nome: Mapped[str] = mapped_column(String(50), nullable=False) 
    cpf: Mapped[str] = mapped_column(String(11), unique= True,nullable=False) 
    idade: Mapped[int] = mapped_column(Integer, nullable=False) 
    peso: Mapped[float] = mapped_column(Float, nullable=False) 
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    nome: Mapped[str] = mapped_column(String(10), nullable=False)
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centrp_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'))