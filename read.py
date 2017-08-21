import pandas as pd

def load_data():
    hn_stories = pd.read_csv("C:/Users/i7/cmdline/1/hn_stories.csv")
    hn_stories.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return(hn_stories)

print(load_data())
