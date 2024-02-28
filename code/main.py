#dependencias
from sim import sim_inscriptions, sim_reclams
import datetime
import time
import os

#metodos auxiliares
from utils import sort_by_date, compare_dates

#simulacion del funcionamiento de la empresa
def start(start_date, presp: float, months: int):
  events = [] #aqui guardaremos todos los eventos
  presp_com = presp #aqui guardaremos el presupuesto de la empresa
  cant_clients = 0 #aqui guardaremos la cantidad de clientes
  cant_reclams = 0 #aqui guardaremos la cantidad de reclamaciones
  
  #agregamos las inscripciones de los clientes
  for i in range(months):
    for client in sim_inscriptions(start_date + datetime.timedelta(days = i * 30)):
      cant_clients += 1
      events.append({str(client.inscription_date): f'Cliente {client.id} se ha inscrito en la empresa de seguros por {client.months} meses'})

      #agregar las reclamaciones generadas por cada cliente
      sim_reclams(client)
      
      for reclam in client.reclams:
        if compare_dates(reclam[0], str(start_date + datetime.timedelta(days = months * 30))):
          break
        
        presp_com -= reclam[1]
        cant_reclams += 1
        events.append({reclam[0]: f'Cliente {client.id} ha generado una reclamacion con un monto de {reclam[1]} dolares'})
        
      #agregar los pagos mensuales de cada cliente
      for i in range(1, client.months): 
        if compare_dates(str(client.inscription_date + datetime.timedelta(days = i * 30)), str(start_date + datetime.timedelta(days = months * 30))):
          break
        
        presp_com += client.cuote
        events.append({str(client.inscription_date + datetime.timedelta(days = i * 30)): f'Cliente {client.id} pago {client.cuote} dolares a la empresa como parte de su membresia'})
      
  #imprimir los resultados del experimento
  print(f'RESULTADOS GENERALES DURANTE {months} MESES:')
  print(f'presupuesto final: {round(presp_com, 2)} dolares => se generaron aproximadamente {round(presp_com / months, 2)} dolares por mes')
  print(f'total de clientes: {cant_clients} => se unieron aproximadamente {round(cant_clients / months, 2)} clientes por mes')
  print(f'total de reclamaciones: {cant_reclams} => se realizaron aproximadamente {round(cant_reclams / months, 2)} por mes')
  input(f'Pulse una tecla para ver los eventos ocurridos duante {months} meses')
  os.system('clear')
  
  #imprimir los resultados de la simulacion
  print(f'SIMULACION DEL COMPORTAMIENTO DE LA EMPRESA POR {months} MESES:')
  result = sort_by_date(events)
  contador = 1
  
  for element in result:
    if compare_dates(list(element.keys())[0], str(start_date + datetime.timedelta(days = months * 30))):
      break
    
    print(f'{contador}-{element}')
    contador += 1
    time.sleep(1)

start(datetime.date(2024, 2, 26), 100.0, 12)
  