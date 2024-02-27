class Client:
  #cosas que puede hacer un cliente
  def __init__(self, id: str, inscription_date, months: int, cuote: float, reclams: list):
    self.__id = id #nombre del cliente
    self.__inscription_date = inscription_date #fecha en que se iscribio
    self.__months = months #tiempo en meses que va a estar el cliente en la aseguradora
    self.__cuote = cuote #cuota mensual que paga a la empresa el cliente
    self.__reclams = reclams #reclamaciones generadas por el cliente
  
  def __repr__(self):
    return '{ ' + f'id: {self.__id}, inscription_date: {self.__inscription_date}, months: {self.__months}, cuote: {self.__cuote}, reclams: {self.__reclams}' + '}'
  
  #agregar una reclamacion a la lista de reclamaciones 
  def add_reclam(self, date, mount):
    self.__reclams.append((date, mount))
    
  @property
  def id(sef) -> int: return sef.__id
  @property
  def inscription_date(self): return self.__inscription_date
  @property
  def months(self) -> int: return self.__months
  @property
  def reclams(self) -> list: return self.__reclams
  @property
  def cuote(self) -> float: return self.__cuote
    