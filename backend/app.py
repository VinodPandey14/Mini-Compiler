from flask import Flask, request, jsonify
from compiler.engine import process_code
from flask_cors import CORS  # type: ignore
import os

app = Flask(__name__)
CORS(app)

@app.route('/compile', methods=['POST'])
def compile_code():
    try:
        data = request.json
        print("Received Data:", data)

        if 'code' not in data or not isinstance(data['code'], str):
            return jsonify({"error": "Expected a string for 'code'"}), 400
        if 'grammar' not in data or not isinstance(data['grammar'], str):
            return jsonify({"error": "Expected a string for 'grammar'"}), 400

        code = data['code']
        grammar = data['grammar']

        result = process_code(code, grammar)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/ping', methods=['GET'])
def ping():
    try:
        return "pong", 200
    except:
        return "error", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
