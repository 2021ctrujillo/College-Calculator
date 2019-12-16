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

    output = model.iterate(school, score, score, GPA, testtype)
    output2 = model.GPAAA(school, score, score, GPA, testtype)
    print (output)
    print (output2)
    return render_template('results.html', school = school, GPA = GPA, output = output, output2 = output2)
