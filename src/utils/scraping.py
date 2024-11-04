import pandas as pd
import requests
from bs4 import BeautifulSoup


def  scrape_table(page: str, year: int, filter_option: str = '') -> pd.DataFrame:
    """
    Extrai uma tabela de uma página específica da Embrapa e retorna como um DataFrame.

    Parâmetros:
    ----------
    page : str
        Número da página para consulta.
    year : int
        Ano a ser consultado.
    filter_option : str
        Filtro opcional para consulta.

    Retorno:
    -------
    pd.DataFrame
        DataFrame com os dados da tabela extraída.

    Descrição:
    ----------
    Faz uma requisição HTTP para uma página da Embrapa, usa BeautifulSoup para analisar o HTML e pandas para extrair a tabela
    (classe 'tb_base tb_dados') em formato DataFrame.
    """
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao={page}&subopcao={filter_option}'
    return get_empraba_table(url)


def scrape_table_base_url(page: str) -> pd.DataFrame:
    """
    Extrai uma tabela de uma página específica da Embrapa e retorna como um DataFrame sem filtros adicionais.

    Parâmetros:
    ----------
    page : str
        Número da página para consulta.

    Retorno:
    -------
    pd.DataFrame
        DataFrame com os dados da tabela extraída.

    Descrição:
    ----------
    Faz uma requisição HTTP para uma página da Embrapa, usa BeautifulSoup para analisar o HTML e pandas para extrair a tabela
    (classe 'tb_base tb_dados') em formato DataFrame.
    """
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={page}'
    return get_empraba_table(url)


def get_empraba_table(url) -> pd.DataFrame:
    """
        Realiza uma requisição HTTP para uma URL específica e extrai uma tabela da página retornada.

        Parâmetros:
        ----------
        url : str
            URL da página da Embrapa que contém a tabela a ser extraída.

        Retorno:
        -------
        pd.DataFrame
            DataFrame com os dados da tabela extraída. A tabela deve estar identificada pela classe 'tb_base tb_dados'.

        Descrição:
        ----------
        A função faz uma requisição HTTP usando a URL fornecida, utiliza BeautifulSoup para processar o conteúdo HTML da página
        e localiza uma tabela com a classe 'tb_base tb_dados'. Caso encontrada, a tabela é convertida em um DataFrame com pandas.
        """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find(class_='tb_base tb_dados')

        if table:
            df = pd.read_html(str(table))[0]
            return df
        else:
            raise ValueError("Tabela não encontrada na página.")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na requisição HTTP: {e}")
    except ValueError as e:
        raise Exception(f"Erro ao processar a tabela: {e}")