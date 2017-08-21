import read
import pandas as pd

f = read.load_data()
domains = f['url'].value_counts()
domains = domains[:99:]
for name, row in domains.items():
    print("{0}: {1}".format(name, row))
