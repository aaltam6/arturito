from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
     if request.method == 'POST':
          return render_template('home.html')
     else:
          return render_template('home.html')

@app.route('/experience', methods=['GET', 'POST'])
def experience():
    if request.method == 'POST':
         return render_template('experience.html')
    else:
          return render_template('experience.html')
    
@app.route('/education', methods=['GET', 'POST'])
def education():
    if request.method == 'POST':
         return render_template('education.html')
    else:
          return render_template('education.html')