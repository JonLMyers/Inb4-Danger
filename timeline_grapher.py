import parser
import analyzer
import plotly
import datetime
import plotly.plotly as py
import plotly.graph_objs as go
import colorlover as cl


colors = cl.scales['11']['div']['RdBu']

def chat_frequency_ts_grapher(APIKey, Username, chats):
    print("Defining: Plot.ly API Connection.")
    plotly.tools.set_credentials_file(username=Username, api_key=APIKey)
    data = []
    print("Configuring: Graph")
    print("Processing: Data")
    for chat in chats:
        name = chat["Name"]
        print("    Adding: " + name)
        color = chat["Color"]
        messages = chat["Messages"]

        y = []
        x = []
        timestamps = parser.get_timestamps(messages)
        date_count_structures = analyzer.daily_message_count(timestamps)

        for date_count in date_count_structures:
            x.append(datetime.datetime(year=int(date_count["Year"]), month=int(date_count["Month"]), day=int(date_count["Day"])))
            y.append(int(date_count["Count"]))
        
        plot = go.Scatter(x=x, y=y, name=name, opacity = 0.8, line = dict(color = color))
        data.append(plot)

    layout = go.Layout(xaxis = dict(
                    range = [parser.to_unix_time(2014, 10, 20),
                                parser.to_unix_time(2018, 12, 15)]
        ))
    print("Printing: Graph")
    fig = go.Figure(data = data, layout = layout)
    url = py.plot(fig)
    return url 

def freq_equality_ts_grapher(APIKey, Username, chats):
    print("Defining: Plot.ly API Connection.")
    plotly.tools.set_credentials_file(username=Username, api_key=APIKey)
    data = []
    print("Configuring: Graph")
    print("Processing: Data")
    color_num = 0
    chat = chats[0]
    names = parser.get_names(chat["Messages"])
    
    for name in names:
        print("    Adding: " + name)
        color = colors[color_num]
        color_num = color_num + 1
        messages = chat["Messages"]

        y = []
        x = []
    
        timestamp_names = parser.build_timestamp_name_structure(messages)
        date_count_structures = analyzer.individual_daily_message_count(timestamp_names, name)

        for structure in date_count_structures:
            x.append(datetime.datetime(year=int(structure["Year"]), month=int(structure["Month"]), day=int(structure["Day"])))
            y.append(int(structure["Count"]))
        
        plot = go.Scatter(x=x, y=y, name=name, opacity = 0.8, line = dict(color = color))
        data.append(plot)

    layout = go.Layout(xaxis = dict(
                    range = [parser.to_unix_time(2018, 10, 20),
                                parser.to_unix_time(2019, 1, 15)]
        ))
    print("Printing: Graph")
    fig = go.Figure(data = data, layout = layout)
    url = py.plot(fig)
    return url
