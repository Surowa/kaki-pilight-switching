#!/usr/bin/python

import schedule
import time
import os

def Lamp2Aan():
	os.system('sudo bash /home/pi/shared/lamp2aan.sh')
	return

def Lamp2Uit():
	os.system('sudo bash /home/pi/shared/lamp2uit.sh')
	return

def Lamp3Aan():
	os.system('sudo bash /home/pi/shared/lamp3aan.sh')
	return

def Lamp3Uit():
	os.system('sudo bash /home/pi/shared/lamp3uit.sh')
	return

def AlleLampenUit():
	os.system('sudo bash /home/pi/shared/allesuit.sh')
	return



schedule.every().day.at("21:10").do(Lamp2Aan)
schedule.every().day.at("22:50").do(Lamp3Aan)
schedule.every().day.at("23:00").do(Lamp2Uit)
schedule.every().day.at("23:05").do(Lamp3Uit)
schedule.every().day.at("23:59").do(AlleLampenUit)

while True:
	schedule.run_pending()
	time.sleep(5)

