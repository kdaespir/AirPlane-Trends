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
    counts = []

    for item in numeric_data:
        means += [np.mean(df[item])]
        sd += [np.std(df[item])]
        p0 += [np.quantile(df[item], 0)]
        p25 += [np.quantile(df[item], .25)]
        p50 += [np.quantile(df[item], .50)]
        p75 += [np.quantile(df[item], .75)]
        p100 += [np.quantile(df[item], 1)]
        var += [np.var(df[item])]
        # counts += 
        pass
    all_data = list(zip(means, sd, var, p0, p25, p50, p75, p100))
    all_data = pd.DataFrame(all_data)
    all_data.columns = ["Mean", "Std dev", "Variance", "P0", "P25", "P50", "P75", "P100"]
    all_data.index = df.columns
    return all_data

def by_dates(df):
    '''
    Allows the user to specify a date. once specified function returns a dataframe with just information from that date

    Note: add Ranges of dates. Example: 199006 to 200006. format will be (df.loc[(df["Fly Date"] >= lower_target) & (df["Fly Date"] <= upper_target)])
    '''
    dates = df["Fly Date"].unique()
    target = int(float(input("Please Enter A Date. Format = YYYYMM: ")))

    while target not in dates:
        print("Invalid Date Entered")
        target = int(float(input("Please Enter A Date. Format = YYYYMM: ")))
        
    df = df.loc[df["Fly Date"] == target]
    return df

def main():
# Loads the dataset into the variable data
    data = pd.read_csv(r"D:\Users\Owner\Desktop\Python Projects\AirPlane Trends\flights.csv")
    numeric_data = data[data.columns[6:]]
    x = by_dates(numeric_data)
    print(x)

main()
