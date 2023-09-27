from flask import Flask , redirect, url_for, render_template, request
from solver import *




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST", "GET"])
def solver():
    if(request.method == 'POST'):
        # print("POST REQ")

        ddx = request.form['ddx']
        c_y = request.form['c_y']
        const = request.form['const']
        # print(const)
        eqn = get_eqn(ddx, c_y, const)

        solv = solve(ddx, c_y, const)
        # return redirect(url_for('soln',eqn = eqn, soln = solv))
        return render_template("solution.html", eqn = eqn, soln = solv)
    
    return render_template("equation-solver.html")

@app.route("/about")
def about():
    return render_template("about-our-team.html")

@app.route("/manual")
def manual():
    return render_template("user-manual.html")

if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
