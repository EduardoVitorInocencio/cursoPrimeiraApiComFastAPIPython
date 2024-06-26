from sqlalchemy import Integer, String, ForeignKey
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key = True) #Chave Primária
    nome: Mapped[str] = mapped_column(String(10), unique= True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
    
    