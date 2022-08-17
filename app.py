import pandas as pd

# set URL
URL = "https://www.cdc.gov/wcms/vizdata/poxvirus/monkeypox/data/USmap_counts.csv"

# read URL
df = pd.read_csv(url)

# save to CSV
df.to_csv('./data/USmap_counts.csv')
