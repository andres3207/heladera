#!/usr/bin/python
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
from time import sleep


pin_rs=25
pin_e=24
pins_db=[23, 12, 16, 20]




GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_e, GPIO.OUT)
GPIO.setup(pin_rs, GPIO.OUT)
for pin in pins_db:
	GPIO.setup(pin, GPIO.OUT)




def clear():
	#""" Blank / Reset LCD """

	cmd(0x33) # $33 8-bit mode
	cmd(0x32) # $32 8-bit mode
	cmd(0x28) # $28 8-bit mode
	cmd(0x0C) # $0C 8-bit mode
	cmd(0x06) # $06 8-bit mode
	cmd(0x01) # $01 8-bit mode

def cmd( bits, char_mode=False):
	#""" Send command to LCD """

	sleep(0.001)
	bits=bin(bits)[2:].zfill(8)

	GPIO.output(pin_rs, char_mode)

	for pin in pins_db:
		GPIO.output(pin, False)

	for i in range(4):
		if bits[i] == "1":
			GPIO.output(pins_db[::-1][i], True)

	GPIO.output(pin_e, True)
	GPIO.output(pin_e, False)

	for pin in pins_db:
		GPIO.output(pin, False)

	for i in range(4,8):
		if bits[i] == "1":
			GPIO.output(pins_db[::-1][i-4], True)


	GPIO.output(pin_e, True)
	GPIO.output(pin_e, False)


def message(text):
	#""" Send string to LCD. Newline wraps to second line"""

	for char in text:
		if char == '\n':
			cmd(0xC0) # next line
		else:
			cmd(ord(char),True)



clear()
while(1):
	clear()
	#cmd(0xC0)
	#sleep(0.00001)
	temp=""
	hum=""
	while(((temp=="") or (hum==""))):
		f1=open("/var/www/web/monitor/application/third_party/scripts/temp2",'r')
		temp=f1.read()
		f1.close()
		f2=open("/var/www/web/monitor/application/third_party/scripts/hum2",'r')
		hum=f2.read()
		f2.close()
		temp=str(temp)
		hum=str(hum)
	#print(temp)
	#print(hum)
	#clear()
	#clear()
	message("Temperatura "+temp+"\nHumedad     "+hum)
	#cmd(0xC0)
	sleep(0.7)
	#cmd(0xC0)
