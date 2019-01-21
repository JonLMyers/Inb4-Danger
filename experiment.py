import parser

def test_conversation_buckets(messages):
    chats = messages[0]
    chat = chats["Messages"]
    buckets = parser.build_conversation_buckets(chat)
    return buckets