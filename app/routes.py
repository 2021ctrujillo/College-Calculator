from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/collegecalculator', methods=["GET", "POST"])
def collegecalculator():
    user_input = dict(request.form)
    print(user_input)
    school = user_input["school"]
    testtype= user_input["testtype"]
    score = int(user_input["score"])
    GPA = float(user_input["GPA"])
    print(school)
    print(testtype)
    print(score)
    print(GPA)

@app.route('/results')
def results():
        output = model.iterate(school, score, score, GPA, testtype)
        return output
        output2 = model.GPAAA(school, score, score, GPA, testtype)
        return output2
