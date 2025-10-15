from flask import Flask

app = Flask(__name__)
@app.route('/')
def home()->str:
    return "<h3>Hello, world!</h3>"

app.run(debug=True, host='127.0.0.1', port= 5500)