from flask import Flask, render_template, redirect, session, request
from random import randrange
from datetime import datetime

app = Flask(__name__)
app.secret_key = "soup"

@app.route("/")
def landing_page():
    if 'gold' not in session:
        session['gold'] = 0

    if 'activity_log' not in session:
        session['activity_log'] = []

    return render_template("index.html")

@app.route("/process_money", methods=["post"])
def process_money():
    building = request.form.get('building')
    gold = 0

    if building == "farm":
        gold = randrange(10, 20)
    elif building == "cave":
        gold = randrange(5, 10)
    elif building == "house":
        gold = randrange(2,5)
    elif building == "casino":
        gold = randrange(-50, 50)

    session['gold'] += gold
    
    if gold < 0:
        session['activity_log'].insert(0, ("red", f"Entered a casino and lost {gold}! ({datetime.strftime(datetime.now(), '%Y/%m/%d %I:%M %p')})"))
    else:
        session['activity_log'].insert(0, ("green", f"Earned {gold} from the {building}! ({datetime.strftime(datetime.now(), '%Y/%m/%d %I:%M %p')})"))

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)