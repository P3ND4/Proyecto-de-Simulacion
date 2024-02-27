from sim import sim_inscriptions, sim_reclam
import datetime

def start(start_date, months: int):
  #aqui guardaremos todos los eventos
  events = []
  
  #agregamos las inscripciones de los clientes
  for i in range(months):
    for client in sim_inscriptions(start_date + datetime.timedelta(i * 30)):
      events.append({client.inscrption_date: f'Cliente {client.id} se ha inscrito en la empresa de seguros por {client.months} meses'})

      #agregar las reclamaciones generadas por cada cliente
      sim_reclam(client)
      
      for reclam in client.reclams:
        events.append({reclam[0]: f'Cliente {client.id} ha generado una reclamacion con un monto de {reclam[1]} dolares'})
  
  