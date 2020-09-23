from flask import Flask,request,make_response

app = Flask(__name__)

@app.route("/validate")
def f():
    print(request.headers)
    resp=make_response()
    resp.headers["X-msg"]="777"
    if request.headers.get("Username","-") != "Ram" :
        return "Unauthorized", 401
    resp.set_cookie("msg","PraiseGod!",30)
    print(resp)
    return resp

@app.route("/error")
def f1():
    return "error",500

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888)