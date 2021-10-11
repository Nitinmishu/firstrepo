from flask import Flask ,render_template , request,redirect
from werkzeug.utils import redirect 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import synonym

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///StudentList.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONs'] = False
db= SQLAlchemy(app)

class Student(db.Model):
    Sno = db.Column(db.Integer, primary_key = True)
    First = db.Column(db.String(200), nullable = False)
    Last = db.Column(db.String(500), nullable = False)
    Description = db.Column(db.String(500), nullable = False)

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.First}"

@app.route("/update/{{student.Sno}}", methods = ["GET","POST"])
def hello_world():
    if request.method == 'POST':
        title = request.form["title"]
        text = request.form["text"]
        desc = request.form["desc"]
        student = Student(First = title,Last = text ,Description = desc)
        db.session.add(student)
        db.session.commit()
    allstudent = Student.query.all()
    return render_template("Index.html", allstudent=allstudent)

@app.route("/show")
def products():
    allstudent = Student.query.all()
    print(allstudent)
    return "this is product page"

@app.route("/update/<int:Sno>")
def Update(Sno):
    if request.method == "POST":
        
    student = Student.query.filter_by(Sno=Sno).first()
    return render_template("Update.html",student= student)

    
@app.route("/delete/<int:Sno>")
def delete(Sno):
    student = Student.query.filter_by(Sno=Sno).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")

if __name__  == "__main__":
    app.run(debug=True)
    
