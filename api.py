from flask import Flask,render_template,request
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
def home():
     return render_template("index.html")
 
@app.route("/adddata")
def adddata():
    return render_template("form.html")


@app.route("/result")
def result():
    return render_template("result.html")
     
@app.route("/submitform" , methods= ["POST","GET"])
def submit():
    if request.method == "POST":  
        name = request.form["name"]
        email = request.form["email"]
        with sql.connect("mydatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO student (name, email) VALUES ( ?, ?)", (name, email))
            con.commit()
        return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
