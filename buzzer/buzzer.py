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
BUZZER_PIN = 3  # Buzzer pin number

#Hacemos la variable como una salida
GPIO.setup(BUZZER_PIN, GPIO.OUT)

while True:
	duration=int(input("Ingrese la duracion: "))
	for i in range(duration):
		GPIO.output(BUZZER_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(BUZZER_PIN, GPIO.LOW)
		time.sleep(1)

