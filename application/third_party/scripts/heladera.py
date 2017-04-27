#!/usr/bin/python



def obt_temp():
	tfile=open("/sys/bus/w1/devices/28-0000073587d3/w1_slave")
	text=tfile.read()
	tfile.close()
	secondline=text.split("\n")[1]
	temperaturedata=secondline.split(" ")[9]
	temperature =float(temperaturedata[2:])
	temperature=temperature/1000
	return float(temperature)

mensaje =str(obt_temp()) +" C"
print mensaje
