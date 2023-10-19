# =========================
# FIT3179 A2 Data scraping!
# =========================
from datetime import datetime

import pandas as pd

def strip_aus_weather():

    _df = pd.read_csv("weatherAUS.csv")

    _buckets = []
    _min_temp, _max_temp = [], []
    _avg_rain, _count_avg = [], []

    # -- organize names into buckets.

    for index, row in _df.iterrows():

        if row["Location"] not in _buckets:
            _buckets.append(row["Location"])
            _min_temp.append(1000)
            _max_temp.append(0)
            _avg_rain.append(0)
            _count_avg.append(0)

    # -- grab the states min, max temp, avg rainfall.

    for index, row in _df.iterrows():

        _index = _buckets.index(row["Location"])

        if row["MinTemp"] < _min_temp[_index]:
            _min_temp[_index] = row["MinTemp"]

        if row["MaxTemp"] > _max_temp[_index]:
            _max_temp[_index] = row["MaxTemp"]

        # -- try catch null or missing values.

        try:
            rain = int(row["Rainfall"])
        except ValueError:
            rain = 0

        _avg_rain[_index] += rain
        _count_avg[_index] += 1

    # -- get rainfall average.

    for i in range(0,len(_buckets)):

        _avg_rain[i] /= _count_avg[i]

    # -- get temperature median.

    _new_df = pd.DataFrame({"location": _buckets,
                            "min_temp": _min_temp,
                            "max_temp": _max_temp,
                            "rainfall": _avg_rain,
                            "records": _count_avg})

    _new_df.to_csv("AustraliaWeather.csv")


strip_aus_weather()