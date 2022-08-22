from datetime import date
from datetime import datetime

def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def Formata_float_moeda(valor: float) -> float:
    return f'R$ {valor:,.2f}'
