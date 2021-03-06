#!/usr/bin/python


import time
import sys





import MySQLdb


from datetime import datetime




time.sleep(14)


condicion=4

periodo_sin_alarma=1800   #En segundos

alertar=1


#print "Temp: "+temp
#print "Hum: "+hum




DB_HOST='localhost'
DB_USER='root'
DB_PASS='andres'
DB_NAME='heladera'


def run_query(query=''):
   datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
   conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
   cursor = conn.cursor()         # Crear un cursor 
   cursor.execute(query)          # Ejecutar una consulta
   if query.upper().startswith('SELECT'):
      data = cursor.fetchall()   # Traer los resultados de un select 
   else:
      conn.commit()              # Hacer efectiva la escritura de datos 
      data = None 
   
   cursor.close()                 # Cerrar el cursor 
   conn.close()                   # Cerrar la conexion 

   return data


def enviar_alertas(reporte,condicion):
   query="INSERT INTO alertas (mensaje,condicion) VALUES ('%s','%s')" %(reporte,condicion)
   #print query
   run_query(query)
   


while(1):

   file = open('/var/www/web/monitor/application/third_party/scripts/temp2', 'r')
   
   temp = file.read()
   file.close()
   if ((temp!="") ):
   #if hum is not None and temp is not None:
      query="SELECT * from configuracion where 1"
      datos=run_query(query)

      t_min=datos[0][1]
      t_max=datos[0][2]
      h_min=datos[0][3]
      h_max=datos[0][4]

      if (temp<t_min):
         if(hum<h_min):
            reporte="temperatura y humedad por debajo"
            reporte="TEMPERATURA = "+temp+" por debajo del limite configurado de "+str(t_min)+". HUMEDAD = "+hum+" por debajo del limite configurado de "+str(h_min)+"."
            condicion=0

         elif((hum>=h_min) and (hum<=h_max)):
            reporte="temperatura por debajo, humedad ok"
            reporte="TEMPERATURA = "+temp+" por debajo del limite configurado de "+str(t_min)+". HUMEDAD = "+hum+" dentro del limite configurado de "+str(h_min)+" y "+str(h_max)+"."
            condicion=1

         elif(hum>h_max):
            reporte="temperatura por debajo, humedad por encima"
            reporte="TEMPERATURA = "+temp+" por debajo del limite configurado de "+str(t_min)+". HUMEDAD = "+hum+" por encima del limite configurado de "+str(h_max)+"."
            condicion=2

      elif((temp>=t_min) and (temp<=t_max)):
         if(hum<h_min):
            reporte="temperatura ok, humedad por debajo"
            reporte="TEMPERATURA = "+temp+" dentro del limite configurado de "+str(t_min)+" y "+str(t_max)+". HUMEDAD = "+hum+" por debajo del limite configurado de "+str(h_min)+"."
            condicion=3

         elif((hum>=h_min) and (hum<=h_max)):
            reporte="temperatura ok, humedad ok"
            reporte="TEMPERATURA = "+temp+" dentro del limite configurado de "+str(t_min)+" y "+str(t_max)+". HUMEDAD = "+hum+" dentro del limite configurado de "+str(h_min)+" y "+str(h_max)+"."
            condicion=4

         elif(hum>h_max):
            reporte="temperatura ok, humedad por encima"
            reporte="TEMPERATURA = "+temp+" dentro del limite configurado de "+str(t_min)+" y "+str(t_max)+". HUMEDAD = "+hum+" por encima del limite configurado de "+str(h_max)+"."
            condicion=5

      elif (temp>t_max):
         if(hum<h_min):
            reporte="temperatura por encima, humedad por debajo"
            reporte="TEMPERATURA = "+temp+" por encima del limite configurado de "+str(t_max)+". HUMEDAD = "+hum+" por debajo del limite configurado de "+str(h_min)+"."
            condicion=6

         elif((hum>=h_min) and (hum<=h_max)):
            reporte="temperatura por encima, humedad ok"
            reporte="TEMPERATURA = "+temp+" por encima del limite configurado de "+str(t_max)+". HUMEDAD = "+hum+" dentro del limite configurado de "+str(h_min)+" y "+str(h_max)+"."
            condicion=7

         elif(hum>h_max):
            reporte="temperatura por encima, humedad por encima"
            reporte="TEMPERATURA = "+temp+" por encima del limite configurado de "+str(t_max)+". HUMEDAD = "+hum+" por encima del limite configurado de "+str(h_max)+"."
            condicion=8


      if(condicion!=4):
         query="SELECT MAX(id) FROM alertas WHERE ocultar=0"
         n=run_query(query)
         n=n[0][0]
         if n==None:
            if alertar==1:
               query="INSERT INTO datos (temperatura, humedad) VALUES ('%s','%s')" %(temp,hum)
               run_query(query)
               enviar_alertas(reporte,condicion)
               alertar=0
         else:
            query="SELECT cuando,condicion FROM alertas WHERE id="+str(n)
            #print query
            resultado=run_query(query)
            #print resultado
            fecha=resultado[0][0]
            ultima_condicion=resultado[0][1]
            #print fecha
            #print ultima_condicion
            ahora=datetime.now()
            delta = ahora - fecha
            #print delta
            diferencia=delta.total_seconds()

            if((ultima_condicion!=condicion) or (diferencia>=periodo_sin_alarma)):
               query="INSERT INTO datos (temperatura, humedad) VALUES ('%s','%s')" %(temp,hum)
               run_query(query)
               enviar_alertas(reporte,condicion)

