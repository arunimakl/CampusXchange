from flask import Flask, render_template

app = Flask(__name__)

# ---------- Books Data ----------
books = [
    {
        "title": "Design Data Handbook For Mechanical Engineers",
        "author": "Balaveera K",
        "dept": "Mechanical/Industrial",
        "owner": "Ann Mathew",
        "price": "Rs 300",
        "condition": "Used",
        "contact": "9488215630",
        "topics": ["mechanical", "theory of machine design", "stress"]
    },
    {
        "title": "Hydraulics and Pneumatics",
        "author": "Jagadeesha T",
        "dept": "ECE/Mechanical/Industrial/EEE/CS/EL/AE",
        "owner": "Not Specified",
        "price": "Rs 200",
        "condition": "Good",
        "contact": "8510236549",
        "topics": ["robotics", "Hydraulics", "Pneumatics","Automation"]
    }
]

# ---------- Tutors Data ----------
tutors = [
    {"name": "Alice", "skill": "Python", "rate": "$10/hr", "days": "Mon, Wed", "location": "Online"},
    {"name": "Bob", "skill": "Digital Electronics", "rate": "$12/hr", "days": "Tue, Thu", "location": "Offline"}
]

# ---------- Skills Data ----------
skills = [
    {"skill": "Python", "owner": "Alice", "experience": "2 yrs", "contact": "alice@example.com"},
    {"skill": "Matlab", "owner": "Charlie", "experience": "1 yr", "contact": "charlie@example.com"}
]

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def books_page():
    return render_template("books.html", books=books)

@app.route("/tutors")
def tutors_page():
    return render_template("tutors.html", tutors=tutors)

@app.route("/skills")
def skills_page():
    return render_template("skills.html", skills=skills)

if __name__ == "__main__":
    app.run(debug=True)