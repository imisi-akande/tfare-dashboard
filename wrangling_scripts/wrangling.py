import pandas as pd
import plotly.graph_objs as go


def clean_average_data(dataset, keepcolumns = ['State', '2016', '2020'], value_variables = ['2016', '2020']):
    """Clean average transport fare data for a visualization dashboard

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
    """Clean the percentage change transport fare data for a visualization dashboard

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
    df.columns = ['state','year','airfare']
    df.sort_values('airfare', ascending=False, inplace=True)
    statelist = df.state.unique().tolist()

    for state in statelist:
      x_val = df[df['state'] == state].year.tolist()
      y_val =  df[df['state'] == state].airfare.tolist()
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
                yaxis = dict(title = 'Average Air transport fare'),
                )

    # second chart plots the percentage change in Airfare in different
    # states between 2016 and 2020 as bar chart
    graph_two = []
    df = clean_percentage_data('data/states_airfare.csv')
    df.columns = ['state','year','airfare']
    df.sort_values('airfare', ascending=False, inplace=True)
    df = df[df['year'] == 'percentage-change-16-20'] 

    graph_two.append(
      go.Bar(
      x = df.state.tolist(),
      y = df.airfare.tolist(),
      )
    )

    layout_two = dict(title = 'Percentage change in Air transport Fare per state <br> between the year 2016 and 2020',
                xaxis = dict(title = 'State',),
                yaxis = dict(title = '% change in Air transport fare'),
                )

    # third chart plots average transport fare between cities in 2016 and 2020
    # as a line chart
    graph_three = []
    df = clean_average_data('data/states_inter_city_bus_journey.csv')
    df.columns = ['state','year','inter_city_bus_fare']
    df.sort_values('inter_city_bus_fare', ascending=False, inplace=True)

    for state in statelist:
        x_val = df[df['state'] == state].year.tolist()
        y_val =  df[df['state'] == state].inter_city_bus_fare.tolist()

        graph_three.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = state
            )
        )
    layout_three = dict(title = 'Average Transport Fare between cities<br> in state routes in the year 2016 and 2020',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=2016, dtick=4),
                yaxis = dict(title = 'Average intercity transport fare'),
                )

    # fourth chart plots the percentage change in transport fare between cities 
    # in state route between 2016 and 2020 as bar chart
    graph_four = []
    df = clean_percentage_data('data/states_inter_city_bus_journey.csv')
    df.columns = ['state','year','inter_city_bus_fare']
    df.sort_values('inter_city_bus_fare', ascending=False, inplace=True)
    df = df[df['year'] == 'percentage-change-16-20']

    graph_four.append(
      go.Bar(
      x = df.state.tolist(),
      y = df.inter_city_bus_fare.tolist(),
      )
    )

    layout_four = dict(title = 'Percentage change in intercity transport Fare per state <br> between the year 2016 and 2020',
                xaxis = dict(title = 'State',),
                yaxis = dict(title = '% change in intercity transport-fare'),
                width=800,
                height=400,
                )

    # fifth chart plots average transport fare between cities in 2016 and 2020
    # as a line chart
    graph_five = []
    df = clean_average_data('data/states_intra_city_bus_journey.csv')
    df.columns = ['state','year','intra_city_bus_fare']
    df.sort_values('intra_city_bus_fare', ascending=False, inplace=True)

    for state in statelist:
        x_val = df[df['state'] == state].year.tolist()
        y_val =  df[df['state'] == state].intra_city_bus_fare.tolist()

        graph_five.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = state
            )
        )
    layout_five = dict(title = 'Average Transport Fare within cities<br> in a particular state in the year 2016 and 2020',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=2016, dtick=4),
                yaxis = dict(title = 'Average intracity transport fare'),
                )

    # sixth chart plots the percentage change in transport fare between cities
    # between 2016 and 2020 as bar chart
    graph_six = []
    df = clean_percentage_data('data/states_intra_city_bus_journey.csv')
    df.columns = ['state','year','intra_city_bus_fare']
    df.sort_values('intra_city_bus_fare', ascending=False, inplace=True)
    df = df[df['year'] == 'percentage-change-16-20']

    graph_six.append(
      go.Bar(
      x = df.state.tolist(),
      y = df.intra_city_bus_fare.tolist(),
      )
    )

    layout_six = dict(title = 'Percentage change in intracity transport Fare per state <br> between the year 2016 and 2020',
                xaxis = dict(title = 'State',),
                yaxis = dict(title = '% change in intracity transport-fare'),
                width=800,
                height=400,
                )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))
    figures.append(dict(data=graph_six, layout=layout_six))

    return figures