# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa el módulo time
import time

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)

# Configurar la librería para usar el número de pin.
# Llame GPIO.setmode(GPIO.BCM) para usar el canal SOC definido por Broadcom
GPIO.setmode(GPIO.BOARD)
#Creacion de variables
push=3
led =7

#Configurar los pines de salida y entrada 
GPIO.setup(led,GPIO.OUT)
GPIO.setup(push,GPIO.IN)

#Variables auxiliares para guardar el estado
estadoLed = 0
estadoAnterior=0 

#Ciclo infinito para encender el led  cuando se presine el boton
while True:
	led_push = GPIO.input(push) #entrada del boton
	if (not led_push)==1 and estadoAnterior==0:
		estadoLed = 1 - estadoLed
		time.sleep(0.01)
	estadoAnterior = not led_push
	if estadoLed==1:
		GPIO.output(led,1)
	else:
		GPIO.output(led,0)

