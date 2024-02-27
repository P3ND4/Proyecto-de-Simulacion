#dependencias
from client import Client
import random
from scipy.stats import poisson, gamma
import datetime 

#metodos auxiliares
from utils import gen_id

#un cliente genera una reclamacion
def sim_reclams(client: Client):
  param_poisson = 0.5 #tasa de reclamaciones por mes
  reclams = list(poisson.rvs(param_poisson, size = client.months)) #generar las reclamaciones por mes de cada cliente
  
  for i in range(len(reclams)):
    if reclams[i] == 0:
      continue
    
    mount = round(random.uniform(5000.0, 100000.0), 2)
    reclams_month = gen_dates_reclams(i, reclams[i], client)
    
    for date in reclams_month:
      client.add_reclam(date, mount)

#generar las fechas de las reclamaciones de un mes
def gen_dates_reclams(month: int, reclams: int, client: Client) -> list:
  result = []
  temp = 0
  
  for i in range(reclams):
    days_reclam = random.randint(temp, 30 )
    temp = days_reclam
    date_reclam = client.inscription_date + datetime.timedelta(days = month * 30) + datetime.timedelta(days = days_reclam)
    result.append(str(date_reclam))
    
  return result
    
#generar la cantidad de clientes que se inscriben por mes
def sim_inscriptions(date) -> list:
  result = []
  param_poisson = 1.7 #tasa de inscripciones por dia
  inscriptions = list(poisson.rvs(param_poisson, size = 30)) #generar las reclamaciones por mes de cada cliente
  
  for i in range(len(inscriptions)):  
    for j in range(inscriptions[i]):
      inscription_date = date + datetime.timedelta(i)
      client = Client(gen_id(), inscription_date, sim_month(), sim_cuote(), [])
      result.append(client)
    
  return result    

#generar la cuota mensual de un cliente
def sim_cuote() -> float:
  alpha = 1.2 #parametro de forma
  beta = 100.0 #parametro de escala
  result = round(list(gamma.rvs(alpha, scale = beta, size = 10))[0], 2)
  return  result if result > 50 else result + 50

def sim_month() -> int:
  alpha = 1 #parametro de forma
  beta = 2.0 #parametro de escala
  result = round(list(gamma.rvs(alpha, scale = beta, size = 10))[0], 1)
  result_frac = result - int(result)
  result = int(result) * 12 + int(result_frac*12)
  return result if result > 1 else 3