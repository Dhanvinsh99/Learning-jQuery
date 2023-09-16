from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time', methods=['GET'])
def get_time():
    current_time = time.ctime()
    epoch_time_ns = int(time.time_ns())
    time_bc_ns = 62167195440000000000 + time.time_ns()
    
    return jsonify({
        'current_time': current_time,
        'epoch_time_ns': epoch_time_ns,
        'time_bc_ns': time_bc_ns
    })

if __name__ == '__main__':
    app.run(port=0, debug=True)
