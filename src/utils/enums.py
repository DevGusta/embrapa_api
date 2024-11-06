from enum import Enum

class ProcessamentoFilterOption(str, Enum):
    PROCESSAMENTO_VINIFERAS = 'subopt_01'
    PROCESSAMENTO_AMERICANAS_HIBRIDAS = 'subopt_02'
    PROCESSAMENTO_UVAS_MESA = 'subopt_03'
    PROCESSAMENTO_SEM_CLASSIFICACAO = 'subopt_04'

class ImportacaoFilterOption(str, Enum):
    IMPORTACAO_VINHO_MESA = 'subopt_01'
    IMPORTACAO_ESPUMANTE = 'subopt_02'
    IMPORTACAO_UVAS_FRESCAS = 'subopt_03'
    IMPORTACAO_UVAS_PASSAS = 'subopt_04'
    IMPORTACAO_SUCO_UVA = 'subopt_05'

class ExportacaoFilterOption(str, Enum):
    EXPORTACAO_VINHO_MESA = 'subopt_01'
    EXPORTACAO_ESPUMANTE = 'subopt_02'
    EXPORTACAO_UVAS_FRESCAS = 'subopt_03'
    EXPORTACAO_SUCO_UVA = 'subopt_04'