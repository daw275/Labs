from flask import Flask, render_template, request
import segno 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", qrcode_uri=None, message=None)
    else:
        data = request.form.get("data")

        qrcode = segno.make(data) 
        qrcode_uri = qrcode.svg_data_uri(scale=4)  

        return render_template("index.html", qrcode_uri=qrcode_uri, message=data)

if __name__ == "__main__":
    app.run(debug=True)
