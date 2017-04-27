#!/usr/bin/python
import time


def obt_temp():
	tfile=open("/sys/bus/w1/devices/28-0000073587d3/w1_slave")
	text=tfile.read()
	tfile.close()
	secondline=text.split("\n")[1]
	temperaturedata=secondline.split(" ")[9]
	temperature =float(temperaturedata[2:])
	temperature=temperature/1000
	return float(temperature)


while(1):
	temp=obt_temp()
	temp="{0:0.1f}".format(temp)
	f=open("/var/www/web/heladera/application/third_party/scripts/temp","w")
	f.write(temp)
	f.close()
	print(temp)
	time.sleep(1)

