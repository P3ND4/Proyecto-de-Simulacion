#dependencias
import uuid
from datetime import datetime

#generar un id unico
def gen_id() -> str:
  return str(uuid.uuid1()).split('-')[0] + str(uuid.uuid1()).split('-')[1]

def sort_by_date(list_of_dict):
    sorted_dates = sorted(list_of_dict, key=lambda x: datetime.strptime(list(x.keys())[0], '%Y-%m-%d'))
    return sorted_dates

#comparar 2 fechas como strings
def compare_dates(date1: str, date2: str) -> bool:
  #valor de la fecha 1 
  split_date1 = date1.split('-')
  value1 = int(split_date1[0] + split_date1[1] + split_date1[2])
  
  #valor de la fecha 2
  split_date2 = date2.split('-')
  value2 = int(split_date2[0] + split_date2[1] + split_date2[2])
  
  return value1 > value2