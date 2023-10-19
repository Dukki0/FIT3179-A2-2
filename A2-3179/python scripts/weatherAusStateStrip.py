import pandas as pd

def strip_aus_weather():

    _df = pd.read_csv("AustraliaWeather.csv")

    _locales = []
    _temps = []

    for index, row in _df.iterrows():

        _locales.append(row["location"])

        _min = row["min_temp"]
        _max = row["max_temp"]
        _list = []

        while _min < _max:
            _list.append(_min)
            _min += 1

        _temps.append(_list)

    # -- get temperature median.

    _new_df = pd.DataFrame({"location": _locales, "temp": _temps})

    _new_df.to_csv("GantTemps.csv")


strip_aus_weather()