import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    forbidden_patterns = [
        'secret.txt', 
        'id_rsa', 
        '.git', 
        'notes.txt', 
        '.env'
    ]
    
    current_files = os.listdir('.')
    found = [f for f in forbidden_patterns if f in current_files]
    
    return jsonify({
        "status": "ALIVE",
        "leaked_files_found": len(found) > 0,
        "found_list": found,
        "task": 3
    })

if __name__ == "__main__":
 
    print("Uruchamiam serwer Flask na porcie 8080...")
    app.run(host='0.0.0.0', port=8080)