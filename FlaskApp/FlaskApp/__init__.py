from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("index.html")
   
@app.route('/dht1')
def DHT1():
   import sys
   import Adafruit_DHT
   humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
   pagetype = 'dht1'
   s1 = "Temperature"
   if temperature >=35:
      print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
      return render_template("home1.html",s1=s1, pagetype=pagetype, w1="temp too high", op1=temperature)
   else:
      return render_template("home1.html", s1=s1, pagetype=pagetype, op1=temperature)
   

@app.route('/dht2')
def DHT2():
   import sys
   import Adafruit_DHT
   humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
   pagetype = 'dht2'
   s1 = "Humidity"
   if humidity >=50:
      print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
      return render_template("home1.html",s1=s1, pagetype=pagetype, w1="hum too high", op1=humidity)
   else:
      return render_template("home1.html", s1=s1, pagetype=pagetype, op1=humidity)   
     
   
@app.route('/reed')
def REED():
   import RPi.GPIO as GPIO
   pagetype = 'reed'
   s1 = "Magnetic Field"
   inPin = 4
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(inPin, GPIO.IN)

   while True:
       value = GPIO.input(inPin)
       if value == GPIO.LOW:
           return render_template("home1.html",s1=s1, pagetype=pagetype, w1="Magnetic Field Detected!!")
       else:
           return render_template("home1.html",s1=s1, pagetype=pagetype, op1="No Magnetic Field Detected!!")  
    
@app.route('/hcsr')
def HCSR():
   import RPi.GPIO as GPIO
   import time
   GPIO.setmode(GPIO.BCM)

   pagetype = 'hcsr'
   s1 = "Object Distance"
   
   TRIG = 23 
   ECHO = 24

   GPIO.setwarnings(False)
   GPIO.setup(TRIG,GPIO.OUT)
   GPIO.setup(ECHO,GPIO.IN)

   GPIO.output(TRIG, False)
   time.sleep(2)

   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)

   while GPIO.input(ECHO)==0:
     pulse_start = time.time()

   while GPIO.input(ECHO)==1:
     pulse_end = time.time()

   pulse_duration = pulse_end - pulse_start

   distance = pulse_duration * 17150

   distance = round(distance, 2)
   if distance <=5:
      return render_template("home1.html", s1=s1, pagetype=pagetype,w1="Too Close!",op1=distance)
   else:
      return render_template("home1.html", s1=s1, pagetype=pagetype,op1=distance)
      

@app.route('/sw')
def SW():
   pagetype = 'sw'
   s1 = "Vibration"
   return render_template("home1.html", s1=s1, pagetype=pagetype)
   
if __name__ == "__main__":
   app.run(debug=True)

