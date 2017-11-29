from flask import Flask, render_template # import redirect & session
app = Flask(__name__)

# session.name = 'Alan'

@app.route("/")
def hello():
    return render_template('float.html', name='Alan')

# @app.route("/name/<language>")
# def name(language):
# 	if language == 'EN':
# 		return render_template('english_name.html')
# 	else:
#     	return render_template('home.html')

# @app.route("/email")
# def email():
#     return render_template('home.html')


# Post Request to [ALAN WILL PROVIDE LINK HERE]
# Name (required), email (optional), kiosk number (required)
# success or failure
# if failure, retry until you succeed ( delay of 10 seconds )
# https://stackoverflow.com/questions/15463004/how-can-i-send-a-get-request-from-my-flask-app-to-another-site 
# note that the example is a GET request, so we need to look for POST in requests library



if __name__ == '__main__':
    app.run(debug = True)