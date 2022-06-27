# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)
# Configurar la librería para usar el número de pin.
# Llame GPIO.setmode(GPIO.BCM) para usar el canal SOC definido por Broadcom
GPIO.setmode(GPIO.BOARD)
# Configurar el pin 3 como entrada
boton=3
GPIO.setup(boton, GPIO.IN)
while True:
	
	boton_push = GPIO.input(boton)
	if boton_push==0:
		print("Se presiono boton")
	else:
		print("No se presiono boton")
