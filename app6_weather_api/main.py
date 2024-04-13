from flask import Flask, render_template
import pandas as pd

#df = pandas.read_csv("app6_weather_api\\data_small")
app = Flask(__name__)


stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/vi/<station>/<date>/")
def about(station, date):
    filename = "app6_weather_api/data_small/TG_STAID" + str(station).zfill(6) + ".txt" 
    df = df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"], sep=",", engine="python", skipfooter=1)
    temperature = df.load[df['    DATE'] == "date"]['   TG'].squeeze() / 10
    return {"station": station,
             "date": date,
               "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"]))
    result = df.to_dict()
    return result
                    

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict()
    print(result)





if __name__ == "__main__":
    #Pass port parameter to run multiple instances
    app.run(debug=True)
