from flask import Flask

messages = [
    {'sender': 'Вася',
     'text': 'Ты кто?',
     'time': '12.30'},

    {'sender': 'Петя',
     'text': 'Дед Мороз!',
     'time': '12.31'}
]

def add_message(sender, text):
    new_message = {
        'sender': sender,
        'text': text,
        'time': '13.30'
    }
    messages.append(new_message)

def print_mass(message):
    print(f"[{message['sender']}] {message['text']} : {message['time']}")

add_message('Маня', 'Привет')
add_message('Слон', 'Мууууу')

for mess in messages:
    print_mass(mess)

