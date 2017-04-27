#!/usr/bin/python

from sht1x.Sht1x import Sht1x as SHT1x
import time
import sys

dataPin = 11

clkPin = 7

sht1x = SHT1x(11,7)

while True:

	temp=sht1x.read_temperature_C()

	hum=sht1x.read_humidity() 

	temp="{0:0.1f}".format(temp)
	hum="{0:0.1f}".format(hum)
	#print "Temperatura: "+temp
	#print "Humedad: "+hum
	if ((temp!="") and (hum!="")):
	#if hum is not None and temp is not None:
		time.sleep(1)
		f=open("/var/www/web/monitor/application/third_party/scripts/temp2","w")
		f.write(temp)
		f.close()
		f2=open("/var/www/web/monitor/application/third_party/scripts/hum2","w")
		f2.write(hum)
		f2.close()


