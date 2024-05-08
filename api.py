from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/muneeb ur rehman/OneDrive - Dawood University of Engineering Technology/Desktop/database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Use app.app_context() to work within the application context
with app.app_context():
    # Create all tables in the database
    db.create_all()

@app.route("/")
def home():
     return "hello"
 
if __name__ == "__main__":
    app.run(debug=True, port=5001)
