from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('float.html')

# @app.route("/name/<language>")
# def name(language):
# 	if language == 'EN':
# 		return render_template('english_name.html')
# 	else:
#     	return render_template('home.html')

# @app.route("/email")
# def email():
#     return render_template('home.html')


if __name__ == '__main__':
    app.run(debug = True)