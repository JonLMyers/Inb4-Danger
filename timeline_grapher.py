import parser
import analyzer
import plotly
import datetime
import plotly.plotly as py
import plotly.graph_objs as go
#IF you don't remove this before committing I will kill you.
### IF YOU DON'T READ THE ABOVE BEFORE COMMITING I

def chat_frequency_ts_grapher(APIKey, Username, chats):
    print("Defining: Plot.ly API Connection.")
    plotly.tools.set_credentials_file(username=Username, api_key=APIKey)
    data = []
    print("Configuring: Graph")
    print("Processing: Data")
    for chat in chats:
        name = chat["Name"]
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

