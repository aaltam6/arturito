from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
     if request.method == 'POST':
          return render_template('home.html')
     else:
          return render_template('home.html')

@app.route('/CV', methods=['GET', 'POST'])
def CV():
    if request.method == 'POST':
         return render_template('CV.html')
    else:
          return render_template('CV.html')
    
@app.route('/extra', methods=['GET', 'POST'])
def extra():
    if request.method == 'POST':
         return render_template('extra.html')
    else:
          return render_template('extra.html')
    
@app.route('/aws', methods=['GET', 'POST'])
def aws():
     if request.method == 'POST':
          return render_template('aws.html')
     else:
          return render_template('aws.html')