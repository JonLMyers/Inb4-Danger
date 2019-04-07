import json
import datetime
import uuid

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

def filter_messenger_emoji(content):
    return content

def indentify_image(content):
    return False

def build_block(content, message_block, name):
    if not indentify_image(content):
        filtered_content = filter_messenger_emoji(content)
        block_json = {'Name': name, 'Content': content}
        message_block.append(block_json)
    else:
        # We should add a placeholder for images
        # It would be super neat if we could generate a tag for an image
        # sounds like some intense processing...
        # Fuck it lets do it.
        pass
    return message_block

# We need to come up with an average delta of time between two
# participants of a conversation.
    # Maybe we can avoid this by just building blocks of exchanges
    # Person A sends a block of messages
    # Person B responds with a block of messages
    # Person A responds... CUT.  This is a bucket.
        # What happens when person B cuts off person B
        # BUT Person B already sent the next message?
            # Store a buffer block or 2 for analysis

# turns out conversations are not easily blocked in an ABABABAB
# We need to use time/frequency to build blocks from a stream
# Consider Asyncioing this boi ^.^
def build_conversation_buckets(chat_logs):
    message_block = []
    conversation_buckets = []
    previous_sender = ""
    block_counter = 0
    setup_run = True

    with open(chat_logs) as json_messages:
        data = json.load(json_messages)
        
        # O(N)
        for message in data['messages']:
            name = message['sender_name']
            content = message['content']
            
            if not setup_run:
                if name == previous_sender:
                    message_block = build_block(content, message_block, name)
                else:
                    block_counter += 1
                    previous_sender = name
                    if block_counter == 2:
                        # Build the bucket
                        bucket_json = {'ID': str(uuid.uuid4()), 'Block': message_block, 'Tags': ''}
                        conversation_buckets.append(bucket_json)
                        message_block = []
                    else:
                        message_block = build_block(content, message_block, name)
                        previous_sender = name
            else:
                message_block = build_block(content, message_block, name)
                previous_sender = name
                setup_run = False

    return conversation_buckets

#Recommended time_delta of 6 hours
#Eventually we will compute this for the user
def get_daily_conversation_bucket(chat_logs, time_delta)
    message_block = []
    daily_blocks = []
    last_message_timestamp = 0
    
    with open(chat_logs) as json_messages:
        data = json.load(json_messages)
        for message in data['messages']:
            name = message['sender_name']
            content = message['content']
            timestamp = message['timestamp_ms']

        if timestamp + time_Delta > last_message_timestamp:
            block_json{'ID': str(uuid.uuid4()), 'Block': message_block}
            daily_blocks.append(block_json)
            message_block = []
            message_block.append(message)
        else:
            message_block.append(message)

            