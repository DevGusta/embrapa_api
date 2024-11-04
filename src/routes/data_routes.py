from fastapi import APIRouter,Path
from src.utils.scraping import scrape_table, scrape_table_base_url
import src.utils.pages_constants as pages_constants
from src.utils.enums import *
from src.models.response import ResponseModel
from src.models.user import User
import json
from src.auth.auth import get_current_user
from fastapi import Depends

router = APIRouter()


@router.get("/producao",
            tags=['Produção'],
            description='Produção de vinhos, sucos e derivados do Rio Grande do Sul',
            summary="Obter dados de produção",
            response_model=ResponseModel)
async def get_producao(current_user: User = Depends(get_current_user)):
    data = scrape_table_base_url(pages_constants.PRODUCAO)
    data = data.rename(columns={"Quantidade (L.)": "Quantidade_L"})
    json_data = json.loads(data.to_json(orient='records'))

    return {
        "status": "success",
        "data": json_data
    }

@router.get("/producao/{year}",
            tags= ['Produção'],
            description='Produção de vinhos, sucos e derivados do Rio Grande do Sul',
            summary="Obter dados de produção",
            response_model=ResponseModel)
async def get_producao(year: int = Path(..., ge=1970, le=2023), current_user: User = Depends(get_current_user)):
    data = scrape_table(pages_constants.PRODUCAO, year)
    data = data.rename(columns={"Quantidade (L.)": "Quantidade_L"})
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }


@router.get("/processamento/",
            tags=['Processamento'],
            description='Quantidade de uvas processadas no Rio Grande do Sul',
            summary="Obter dados de processamento",
            response_model=ResponseModel
            )
async def get_processamento(current_user: User = Depends(get_current_user)):
    data = scrape_table_base_url(pages_constants.PROCESSAMENTO)
    data = data.rename(columns={"Quantidade (Kg)": "Quantidade_Kg"})
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }

@router.get("/processamento/{year}",
            tags=['Processamento'],
            description='Quantidade de uvas processadas no Rio Grande do Sul',
            summary="Obter dados de processamento",
            response_model=ResponseModel)
async def get_processamento(year: int = Path(..., ge=1970, le=2023), current_user: User = Depends(get_current_user)):
    data = scrape_table(pages_constants.PROCESSAMENTO, year)
    data = data.rename(columns={"Quantidade (Kg)": "Quantidade_Kg"})
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }

@router.get("/processamento/{year}/{filter_option}",
            tags=['Processamento'],
            description='Quantidade de uvas processadas no Rio Grande do Sul',
            summary="Obter dados de processamento",
            response_model=ResponseModel)
async def get_processamento(year: int = Path(..., ge=1970, le=2023),
                            filter_option: ProcessamentoFilterOption = Path(...),
                            current_user: User = Depends(get_current_user)):
    data = scrape_table(pages_constants.PROCESSAMENTO, year, getattr(pages_constants, filter_option))
    data = data.rename(columns={"Quantidade (Kg)": "Quantidade_Kg"})
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }



@router.get("/comercializacao",
            tags=['Comercialização'],
            description='Comercialização de vinhos e derivados no Rio Grande do Sul',
            summary="Obter dados de comercialização",
            response_model=ResponseModel)
async def get_comercializacao(current_user: User = Depends(get_current_user)):
    data = scrape_table_base_url(pages_constants.COMERCIALIZACAO)
    data = data.rename(columns={"Quantidade (L.)": "Quantidade_L"})
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }

@router.get("/comercializacao/{year}",
            tags=['Comercialização'],
            description='Comercialização de vinhos e derivados no Rio Grande do Sul',
            summary="Obter dados de comercialização",
            response_model=ResponseModel)
async def get_comercializacao(year: int = Path(..., ge=1970, le=2023),
                              current_user: User = Depends(get_current_user)):
    data = scrape_table(pages_constants.COMERCIALIZACAO, year)
    data = data.rename(columns={"Quantidade (L.)": "Quantidade_L"})
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }


@router.get("/importacao",
            tags=['Importação'],
            description='Importação de derivados de uva',
            summary="Obter dados de importação",
            response_model=ResponseModel)
async def get_importacao(current_user: User = Depends(get_current_user)):
    data = scrape_table_base_url(pages_constants.PROCESSAMENTO)
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }

@router.get("/importacao/{year}",
            tags=['Importação'],
            description='Importação de derivados de uva',
            summary="Obter dados de importação",
            response_model=ResponseModel)
async def get_importacao(year: int = Path(..., ge=1970, le=2023)):
    data = scrape_table(pages_constants.PROCESSAMENTO, year)
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }
@router.get("/importacao/{year}/{filter_option}",
            tags=['Importação'],
            description='Importação de derivados de uva',
            summary="Obter dados de importação",
            response_model=ResponseModel)
async def get_importacao(year: int = Path(..., ge=1970, le=2023),
                         filter_option: ImportacaoFilterOption = Path(...),
                         current_user: User = Depends(get_current_user)):
    data = scrape_table(pages_constants.PROCESSAMENTO, year, filter_option)
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }

@router.get("/exportacao",
            tags=['Exportação'],
            description='Exportação de derivados de uva',
            summary="Obter dados de Exportação",
            response_model=ResponseModel)
async def get_exportacao(current_user: User = Depends(get_current_user)):
    data = scrape_table_base_url(pages_constants.PROCESSAMENTO)
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }

@router.get("/exportacao/{year}",
            tags=['Exportação'],
            description='Exportação de derivados de uva',
            summary="Obter dados de Exportação",
            response_model=ResponseModel)
async def get_exportacao(year: int = Path(..., ge=1970, le=2023),
                         current_user: User = Depends(get_current_user)):
    data = scrape_table(pages_constants.PROCESSAMENTO, year)
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }
@router.get("/exportacao/{year}/{filter_option}",
            tags=['Exportação'],
            description='Exportação de derivados de uva',
            summary="Obter dados de Exportação",
            response_model=ResponseModel)
async def get_exportacao(year: int = Path(..., ge=1970, le=2023),
                         filter_option: ExportacaoFilterOption = Path(...),
                         current_user: User = Depends(get_current_user)):
    data = scrape_table(pages_constants.PROCESSAMENTO, year, filter_option)
    json_data = json.loads(data.to_json(orient='records'))
    return {
        "status": "success",
        "data": json_data
    }



