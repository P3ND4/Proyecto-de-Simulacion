from date import Date

class Client:
  def __init__(self, name: str, inscription_date: Date, months: int, cuote: float):
    self.__name = name #nombre del cliente
    self.__inscription_date = inscription_date #fecha en que se iscribio
    self.__months = months #tiempo en meses que va a estar el cliente en la aseguradora
    self.__cuote = cuote #cuota mensual que paga el cliente a la aseguradora
    self.__total_mount = 0 #monto total de las reclamaciones 
    
  #generacion de una reclamacion del cliente  
  def gen_reclam(self, date: Date, mount: float):
    self.__last_reclam = date
    self.__total_mount += mount
    
  @property
  def name(sef): return sef.__name
  @property
  def inscription_date(self): return self.__inscription_date
  @property
  def months(self): return self.__months
  @property
  def cuote(self): return self.__cuote
    