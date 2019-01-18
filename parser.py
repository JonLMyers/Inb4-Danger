import json
import datetime
#from datetime import datetime

def get_timestamps(chat_log):
    timestamps = []
    with open(chat_log) as json_messages:
        data = json.load(json_messages)
        for message in data['messages']:
            raw_timestamp = message['timestamp_ms']
            clean_timestamp = datetime.datetime.utcfromtimestamp(int(raw_timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
            timestamps.append(clean_timestamp)
    return timestamps

def get_names(chat_log):
    names = []
    with open(chat_log) as json_messages:
        data = json.load(json_messages)
        for participant in data['participants']:
            names.append(participant["name"])
    return names

def build_timestamp_name_structure(chat_logs):
    structures = []
    with open(chat_logs) as json_messages:
        data = json.load(json_messages)
        for message in data['messages']:
            raw_timestamp = message['timestamp_ms']
            clean_timestamp = datetime.datetime.utcfromtimestamp(int(raw_timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
            name = message['sender_name']
            structure = {"timestamp": clean_timestamp, "name": name}
            structures.append(structure)
    return structures

def to_unix_time(time_year, time_month, time_day):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (datetime.datetime(year=time_year, month=time_month, day=time_day) - epoch).total_seconds() * 1000