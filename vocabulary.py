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
file = open('./config/language.json', 'r+', encoding='UTF-8')
prog_lang = json.load(file)
file.close()
if config['program-language'] in prog_lang['possible-options']:
    prog_text = prog_lang[config['program-language']]
else:
    print('\u001b[31mError\u001b[0m: Invalid option at "program-language" in "config.json"\n'
          'Use one of the following', prog_lang['possible-options'])
    input('Press any key...\n')
    sys.exit(0)

# decides which vocabularies are used
if config['vocab-to'] in config['possible-vocab-to-options']:
    vocab_origin_lang = vocab['lang-codes'][config['vocab-to']]['origin-lang']
    vocab_lang = vocab['lang-codes'][config['vocab-to']]['vocab-lang']
else:
    print('\u001b[31mError\u001b[0m: Invalid option at "possible-vocab-to-options" in "config.json"\n'
          'Use one of the following', config['possible-vocab-to-options'])
    input('Press any key...\n')
    sys.exit(0)


def random_vocab():
    chosen = random.choice(list(vocab[config['vocab-to']]))
    return chosen


# a first usage of colored text to ensure that it is initialized correctly (I had graphic bugs at first tests of the
# program and that is to solve the problem, I don't know if it's neccessary anymore)
# ensures that the right os is used
if config['os'] == 'windows':
    os.system('cls')
elif config['os'] == 'linux':
    os.system('clear')
else:
    input('\u001b[31mError\u001b[0m: Invalid option at "os" in "config.json"\nUse either "windows" or "linux"')
    sys.exit(0)

# main program
while True:
    vocabulary = random_vocab()
    print(prog_text['1'])
    print(prog_text['2'], vocabulary.upper(), prog_text['3'], prog_text[vocab_lang], prog_text['7'])
    player_input = input('>')
    if player_input.lower() == vocab[config['vocab-to']][vocabulary]:
        print(prog_text['5'])
        input(prog_text['4'])
    elif player_input.lower() == '!quit':
        sys.exit(0)
    else:
        print(prog_text['6'], vocab[config['vocab-to']][vocabulary])
        input(prog_text['4'])
    if config['os'] == 'windows':
        os.system('cls')
    elif config['os'] == 'linux':
        os.system('clear')
