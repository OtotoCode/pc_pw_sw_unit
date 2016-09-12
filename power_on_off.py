#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess

#out put gpio pin
OUTPUT=16

#host ip
HOST="ip address"

#initialize
def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(OUTPUT,GPIO.OUT,initial=GPIO.LOW)

#finalize
def finalize():
	GPIO.cleanup()

#gpio power on
def on():
	GPIO.output(OUTPUT,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(OUTPUT,GPIO.LOW)

#gpio power off
def off():
	GPIO.output(OUTPUT,GPIO.HIGH)
	time.sleep(10)
	GPIO.output(OUTPUT,GPIO.LOW)

#ping check
def ping_check():
    pcheck = subprocess.Popen(["ping", "-c", "1", HOST],stdout = subprocess.PIPE,stderr = subprocess.PIPE )
    time.sleep(10)
    pcheck_out, pcheck_error = pcheck.communicate()
    out_line = pcheck_out.split("\n")
    for i in range(0,len(out_line)):
	print out_line[i]
    if "1 received, 0% packet loss" in pcheck_out:
    	print "ping success!!"
    else:
    	print "--ping fail--"

#power on main
def power_on():
	print "power on y/n"
	input_line = raw_input()
	if input_line == "y":
		print "power on please wait"
		on()
		time.sleep(120)
		print "ping check please wait"
		ping_check()
	elif input_line == "n":
		print "power on cancel"
	else:
		print "input error"

#power off main
def power_off():
	print "--CAUTION---"
	print "power off? y/n"
	input_line = raw_input()
	if input_line == "y":
		print "power off please wait"
		off()
		print "ping check please wait"
		ping_check()
	elif input_line == "n":
		print "power off cancel"
	else:

		print "input error"

#main
if __name__ == '__main__':
	try:
		init()
		print "please input power on/off "
		input_l = raw_input()
		if input_l == "on":
			power_on()
		elif input_l == "off":
			power_off()
		else:
			print "input error"
		finalize()
	except:
		finalize()
