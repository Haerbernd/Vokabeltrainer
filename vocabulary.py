import json
import random
import sys
import os

# opens the vocabulary dictionary
file = open('./vocab/vocabulary.json', 'r+', encoding='UTF-8')
vocab = json.load(file)
file.close()

# opens the config file
file = open('./config/config.json', 'r+', encoding='UTF-8')
config = json.load(file)
file.close()

# decides the language of the program
if config['program-language'] == 'de':
    file = open('./config/german.json', 'r+', encoding='UTF-8')
    prog_text = json.load(file)
    file.close()
elif config['program-language'] == 'en':
    file = open('./config/english.json', 'r+', encoding='UTF-8')
    prog_text = json.load(file)
    file.close()
else:
    input('\u001b[31mError\u001b[0m: Invalid option at "program-language" in "config.json"\nUse either "de" or "en"')
    sys.exit(0)

if config['vocab-to'] == 'en':
    if config['program-language'] == 'de':
        vocab_lang = 'Deutsch'
        vocab_lang_irl = 'Englisch'
elif config['vocab-to'] == 'de':
    if config['program-language'] == 'en':
        vocab_lang = 'English'
        vocab_lang_irl = 'German'


def random_vocab():
    chosen = random.choice(list(vocab[vocab_lang]))
    return chosen


if config['program-language'] == 'de':
    print(prog_text['1'])
elif config['program-language'] == 'en':
    print(prog_text['1'])

if config['os'] == 'windows':
    os.system('cls')
elif config['os'] == 'linux':
    os.system('clear')
else:
    input('\u001b[31mError\u001b[0m: Invalid option at "os" in "config.json"\nUse either "windows" or "linux"')
    sys.exit(0)

while True:
    vocabulary = random_vocab()
    print(prog_text['1'])
    print(prog_text['2'], vocabulary.upper(), prog_text['3'], vocab_lang_irl, prog_text['7'])
    player_input = input('>')
    if player_input.lower() == vocab[vocab_lang][vocabulary]:
        print(prog_text['5'])
        input(prog_text['4'])
    elif player_input.lower() == '!quit':
        sys.exit(0)
    else:
        print(print(prog_text['6']), vocab[vocab_lang][vocabulary])
        input(prog_text['4'])
    if config['os'] == 'windows':
        os.system('cls')
    elif config['os'] == 'linux':
        os.system('clear')
