# =========================
# FIT3179 A2 Data scraping!
# =========================
from datetime import datetime

import pandas as pd

def strip_by_column(file, name):

    _df = pd.read_csv(file)

    _all_dates = []
    _all_temps = []

    print("Searching for cities : " + "Name")
    _percentile = len(_df) / 100
    _total_percent = 0
    _percent_at = 0

    for index, row in _df.iterrows():

        if _percent_at >= _percentile:
            _total_percent += 1
            print(str(_total_percent) + "%")
            _percent_at = 0

        if row["City"] == name:
            _all_dates.append(row["dt"])
            _all_temps.append(row["AverageTemperature"])

        _percent_at += 1

    _new_df = pd.DataFrame({"date": _all_dates, "temp": _all_temps})

    print("")
    print(len(_new_df))
    print("")
    _new_df.to_csv("Just_" + name + "_Temperatures.csv")


def get_min_and_max_temps(file, name):

    _df = pd.read_csv(file)
    _all_dates = []
    _min_temps = []
    _max_temps = []
    _avg_temps = []
    _avg_temps_count = []

    # ---------------------------
    # -- Bucket the date stamps.
    # ---------------------------

    def v_date(r):
        return r[6] == "1" and r[5] == "0" and ((r[0] == "1" and r[1] == "9") or (r[0] == "2" and r[1] == "0"))

    for index, row in _df.iterrows():
        if row["date"] not in _all_dates and v_date(row["date"]):
            _all_dates.append(row["date"])
            _min_temps.append(10000)
            _max_temps.append(0)
            _avg_temps.append(0)
            _avg_temps_count.append(0)

    # ---------------------------
    # -- find min and max dates.
    # ---------------------------

    _temp_line = 0
    _temps_count = 0

    for index, row in _df.iterrows():

        if v_date(row["date"]):

            # -- grab date as index
            _index = _all_dates.index(row["date"])
            _temp = row["temp"]

            _avg_temps[_index] = _temp
            _temp_line += _temp
            _temps_count += 1

    print(_temp_line / _temps_count)

    _new_df = pd.DataFrame({"date": _all_dates, "avg_temp": _avg_temps})
    _new_df.to_csv("Just_" + name + "_TempStats.csv")

