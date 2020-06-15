import pandas as pd

def data_wrangling():
    df = pd.read_csv('data/states_airfare.csv')

    # Filter for 2016 and 2020, all states involved
    df = df[['State','2016', '2020']]
    statelist = df["State"].tolist()

    # melt year columns and convert year to date time
    df_melt = df.melt(id_vars='State', value_vars = ['2016', '2020'])
    df_melt.columns = ['state','year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # add column names
    df_melt.columns = ['state', 'year', 'percentfare']

    # prepare data into x, y lists for plotting
    df_melt.sort_values('percentfare', ascending=False, inplace=True)

    data = []
    for state in statelist:
        x_val = df_melt[df_melt['state'] == state].year.tolist()
        y_val =  df_melt[df_melt['state'] == state].percentfare.tolist()
        data.append((state, x_val, y_val))
        # print(state, x_val, y_val)

    return data