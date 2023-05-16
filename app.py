from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    slitWidth  = request.form['Slit Width']
    slitSep  = request.form['Slit Separation']
    screenDist  = request.form['Screen Distance']
    lightWL  = request.form['Light Wavelength']
    #TODO: ADD COLOR DROPDOWN AND LIGHT WAVELENGTH INTERACTIONS
    return 
