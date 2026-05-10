from flask import Flask, render_template
from flask import session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "wardiere-secret-key"


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        return redirect(url_for("dashboard"))

    return render_template('login.html', active_page='login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == "POST":
        return redirect(url_for("dashboard"))

    return render_template('signup.html', active_page='signup')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')


@app.route('/live-services')
def live_services():
    return render_template('live_services.html', active_page='live_services')


@app.route('/p2p-cleaning')
def p2p_cleaning():
    return render_template('p2p_cleaning.html', active_page='cleaning')


@app.route('/lending-supplies')
def lending_supplies():
    return render_template('lending_supplies.html', active_page='supplies')


@app.route('/moving-supplies')
def moving_supplies():
    return render_template('moving_supplies.html', active_page='moving')


@app.route('/find-properties')
def find_properties():
    return render_template('find_properties.html', active_page='properties')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html', active_page='wallet')

if __name__ == "__main__":
    app.run(debug=True)