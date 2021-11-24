from app import app
from flask import render_template

@app.route('/')
def who_we_are():
    return render_template('who-we-are.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

@app.route('/where-we-work')
def where_we_work():
    return render_template('where-we-work.html')