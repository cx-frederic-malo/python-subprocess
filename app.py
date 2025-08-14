import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/run', methods=['GET'])
def run_script():
    name = request.args.get('name', 'World')
    subprocess.run(["python", "main.py"])
    result = subprocess.run(f"echo Hello {name}", shell=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
 