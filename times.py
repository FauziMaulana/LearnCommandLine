import read
import pandas as pd
import dateutil as dt
import datetime
import read

f = read.load_data()

def dates(x):
    y = dt.parser.parse(x)
    return y.hour
f['hour'] = f['submission_time'].apply(dates)
print(f['hour'].value_counts().head())
