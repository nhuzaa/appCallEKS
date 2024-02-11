
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    # Extract numbers from query parameters
    num1 = request.args.get('num1', type=int)
    num2 = request.args.get('num2', type=int)
    # Calculate the sum
    result = num1 + num2
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
