import pandas as pd
import numpy as np



def get_stats(df):
    '''
    Gets various descriptive statistics of the dataset. incuding mean, quantile, standard deviation and variance
    '''
    numeric_data = df.columns
    means = []
    sd = []
    var = []
    p0, p25, p50, p75, p100 = [], [], [], [], []

    for item in numeric_data:
        means += [np.mean(df[item])]
        sd += [np.std(df[item])]
        p0 += [np.quantile(df[item], 0)]
        p25 += [np.quantile(df[item], .25)]
        p50 += [np.quantile(df[item], .50)]
        p75 += [np.quantile(df[item], .75)]
        p100 += [np.quantile(df[item], 1)]
        var += [np.var(df[item])]
        pass
    all_data = list(zip(means, sd, var, p0, p25, p50, p75, p100))
    all_data = pd.DataFrame(all_data)
    all_data.columns = ["Mean", "Std dev", "Variance", "P0", "P25", "P50", "P75", "P100"]
    all_data.index = df.columns
    return all_data

def by_dates(df):
    dates = df["Fly Date"].unique()
    flight_counts = []
    dist_traveled = []
    for item in dates:
        flight_counts += [df.loc[df["Fly Date"] == item].shape[0]] 

        dist_traveled = df.loc[df["Fly Date"] == item]["Distance"]
        print(len(dist_traveled), len(flight_counts))
        
    # test = df.loc[]
    return flight_counts

def main():
# Loads the dataset into the variable data
    data = pd.read_csv(r"D:\Users\Owner\Desktop\Python Projects\AirPlane Trends\flights.csv")
    numeric_data = data[data.columns[6:]]
    print(numeric_data)

main()
# x = by_dates(data)
# print(x)