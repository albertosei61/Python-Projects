from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/vi/<station>/<date>/")
def about(station, date):
    temperature = 23
    return {"station": station, 
            "date": date, 
            "temperature": temperature}

if __name__ == "__main__":
    #Pass port parameter to use multiple apps
    app.run(debug=True, port=5001)
