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
    if request.method == "POST":
        slitWidth  = request.form['Slit Width']
        slitSep  = request.form['Slit Separation']
        screenDist  = request.form['Screen Distance']
        lightWL  = request.form['Light Wavelength']
        #TODO: ADD COLOR DROPDOWN AND LIGHT WAVELENGTH INTERACTIONS
        return 

    else:
        return render_template('index.html')
