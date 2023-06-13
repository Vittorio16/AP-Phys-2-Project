from flask import Flask, request, render_template, session
from flask_session import Session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=["GET", "POST"])
def index():
        return render_template('index.html')
    
    
@app.route('/doubleSlitInterference', methods=["GET", "POST"])
def doubleSlitInterference():
    if request.method == "POST":
        d  = int(request.form['d'])
        max_y  = int(request.form['max_y'])
        max_x  = int(request.form['max_x'])
        point_step = int(request.form['point_step'])
        wavelength = int(request.form['wavelength'])
        render_template("singleSlitInterference.html")
        print ("sjicini")
        create_graph(d, max_y, max_x, point_step, wavelength)
        print ("jsdni")
        return render_template('doubleSlitInterference.html', graph="graph.png")

    else:
        return render_template('doubleSlitInterference.html')
    

@app.route('/singleSlitInterference', methods=["GET", "POST"])
def singleSlitInterference():
    if request.method == "POST":
        return None

    else:
        return render_template('singleSlitInterference.html')