from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "combo"

@app.route("/")
def survey_form():
    return render_template('index.html')

@app.route("/process_form", methods=['POST'])
def on_submit():
    if 'form_data' not in session:
        session['form_data'] = request.form

    return redirect("/result")

@app.route("/result")
def results():
    return render_template("result.html" thing='thing')

if __name__ == "__main__":
    app.run(debug=True)

