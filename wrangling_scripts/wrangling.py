import pandas as pd
import plotly.graph_objs as go


def clean_average_data(dataset, keepcolumns = ['State', '2016', '2020'], value_variables = ['2016', '2020']):
    """Clean transport fare data for a visualization dashboard

    Keeps data range of dates in keep_columns variable and data for all states
    Reorients the columns into a year, state and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """
    df = pd.read_csv(dataset)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]

    statelist = df["State"].tolist()

    df = df[df['State'].isin(statelist)]

    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='State', value_vars = value_variables)
    df_melt.columns = ['state','year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # output clean csv file
    return df_melt

def clean_percentage_data(dataset, keepcolumns = ['State', 'percentage-change-16-18', 'percentage-change-16-20'], value_variables = ['percentage-change-16-18', 'percentage-change-16-20']):
    """Clean transport fare data for a visualization dashboard

    Keeps data range of dates in keep_columns variable and data for all states
    Reorients the columns into a year, state and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """
    df = pd.read_csv(dataset)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]

    statelist = df["State"].tolist()

    df = df[df['State'].isin(statelist)]

    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='State', value_vars = value_variables)
    df_melt.columns = ['state','year', 'variable']
    # df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # output clean csv file
    return df_melt

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots average transport fare by Air per state in 2016 and 2020 
    # as a line chart
    graph_one = []
    df = clean_average_data('data/states_airfare.csv')
    df.columns = ['state','year','averagefare']
    df.sort_values('averagefare', ascending=False, inplace=True)
    statelist = df.state.unique().tolist()

    for state in statelist:
      x_val = df[df['state'] == state].year.tolist()
      y_val =  df[df['state'] == state].averagefare.tolist()
      graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = state
          )
      )

    layout_one = dict(title = 'Average Transport Fare by Air <br> per State in the year 2016 and 2020',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=2016, dtick=4),
                yaxis = dict(title = 'Hectares'),
                )

    # second chart plots the  percentage change in transport fare in different 
    # states between 2016 and 2020 as bar chart
    graph_two = []
    df = clean_percentage_data('data/states_airfare.csv')
    df.columns = ['state','years','percentfare']
    df.sort_values('percentfare', ascending=False, inplace=True)
    df = df[df['years'] == 'percentage-change-16-20'] 

    graph_two.append(
      go.Bar(
      x = df.state.tolist(),
      y = df.percentfare.tolist(),
      )
    )

    layout_two = dict(title = 'Percentage change in Air transport Fare per state <br> between the year 2016 and 2020',
                xaxis = dict(title = 'State',),
                yaxis = dict(title = '% change in transport-fare'),
                )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))

    return figures