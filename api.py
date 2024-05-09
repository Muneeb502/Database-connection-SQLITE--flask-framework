from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
     return render_template("index.html")
 
@app.route("/adddata")
def adddata():
    return render_template("form.html")
     
@app.route("/submitform" , methods= ["POST","GET"])
def submit():
    if request.method == "post":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
    return "form hasbeen submitted"    
        

if __name__ == "__main__":
    app.run(debug=True, port=5001)
