class Date:
  def __init__(self, day: int, month: int, year: int):
    self.__day = day
    self.__month = month
    self.__year = year
  
  #imprimir Date en consola  
  def __str__(self) -> str:
    return f'{self.__day}/{self.__month}/{self.__year}'
  
  @property
  def day(self): return self.__day
  @property
  def month(self): return self.__month
  @property
  def year(self): return self.__year