import json
import traceback
from flask import Flask, render_template, request, jsonify
import jsonata
import simplejson

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    body = request.get_json(force=True)
    json_input = body.get("json_input", "")
    expression = body.get("expression", "$")

    try:
        # Use parse_int=str to load all integers as strings, preserving precision
        # data = simplejson. loads(json_input, parse_int=str) if json_input.strip() else None
        data = simplejson.loads(json_input) if json_input.strip() else None
        # data = simplejson.loads(json_input, use=True) if json_input.strip() else None
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Invalid JSON input: {e}"}), 200
    
    
    try:
        expr = jsonata. Jsonata(expression)
        result = expr.evaluate(data)
        # Serialize with custom JSON encoder to preserve bigint precision
        result_text = json. dumps(result, indent=2, default=str)
        # result_text = simplejson.dumps(result, use_decimal=True, indent=2, default=str)
        return jsonify({"result_text": result_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 200
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

