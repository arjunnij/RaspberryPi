from flask import Flask, render_template 
import bluetooth

app = Flask(__name__)

def getDevices():
    nearby_devices = bluetooth.discover_devices(duration=5) 
    return nearby_devices; 

@app.route('/')
def index():
    dev_list = getDevices(); 
    return render_template('index.html', myList=dev_list); 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

