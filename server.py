from flask import Flask, render_template, redirect, session, url_for, request # import redirect & session
import requests
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RAS@T'

FIREBASE_URL = "firebase.com" # TODO(alan): Change this URL once the server is set up
KIOSK = 1

@app.route("/")
def welcome():
    return render_template('home.html')

@app.route("/language/<lang>")
def language(lang):
    if lang in ["english", "chinese", "french", "german", "spanish", "japanese"]:
        session['language'] = lang
    else:
        raise Exception("Language not found!")
    return redirect(url_for('name'))

@app.route("/name", methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(url_for('email'))
    else: # get request
        print(session['language'])
        return render_template('name.html', language=session['language'])

@app.route("/email", methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        session['email'] = request.form['email']
        response = requests.post(FIREBASE_URL, data = {'name': session['name'], 'email': session['email'], 'kiosk': KIOSK})
        print(response)
        return redirect(url_for('takeorb'))
    else: # get request
        return render_template('email.html', language=session['language'], name=session['name'])

@app.route("/takeorb")
def takeorb():
    return render_template('takeorb.html', language=session['language'], name=session['name'])

@app.route("/havefun")
def havefun():
    return render_template('havefun.html',language=session['language'], name=session['name'])

@app.route("/error")
def error():
    return render_template('error.html', language='english')

# @app.route("/name/<language>")
# def name(language):
#   if language == 'EN':
#       return render_template('english_name.html')
#   else:
#       return render_template('home.html')

# @app.route("/email")
# def email():
#     return render_template('home.html')


# Post Request to [ALAN WILL PROVIDE LINK HERE]
# Name (required), email (required), kiosk number (required)
# success or failure
# if failure, retry until you succeed ( delay of 10 seconds )
# https://stackoverflow.com/questions/15463004/how-can-i-send-a-get-request-from-my-flask-app-to-another-site 
# note that the example is a GET request, so we need to look for POST in requests library



if __name__ == '__main__':
    app.run(debug = True)
