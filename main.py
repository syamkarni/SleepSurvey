from flask import Flask, request, redirect, render_template, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import csv
from sqlalchemy.exc import SQLAlchemyError
import os

app = Flask(__name__)

# Get the absolute path to the directory of the current file
basedir = os.path.abspath(os.path.dirname(__file__))

# Set the path to the SQLite database file
db_path = os.path.join(basedir, 'user_info.db')

# Configure Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    number = db.Column(db.String(50))
    email = db.Column(db.String(100))
    question1 = db.Column(db.String(200))
    question2 = db.Column(db.String(200))
    question3 = db.Column(db.String(200))
    question4 = db.Column(db.String(200))
    question5 = db.Column(db.String(200))
    question6 = db.Column(db.String(200))
    question7 = db.Column(db.String(200))
    question8 = db.Column(db.String(200))
    question9 = db.Column(db.String(200))
    question10 = db.Column(db.String(200))
    question11 = db.Column(db.String(200))
    question12 = db.Column(db.String(200))
    question13 = db.Column(db.String(200))
    question14 = db.Column(db.String(200))
    question15 = db.Column(db.String(200))
    question16 = db.Column(db.String(200))
    question17 = db.Column(db.String(200))
    question18 = db.Column(db.String(200))
    question19 = db.Column(db.String(200))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/loader')
def loader():
    return render_template('loader.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        user = User(
            name=request.form['name'],
            age=request.form['age'],
            gender=request.form['gender'],
            number=request.form['number'],
            email=request.form['email'],
            question1=request.form['question1'],
            question2=request.form['question2'],
            question3=request.form['question3'],
            question4=request.form['question4'],
            question5=request.form['question5'],
            question6=request.form['question6'],
            question7=request.form['question7'],
            question8=request.form['question8'],
            question9=request.form['question9'],
            question10=request.form['question10'],
            question11=request.form['question11'],
            question12=request.form['question12'],
            question13=request.form['question13'],
            question14=request.form['question14'],
            question15=request.form['question15'],
            question16=request.form['question16'],
            question17=request.form['question17'],
            question18=request.form['question18'],
            question19=request.form['question19']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/loader')
    except SQLAlchemyError as e:
        db.session.rollback()
        return str(e), 500

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/export-csv', methods=['GET'])
def export_csv():
    try:
        query = User.query.all()
        csv_path = os.path.join(basedir, 'users.csv')
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = [column.name for column in User.__table__.columns]
            writer.writerow(header)
            for user in query:
                row = [getattr(user, column) for column in header]
                writer.writerow(row)
        return send_from_directory(directory=basedir, path='users.csv', as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    with app.app_context():  # Wrap db.create_all in an application context
        db.create_all()
    app.run(debug=True, port=3000)
