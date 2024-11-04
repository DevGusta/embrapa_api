from pydantic import BaseModel
from typing import List, Union, Optional, Any

class ProducaoData(BaseModel):
    Produto: str
    Quantidade_L: Optional[Union[str, int]]

class ProcessamentoData(BaseModel):
    Cultivar: str
    Quantidade_Kg: Optional[Union[str, int]]

class ComercializacaoData(BaseModel):
    Produto: str
    Quantidade_L: Optional[Union[str, int]]

class ImportacaoData(BaseModel):
    Produto: str
    Quantidade_L: Optional[Union[str, int]]

class ExportacaoData(BaseModel):
    Paises: str
    Quantidade_Kg: Optional[Union[str, int]]
    Valor_US: Optional[Union[str, int]]



class ResponseModel(BaseModel):
    status: str
    message: Union[str, None] = None
    data: Optional[Any] = None

# List[ProducaoData], List[ProcessamentoData], List[ComercializacaoData], List[ImportacaoData], List[ExportacaoData]