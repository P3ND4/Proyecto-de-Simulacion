#dependencias
from sim import sim_inscriptions, sim_reclams
import datetime
import time

#metodos auxiliares
from utils import sort_by_date, compare_dates

#simulacion del funcionamiento de la empresa
def start(start_date, months: int):
  #aqui guardaremos todos los eventos
  events = []
  
  #agregamos las inscripciones de los clientes
  for i in range(months):
    for client in sim_inscriptions(start_date + datetime.timedelta(days = i * 30)):
      events.append({str(client.inscription_date): f'Cliente {client.id} se ha inscrito en la empresa de seguros por {client.months} meses'})

      #agregar las reclamaciones generadas por cada cliente
      sim_reclams(client)
      
      for reclam in client.reclams:
        events.append({reclam[0]: f'Cliente {client.id} ha generado una reclamacion con un monto de {reclam[1]} dolares'})
  
  #imprimir la simulacion siguiendo un orden cronologico
  result = sort_by_date(events)
  contador = 1
  
  for element in result:
    if compare_dates(list(element.keys())[0], str(start_date + datetime.timedelta(days = months * 30))):
      break
    
    print(f'{contador}-{element}')
    contador += 1
    time.sleep(1)

#start(datetime.date(2024, 2, 26), 5)
  