#!/usr/bin/python

import time
import MySQLdb
import os


#time.sleep(14)

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




while True:
	sensores=[]
	rootDir="/sys/bus/w1/devices/"
	for dirName, subdirList, FileList in os.walk(rootDir):
		#print("Directorio encontrado: %s" % dirName)
		for subcarpetas in subdirList:
			if(subcarpetas[0:2]=="28"):
				#print("\t%s" % subcarpetas)
				sensores.append(subcarpetas)
	#print sensores
	k=0
	for sensor in sensores:
		query="SELECT count(id) from sensores where n_serie='"+sensor+"'"
		n=run_query(query)
		n=n[0][0]
		#print n
		if n==0:
			query="INSERT INTO sensores (nombre,n_serie,conectado) values('heladera','"+sensor+"',1)"
			run_query(query)
			print "nuevo sensor agrgado"
		else:
			print "el sensor ya se encuentra en el sistema"
		
		tfile=open("/sys/bus/w1/devices/"+sensor+"/w1_slave")
		text=tfile.read()
		tfile.close()
		secondline=text.split("\n")[1]
		temperaturedata=secondline.split(" ")[9]
		temperature =float(temperaturedata[2:])
		temperature=temperature/1000
		print "sensor "+str(k)+": "+str(temperature)


	time.sleep(1)