#!/usr/bin/python


import time
import sys

import RPi.GPIO as GPIO



import MySQLdb






time.sleep(15)


condicion=4



#print "Temp: "+temp
#print "Hum: "+hum

pin_tmax=6
pin_tmin=13
pin_hmax=19
pin_hmin=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_tmax, GPIO.OUT)
GPIO.setup(pin_tmin, GPIO.OUT)
GPIO.setup(pin_hmax, GPIO.OUT)
GPIO.setup(pin_hmin, GPIO.OUT)


DB_HOST='localhost'
DB_USER='root'
DB_PASS='andres'
DB_NAME='monitoreo'


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





while(1):

   file = open('/var/www/web/monitor/application/third_party/scripts/temp2', 'r')
   file2 = open('/var/www/web/monitor/application/third_party/scripts/hum2', 'r')
   temp = file.read()
   hum = file2.read()
   file.close()
   file2.close()
   if ((temp!="") and (hum!="")):
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
            GPIO.output(pin_tmax, False)
            GPIO.output(pin_tmin, True)
            GPIO.output(pin_hmax, False)
            GPIO.output(pin_hmin, True)
         elif((hum>=h_min) and (hum<=h_max)):
            reporte="temperatura por debajo, humedad ok"
            reporte="TEMPERATURA = "+temp+" por debajo del limite configurado de "+str(t_min)+". HUMEDAD = "+hum+" dentro del limite configurado de "+str(h_min)+" y "+str(h_max)+"."
            condicion=1
            GPIO.output(pin_tmax, False)
            GPIO.output(pin_tmin, True)
            GPIO.output(pin_hmax, False)
            GPIO.output(pin_hmin, False)
         elif(hum>h_max):
            reporte="temperatura por debajo, humedad por encima"
            reporte="TEMPERATURA = "+temp+" por debajo del limite configurado de "+str(t_min)+". HUMEDAD = "+hum+" por encima del limite configurado de "+str(h_max)+"."
            condicion=2
            GPIO.output(pin_tmax, False)
            GPIO.output(pin_tmin, True)
            GPIO.output(pin_hmax, True)
            GPIO.output(pin_hmin, False)
      elif((temp>=t_min) and (temp<=t_max)):
         if(hum<h_min):
            reporte="temperatura ok, humedad por debajo"
            reporte="TEMPERATURA = "+temp+" dentro del limite configurado de "+str(t_min)+" y "+str(t_max)+". HUMEDAD = "+hum+" por debajo del limite configurado de "+str(h_min)+"."
            condicion=3
            GPIO.output(pin_tmax, False)
            GPIO.output(pin_tmin, False)
            GPIO.output(pin_hmax, False)
            GPIO.output(pin_hmin, True)
         elif((hum>=h_min) and (hum<=h_max)):
            reporte="temperatura ok, humedad ok"
            reporte="TEMPERATURA = "+temp+" dentro del limite configurado de "+str(t_min)+" y "+str(t_max)+". HUMEDAD = "+hum+" dentro del limite configurado de "+str(h_min)+" y "+str(h_max)+"."
            condicion=4
            GPIO.output(pin_tmax, False)
            GPIO.output(pin_tmin, False)
            GPIO.output(pin_hmax, False)
            GPIO.output(pin_hmin, False)
         elif(hum>h_max):
            reporte="temperatura ok, humedad por encima"
            reporte="TEMPERATURA = "+temp+" dentro del limite configurado de "+str(t_min)+" y "+str(t_max)+". HUMEDAD = "+hum+" por encima del limite configurado de "+str(h_max)+"."
            condicion=5
            GPIO.output(pin_tmax, False)
            GPIO.output(pin_tmin, False)
            GPIO.output(pin_hmax, True)
            GPIO.output(pin_hmin, False)
      elif (temp>t_max):
         if(hum<h_min):
            reporte="temperatura por encima, humedad por debajo"
            reporte="TEMPERATURA = "+temp+" por encima del limite configurado de "+str(t_max)+". HUMEDAD = "+hum+" por debajo del limite configurado de "+str(h_min)+"."
            condicion=6
            GPIO.output(pin_tmax, True)
            GPIO.output(pin_tmin, False)
            GPIO.output(pin_hmax, False)
            GPIO.output(pin_hmin, True)
         elif((hum>=h_min) and (hum<=h_max)):
            reporte="temperatura por encima, humedad ok"
            reporte="TEMPERATURA = "+temp+" por encima del limite configurado de "+str(t_max)+". HUMEDAD = "+hum+" dentro del limite configurado de "+str(h_min)+" y "+str(h_max)+"."
            condicion=7
            GPIO.output(pin_tmax, True)
            GPIO.output(pin_tmin, False)
            GPIO.output(pin_hmax, False)
            GPIO.output(pin_hmin, False)
         elif(hum>h_max):
            reporte="temperatura por encima, humedad por encima"
            reporte="TEMPERATURA = "+temp+" por encima del limite configurado de "+str(t_max)+". HUMEDAD = "+hum+" por encima del limite configurado de "+str(h_max)+"."
            condicion=8
            GPIO.output(pin_tmax, True)
            GPIO.output(pin_tmin, False)
            GPIO.output(pin_hmax, True)
            GPIO.output(pin_hmin, False)

      
