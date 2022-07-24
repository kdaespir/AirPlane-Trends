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

def by_dates(df, date_type="single"):
    '''
    Allows the user to specify a date or range of dates. once specified function returns a dataframe with just information from that date

    '''
    dates = df["Fly Date"].unique()
    if date_type == "single":
        target = int(float(input("Please Enter A Date. Format = YYYYMM: ")))

        while target not in dates:
            print("Invalid Date Entered")
            target = int(float(input("Please Enter A Date. Format = YYYYMM: ")))

        df = df.loc[df["Fly Date"] == target]
    elif date_type == "range":

        lower_bound = int(float(input("Please Enter The Lower Bound Date. Format = YYYYMM: ")))
        upper_bound = int(float(input("Please Enter The Upper Bound Date. Format = YYYYMM: ")))

        while lower_bound not in dates:
            print("Invalid Date Entered")
        
        while upper_bound not in dates:
            print("Invalid Date Entered")
        
        df = df.loc[(df["Fly Date"] >= lower_bound) & (df["Fly Date"] <= upper_bound)]
        df.columns = ["Mean", "Std dev", "Variance", "P0", "P25", "P50", "P75", "P100"]

    return df

def main():
# Loads the dataset into the variable data
    data = pd.read_csv(r"D:\Users\Owner\Desktop\Python Projects\AirPlane Trends\flights.csv")
    numeric_data = data[data.columns[6:]]
    x = by_dates(numeric_data, date_type="range")
    x = get_stats(x)
    print(x)

main()
