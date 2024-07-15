import nltk
from nltk.chat.util import Chat, reflections

# Sample responses and patterns
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by a developer. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
]

# Create the chatbot
def chatbot():
    print("Hi, I'm the chatbot you created. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()