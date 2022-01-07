from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="Michael is here"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

# delete what is currently stored in session
@app.route('/reset')
def reset():
    # clear all keys
    session.clear()
    # clear a specific key
    session.pop('count') 
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
