from workout_api.contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example = 'Scale', max_length = 10)]