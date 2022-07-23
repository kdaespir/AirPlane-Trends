import pandas as pd
import numpy as np

data = pd.read_csv(r"D:\Users\Owner\Desktop\Python Projects\AirPlane Trends\flights.csv")
def get_stats(df):
    x = df[df.columns[6:]]
    numeric_data = df.columns[6:]
    means = []
    sd = []
    var = []
    p0, p25, p50, p75, p100 = [], [], [], [], []

    for item in numeric_data:
        means += [np.mean(x[item])]
        sd += [np.std(x[item])]
        p0 += [np.quantile(x[item], 0)]
        p25 += [np.quantile(x[item], .25)]
        p50 += [np.quantile(x[item], .50)]
        p75 += [np.quantile(x[item], .75)]
        p100 += [np.quantile(x[item], 1)]
        var += [np.var(x[item])]
        pass
    all_data = list(zip(means, sd, var, p0, p25, p50, p75, p100))
    all_data = pd.DataFrame(all_data)
    all_data.columns = ["Mean", "Std dev", "Variance", "P0", "P25", "P50", "P75", "P100"]
    all_data.index = df.columns[6:]
    return all_data

def by_dates(df):
    dates = df["Fly Date"].unique()
    flight_counts = []
    for item in dates:
        flight_counts += [df.loc[df["Fly Date"] == item].shape[0]]
    # test = df.loc[]
    return flight_counts

x = by_dates(data)
print(x)