from flask import Flask, render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def profile():
    return "We can not only write strings in this flask program but can also integrate various programs in it" 

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/login/profile')
def hi():
    return render_template('Profile.html')       

@app.route('/login/profile/comments')
def comments():
    return "We can even make this site functional by adding various features to it"

if __name__ == '__main__':
    app.run(debug=True)
  