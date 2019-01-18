import json
import timeline_grapher

def main():
    configuration_file = "config.json"
    print("Reading: config.json")
    with open(configuration_file) as config:
        data = json.load(config)
        APIKey = data["APIKey"]
        Username = data["Username"]
        Chats = data["Chats"]

        print("Graph Options: ")
        print("    1: Chat Frequency Time Series Grapher")
        print("    2: Individual Chat Frequency Time Series Grapher")
        selector = input("Pick a grapher: ")

        if int(selector) == 1:
                print("Calling: Chat Frequency Time Series Grapher")
                url = timeline_grapher.chat_frequency_ts_grapher(APIKey, Username, Chats)
        elif int(selector) == 2:
                print("Calling: Individual Chat Frequency Time Series Grapher") 
                url = timeline_grapher.freq_equality_ts_grapher(APIKey, Username, Chats)
        else:
                url = "Na son."

        print(url)

if __name__ == "__main__":
    main()