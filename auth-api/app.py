from flask import Flask,request

app = Flask(__name__)

@app.route("/validate")
def f():
    print(request.headers)
    return "ok",200

@app.route("/error")
def f1():
    return "error",500

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888)