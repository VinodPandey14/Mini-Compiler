from flask import Flask, request, jsonify
from compiler.engine import process_code
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/compile', methods=['POST'])
def compile_code():
    try:
        data = request.json  # Get the incoming JSON data
        print("Received Data:", data)

        # Check if 'code' and 'grammar' exist and are strings
        if 'code' not in data or not isinstance(data['code'], str):
            return jsonify({"error": "Expected a string for 'code'"}), 400
        if 'grammar' not in data or not isinstance(data['grammar'], str):
            return jsonify({"error": "Expected a string for 'grammar'"}), 400

        code = data['code']
        grammar = data['grammar']

        # Process code with lexer, parser, and IR generation
        result = process_code(code, grammar)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
