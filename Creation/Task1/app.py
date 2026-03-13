from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/status')
def status():
    uid = os.getuid()
    hostname = socket.gethostname()
    

    return jsonify({
        "status": "ALIVE",
        "service_name": "K1-DEBUG",
        "user_id": uid,
        "security": "SECURE" if uid != 0 else "INSECURE_ROOT",
        "container_hostname": hostname,
        "msg": "START->K1"
    })

if __name__ == "__main__":
 
    print("Uruchamiam serwer Flask na porcie 8080...")
    app.run(host='0.0.0.0', port=8080)