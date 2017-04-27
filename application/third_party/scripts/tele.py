#!/usr/bin/python


import MySQLdb
import telepot
import time
import netifaces




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


def handle(msg):
   chat_id=msg['chat']['id']
   msg_rec=msg['text']
   
   query="SELECT COUNT(id) from usuarios where chat_id="+str(chat_id)+" and habilitado=1"
   n=run_query(query)
   n=n[0][0]
   #print n
   if n==0:
      query="SELECT COUNT(id) from usuarios where chat_id="+str(chat_id)
      n=run_query(query)
      n=n[0][0]
      if n==0:
         if(msg_rec.lower()=="alta "+NUMERO_SERIE):
            query="INSERT into usuarios (chat_id,habilitado) values ('"+str(chat_id)+"',1)"
            resp=run_query(query)
            bot.sendMessage(chat_id,"CODIGO VALIDO"+chr(10)+chr(13)+"Usuario dado de alta")
         else:
            bot.sendMessage(chat_id,"CODIGO INVALIDO"+chr(10)+chr(13)+"Vuelva a intentar")
      else:
         if(msg_rec.lower()=="alta "+NUMERO_SERIE):
            query="UPDATE usuarios set habilitado=1 where chat_id="+str(chat_id)
            resp=run_query(query)
            bot.sendMessage(chat_id,"CODIGO VALIDO"+chr(10)+chr(13)+"Usuario dado de alta")
         else:
            bot.sendMessage(chat_id,"CODIGO INVALIDO"+chr(10)+chr(13)+"Vuelva a intentar")
   else:      
      if msg_rec.lower()=="ultimo":
         #bot.sendMessage(chat_id,"Hola")
         query="SELECT max(id) FROM datos"
         n=run_query(query)
         n=n[0][0]
         #print n
         query="SELECT * FROM datos where id='%s'"%n
         todos=run_query(query)
         #print todos
         temp=todos[0][1]
         hum=todos[0][2]
         fecha=todos[0][4]
         #print fecha
         #formato="a las %H:%M:%S del dia %d/%m/%Y"
         formato="%d/%m/%Y %H:%M:%S"
         fecha=fecha.strftime(formato)
         #print type(fecha)
         #msg="La ultima temperatura y humedad registrados fueron de %s grados y %s%% %s" %(temp,hum,fecha)
         #msg=(50*"-")+chr(10)+chr(13)+"| TEMPERATURA "+19*" "+str(temp)+" | "+chr(10)+chr(13)+50*"-"+chr(10)+chr(13)+"| HUMEDAD  "+28*" "+str(hum)+" | "+chr(10)+chr(13)+50*"-"+chr(10)+chr(13)+"| FECHA  "+str(fecha)+" | "+chr(10)+chr(13)+50*"-"
         #msg="<b>HOLA</b>"
         #print(len("| TEMPERATURA "+str(temp)))
         msg="TEMPERATURA = "+str(temp)+chr(10)+chr(13)+"HUMEDAD = "+str(hum)+chr(10)+chr(13)+"FECHA = "+str(fecha)
         bot.sendMessage(chat_id,msg)
         #print(msg)
      elif(msg_rec.lower()=="alta "+NUMERO_SERIE):
         bot.sendMessage(chat_id,"El usuario ya se encontraba de alta")
      elif(msg_rec.lower()=="baja"):
         query="UPDATE usuarios set habilitado=0 where chat_id="+str(chat_id)
         resp=run_query(query)
         bot.sendMessage(chat_id,"Usuario dado de baja"+chr(10)+chr(13)+"puede volver a darse de alta en el futuro")
      elif(msg_rec.lower()=="actual"):
         file = open('/var/www/web/monitor/application/third_party/scripts/temp2', 'r')
         file2 = open('/var/www/web/monitor/application/third_party/scripts/hum2', 'r')
         temp = file.read()
         hum = file2.read()
         file.close()
         file2.close()
         msg="TEMPERATURA = "+str(temp)+chr(10)+chr(13)+"HUMEDAD = "+str(hum)
         bot.sendMessage(chat_id,msg)
      elif(msg_rec.lower()=="umbrales"):
         query="SELECT MAX(id) from configuracion WHERE 1"
         n=run_query(query)
         n=n[0][0]
         #print n
         query="SELECT * FROM configuracion WHERE id='%s'"%n
         umbrales=run_query(query)
         #print umbrales
         Tmin=umbrales[0][1]
         Tmax=umbrales[0][2]
         Hmin=umbrales[0][3]
         Hmax=umbrales[0][4]
         #print Tmax
         msg="UMBRALES CONFIGURADOS:"+chr(10)+chr(13)+"Temp. min. = "+str(Tmin)
         msg=msg+chr(10)+chr(13)+"Temp. max. = "+str(Tmax)
         msg=msg+chr(10)+chr(13)+"Hum. min. = "+str(Hmin)
         msg=msg+chr(10)+chr(13)+"Hum. max. = "+str(Hmax)
         bot.sendMessage(chat_id,msg)
      elif(msg_rec[0:12].lower()=="config tmax "):
         tmax=msg_rec[12:]
         query="SELECT MAX(id) from configuracion WHERE 1"
         n=run_query(query)
         n=n[0][0]
         query="UPDATE configuracion set t_max='%s' WHERE id='%s'"%(tmax,n)
         rta=run_query(query)
         query="SELECT t_max FROM configuracion WHERE id='%s'"%n
         tmax=run_query(query)
         msg="Temp. max configurada en "+str(tmax[0][0])
         bot.sendMessage(chat_id,msg)
         #print rta
      elif(msg_rec[0:12].lower()=="config tmin "):
         tmin=msg_rec[12:]
         query="SELECT MAX(id) from configuracion WHERE 1"
         n=run_query(query)
         n=n[0][0]
         query="UPDATE configuracion set t_min='%s' WHERE id='%s'"%(tmin,n)
         rta=run_query(query)
         query="SELECT t_min FROM configuracion WHERE id='%s'"%n
         tmin=run_query(query)
         msg="Temp. min configurada en "+str(tmin[0][0])
         bot.sendMessage(chat_id,msg)
         #print rta
      elif(msg_rec[0:12].lower()=="config hmax "):
         hmax=msg_rec[12:]
         query="SELECT MAX(id) from configuracion WHERE 1"
         n=run_query(query)
         n=n[0][0]
         query="UPDATE configuracion set h_max='%s' WHERE id='%s'"%(hmax,n)
         rta=run_query(query)
         query="SELECT h_max FROM configuracion WHERE id='%s'"%n
         hmax=run_query(query)
         msg="Hum. max configurada en "+str(hmax[0][0])
         bot.sendMessage(chat_id,msg)
         #print rta
      elif(msg_rec[0:12].lower()=="config hmin "):
         hmin=msg_rec[12:]
         query="SELECT MAX(id) from configuracion WHERE 1"
         n=run_query(query)
         n=n[0][0]
         query="UPDATE configuracion set h_min='%s' WHERE id='%s'"%(hmin,n)
         rta=run_query(query)
         query="SELECT h_min FROM configuracion WHERE id='%s'"%n
         hmin=run_query(query)
         msg="Hum. min configurada en "+str(hmin[0][0])
         bot.sendMessage(chat_id,msg)
      elif(msg_rec.lower()=="direcciones"):
         interfaces=netifaces.interfaces()
         msg="Utilice las siguientes direcciones para acceder al sistema web:"+chr(10)+chr(13)+chr(10)+chr(13)
         for i in interfaces:
            addrs = netifaces.ifaddresses(i)
            direccion= addrs[netifaces.AF_INET][0]["addr"]
            if i=="eth0":
               msg=msg+"Desde la red local: http://"+str(direccion)+"/monitor/ "+chr(10)+chr(13)+chr(10)+chr(13)
            elif i=="wlan0":
               msg=msg+"Desde la red Wifi del equipo: http://"+str(direccion)+"/monitor/"
         bot.sendMessage(chat_id,msg)
      else:
         bot.sendMessage(chat_id,"Comando no reconocido")
   


NUMERO_SERIE="0258768680"

DB_HOST='localhost'
DB_USER='root'
DB_PASS='andres'
DB_NAME='monitoreo'


bot=telepot.Bot('196708475:AAFXMiVQVR1CwyYcs9Hv4Lsa1otAg4gLCM0')
bot.message_loop(handle)
while 1:
   time.sleep(10)
