from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from model import fetch_apod

app = Flask(__name__)
app.secret_key = 'secret_for_flashing_messages'  

# Landing Page:
@app.route('/')
def home():
    today = date.today().isoformat()
    try:
        apod_data = fetch_apod(today)
        return render_template("home.html", apod=apod_data, today=today)
    except Exception as e:
        return f"ERROR: {e}"

# History Page:
@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'POST':
        selected_date = request.form.get('date')
        try:
            # Validation: Not in the future or before June 16, 1995
            if selected_date > date.today().isoformat():
                flash("Date cannot be in the future.")
            elif selected_date < "1995-06-16":
                flash("Date cannot be before the date June 16, 1995.")
            else:
                apod_data = fetch_apod(selected_date)
                return render_template("history.html", apod=apod_data, selected_date=selected_date)
        except Exception as e:
            flash(str(e))

    return render_template("history.html", apod=None, selected_date=None)

if __name__ == "__main__":
    app.run(debug=True)
