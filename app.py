from flask import Flask , render_template, request
app = Flask(__name__)

from datetime import datetime

@app.route('/my', methods=['POST']) 
def do_search() -> 'html': 
    phrase = request.form['phrase'] 
    title = 'Here are your results:'
    day1 = int(datetime.today().day)
    mon1  = int(datetime.today().month)
    yr1 = int(datetime.today().year)

    day = int(phrase[0] + phrase[1])
    mon =int( phrase[3] + phrase[4])
    yr = int(phrase[6:11])


    if day>day1:
        mon1 -= 1
        day1+= 30

    r_day = str(day1 - day)

    if mon>mon1:
        yr1 -= 1
        mon1+= 12

    r_mon = str(mon1 - mon)

    r_yr = str(yr1 - yr)

    results = r_yr + ' years ' + r_mon + ' months ' + r_day
    
    return render_template('results.html', the_title=title, the_phrase=phrase, the_results=results,)

@app.route('/') 
@app.route('/entry') 
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Age Calculator') 


app.run(debug=True)