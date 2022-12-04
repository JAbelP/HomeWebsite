from telnetlib import STATUS
from flask import Flask
import flux_led
app = Flask(__name__)
light = flux_led.WifiLedBulb("your ip here")

@app.route("/members")
def members():
    return {"members": ["Member1","Member2","Member3","member4"]}

@app.route("/isOn")
def isOn():
    return str(light.isOn())

@app.route("/lightBulbOff")
def turnOffLightBulb():
    light.turnOff()
    return STATUS

@app.route("/lightBulbOn")
def turnOnLightBulb():
    light.turnOn()
    return STATUS

@app.route("/lightBulbBlue")
def turnLightBlue():
        light.setRgb(0,0,255)
        return STATUS

@app.route("/lightBulbRed")
def turnLightRed():
        light.setRgb(255,0,0)
        return STATUS

@app.route("/lightBulbGreen")
def turnLightGreen():
        light.setRgb(0,255,0)
        return STATUS

if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000, debug=True)
