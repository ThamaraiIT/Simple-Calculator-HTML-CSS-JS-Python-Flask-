from flask import Flask, jsonify, request, render_template
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        allowed_names = {name: obj for name, obj in math.__dict__.items()}
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return jsonify(result=result)
    except Exception:
        return jsonify(result="Error")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
