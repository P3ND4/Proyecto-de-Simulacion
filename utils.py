import uuid

#generar un id unico
def gen_id() -> str:
  return str(uuid.uuid1()).split('-')[0]