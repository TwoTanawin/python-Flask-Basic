from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data = {"name":"Tanawin", "age":23, "salary":80_000}
    return render_template("index.html", data = data)

@app.route('/about')
def about():
    product = ["M1", "M2", "M3"]
    return render_template("about.html", product = product)

@app.route('/admin')
def profile():
    name = "Tanawin ISE"
    return render_template("admin.html", name = name)

@app.route('/sendData')
def signupForm():
    fname = request.args.get('fname')
    discription = request.args.get('discription')
    return render_template("thankyou.html", data={"name":fname, "discription":discription})

# @app.route("/user/<name>/<location>")
# def member(name, location):
#     return "<h1>Hello : {} location : {}</h1>".format(name, location)

if __name__=="__main__":
    app.run()