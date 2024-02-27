import uuid
from datetime import datetime

#generar un id unico
def gen_id() -> str:
  return str(uuid.uuid1()).split('-')[0]

def sort_by_date(list_of_dict):
    sorted_dates = sorted(list_of_dict, key=lambda x: datetime.strptime(list(x.keys())[0], '%Y-%m-%d'))
    return sorted_dates
