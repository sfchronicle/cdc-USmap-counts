import pandas as pd

# set URL
url = "https://www.cdc.gov/wcms/vizdata/poxvirus/monkeypox/data/USmap_counts.csv"

# read URL
df = pd.read_csv(url)

# save to CSV
df.to_csv('./data/USmap_counts.csv')

# call state population data
pop = pd.read_csv('./data/state_pop.csv')

# join case data with population
dfpop = pd.merge(df, pop, left_on='Location', right_on='State')

# calculate per 100K rate and put in new column
dfpop['per100k'] = dfpop['Cases'] / dfpop['pop_est_2021'] *100000

# save to CSV
dfpop.to_csv('./data/state_mp_per100k.csv')

# create metadata file 
def createMetadata():
    print('Creating metadata...')
    # Save current date to variable in this format: Aug. 4, 2022
    date = datetime.datetime.now().strftime("%b. %-d, %Y")
    s = f'Data as of {date}'
    data = {}

    # Create nested dictionary with metadata
    data['annotate'] = {'notes': s}

    json_data = json.dumps(data)
    with open('data/metadata.json', 'w') as f:
        f.write(json_data)
