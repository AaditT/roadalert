from multiprocessing import Process
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 7
GPIO.setup(led, GPIO.OUT)

buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)


Buzzer = 23

CL = [0, 131, 147, 165, 175, 196, 211, 248]
CM = [0, 262, 294, 330, 350, 393, 441, 495]
CH = [0, 525, 589, 661, 700, 786, 882, 990]
song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6]]
beat_1 = [1, 1, 3, 1, 1, 3, 1, 1]


global Buzz
Buzz = GPIO.PWM(Buzzer, 4400)

def turnBuzzerOn():
    Buzz.start(50)
    print ('\n    buzzer...')
    for i in range(1, len(song_1)):
        Buzz.ChangeFrequency(song_1[i])
        time.sleep(beat_1[i] * 0.1)
    time.sleep(1)

def turnBuzzerOff():
    Buzz.stop()
    GPIO.output(Buzzer, 1)

def turnLEDOn():
	GPIO.output(led, GPIO.HIGH)
	time.sleep(2.2)
	GPIO.output(led, GPIO.LOW)

def turnLEDOff():
    GPIO.output(led, GPIO.LOW)



def alert():
	p1 = Process(target = turnLEDOn)
	p1.start()
	p2 = Process(target = turnBuzzerOn)
	p2.start()
